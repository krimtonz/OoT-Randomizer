#include "z64.h"
#include "gfx.h"

uint8_t display_tradequest(z64_gfx_t *gfx){

    if(z64_game.pause_ctxt.cursor_pos!=0 || z64_game.pause_ctxt.item_cursor!=0x16 || z64_game.pause_ctxt.screen_idx!=0) return 0;

    int x = 105;

    for(int i=Z64_ITEM_POCKET_EGG;i<=Z64_ITEM_CLAIM_CHECK;i++){
        sprite_t *sprite = &items_sprite;
        if(i%2==0) sprite = &items_sprite_gray;
        if(i%3==0) gDPSetPrimColor(gfx->poly_opa.p++,0,0,0,0,0,0xFF);
        else gDPSetPrimColor(gfx->poly_opa.p++,0,0,0xFF,0xFF,0xFF,0xFF);
        sprite_load(&(gfx->poly_opa),sprite, i, 1);
        sprite_draw(&(gfx->poly_opa),sprite,0,x,203,8,8);
        x+=10;
    }
    return 1;
}