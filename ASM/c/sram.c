#include <stdint.h>
#include "z64.h"

#define RANDO_SRAM_ADDR 0x08001470
#define RANDO_SRAM_BACK 0x080065B0

typedef struct {
    char                magic[8];               /* 0x0000 */
    uint32_t            scrub_flags;            /* 0x0008 */
    uint32_t            shop_flags;             /* 0x000C */
    struct{
        z64_xyzf_t      pos;                    /* 0x0010 */
        z64_angle_t     yaw;                    /* 0x001C */
        char            unk_0E_[0x0008];        /* 0x001E */
        uint16_t        entrance_idx;           /* 0x0026 */
        uint32_t        room_idx;               /* 0x0028 */
        int32_t         set;                    /* 0x002C */
    } fw;                                       /* 0x0030 */
} rando_save_ctxt_t;

extern rando_save_ctxt_t RANDO_SAVE_CTX;

void create_rando_file(){

    for(int i=0;i<sizeof(RANDO_SAVE_CTX)/2;i++){
        ((uint16_t*)&RANDO_SAVE_CTX)[i] = 0;
    }

    RANDO_SAVE_CTX.magic[0] = 'O';
    RANDO_SAVE_CTX.magic[1] = 'O';
    RANDO_SAVE_CTX.magic[2] = 'T';
    RANDO_SAVE_CTX.magic[3] = 'R';
    RANDO_SAVE_CTX.magic[4] = 'A';
    RANDO_SAVE_CTX.magic[5] = 'N';
    RANDO_SAVE_CTX.magic[6] = 'D';
    RANDO_SAVE_CTX.magic[7] = 'O';

    z64_Io(RANDO_SRAM_ADDR,&RANDO_SAVE_CTX,sizeof(RANDO_SAVE_CTX),OS_WRITE);

    // Displaced from Hook
    __asm__ volatile ("lw   $v0, 0x1354($s1);"
                      "lui  $s0, 0x8010;");
}

void save_rando_sram(){

    z64_Io(RANDO_SRAM_ADDR,&RANDO_SAVE_CTX,sizeof(RANDO_SAVE_CTX),OS_WRITE);
    z64_Io(RANDO_SRAM_BACK,&RANDO_SAVE_CTX,sizeof(RANDO_SAVE_CTX),OS_WRITE);

    // Displaced from Hook
    __asm__ volatile ("la    $a1, %0;"
                    ::
                    "i"(z64_file_addr));
}

int load_rando_save_ctxt_backup(){
    z64_Io(RANDO_SRAM_BACK,&RANDO_SAVE_CTX,sizeof(RANDO_SAVE_CTX),OS_READ);
    if(RANDO_SAVE_CTX.magic[0] == 'O' && RANDO_SAVE_CTX.magic[1] == 'O' &&
        RANDO_SAVE_CTX.magic[2] == 'T' && RANDO_SAVE_CTX.magic[3] == 'R' &&
        RANDO_SAVE_CTX.magic[4] == 'A' && RANDO_SAVE_CTX.magic[5] == 'N' &&
        RANDO_SAVE_CTX.magic[6] == 'D' && RANDO_SAVE_CTX.magic[7] == 'O') return 0;
    return 1;
}

void load_rando_save_ctxt(){
    z64_Io(RANDO_SRAM_ADDR,&RANDO_SAVE_CTX,sizeof(RANDO_SAVE_CTX),OS_READ);
    if(RANDO_SAVE_CTX.magic[0] == 'O' && RANDO_SAVE_CTX.magic[1] == 'O' &&
        RANDO_SAVE_CTX.magic[2] == 'T' && RANDO_SAVE_CTX.magic[3] == 'R' &&
        RANDO_SAVE_CTX.magic[4] == 'A' && RANDO_SAVE_CTX.magic[5] == 'N' &&
        RANDO_SAVE_CTX.magic[6] == 'D' && RANDO_SAVE_CTX.magic[7] == 'O') return;
    
    if(!load_rando_save_ctxt_backup()){
        save_rando_sram();
        return;
    }

    create_rando_file(); 
}