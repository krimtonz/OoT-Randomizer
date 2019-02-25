#include "gfx.h"

#include "util.h"
#include "z64.h"

extern char FONT_TEXTURE;
extern char DPAD_TEXTURE;
#define font_texture_raw ((uint8_t *)&FONT_TEXTURE)
#define dpad_texture_raw ((uint8_t *)&DPAD_TEXTURE)

Gfx setup_db[] =
{
    gsDPPipeSync(),

    gsSPLoadGeometryMode(0),
    gsDPSetScissor(G_SC_NON_INTERLACE,
                  0, 0, Z64_SCREEN_WIDTH, Z64_SCREEN_HEIGHT),

    gsDPSetOtherMode(G_AD_DISABLE | G_CD_DISABLE |
        G_CK_NONE | G_TC_FILT |
        G_TD_CLAMP | G_TP_NONE |
        G_TL_TILE | G_TT_NONE |
        G_PM_NPRIMITIVE | G_CYC_1CYCLE |
        G_TF_BILERP, // HI
        G_AC_NONE | G_ZS_PRIM |
        G_RM_XLU_SURF | G_RM_XLU_SURF2), // LO

    gsSPEndDisplayList()
};

sprite_t stones_sprite = {
    NULL, 16, 16, 3,
    G_IM_FMT_RGBA, G_IM_SIZ_32b, 4
};

sprite_t medals_sprite = {
    NULL, 16, 16, 6,
    G_IM_FMT_IA, G_IM_SIZ_8b, 1
};

sprite_t items_sprite = {
    NULL, 32, 32, 90,
    G_IM_FMT_RGBA, G_IM_SIZ_32b, 4
};

sprite_t quest_items_sprite = {
    NULL, 24, 24, 20,
    G_IM_FMT_RGBA, G_IM_SIZ_32b, 4
};

sprite_t font_sprite = {
    NULL, 8, 14, 95,
    G_IM_FMT_IA, G_IM_SIZ_8b, 1
};

sprite_t dpad_sprite = {
    NULL, 32, 32, 1,
    G_IM_FMT_IA, G_IM_SIZ_16b, 2
};  

sprite_t items_sprite_gray = { 
    NULL, 32, 32, 90,
    G_IM_FMT_RGBA, G_IM_SIZ_32b, 4
};

int sprite_bytes_per_tile(sprite_t *sprite) {
    return sprite->tile_w * sprite->tile_h * sprite->bytes_per_texel;
}

int sprite_bytes(sprite_t *sprite) {
    return sprite->tile_count * sprite_bytes_per_tile(sprite);
}

void sprite_load(z64_disp_buf_t *db, sprite_t *sprite,
        int start_tile, int tile_count) {
    int width = sprite->tile_w;
    int height = sprite->tile_h * tile_count;
    gDPLoadTextureTile(db->p++,
            sprite->buf + (start_tile * sprite_bytes_per_tile(sprite)),
            sprite->im_fmt, sprite->im_siz,
            width, height,
            0, 0,
            width - 1, height - 1,
            0,
            G_TX_WRAP, G_TX_WRAP,
            G_TX_NOMASK, G_TX_NOMASK,
            G_TX_NOLOD, G_TX_NOLOD);
}

void sprite_draw(z64_disp_buf_t *db, sprite_t *sprite, int tile_index,
        int left, int top, int width, int height) {
    int width_factor = (1<<10) * sprite->tile_w / width;
    int height_factor = (1<<10) * sprite->tile_h / height;

    gSPTextureRectangle(db->p++,
            left<<2, top<<2,
            (left + width)<<2, (top + height)<<2,
            0,
            0, (tile_index * sprite->tile_h)<<5,
            width_factor, height_factor);
}

typedef float MtxF_t[4][4];

typedef union{
    MtxF_t mf;
    float f[16];
    struct{
        float xx, xy, xz, xw,
              yx, yy, yz, yw,
              zx, zy, zz, zw,
              wx, wy, wz, ww;
    };
} MtxF;

#define guDefMtxF(xx,xy,xz,xw, \
                  yx,yy,yz,yw, \
                  zx,zy,zz,zw, \
                  wx,wy,wz,ww)  {.f={ \
                      xx,xy,xz,xw, \
                      yx,yy,yz,yw, \
                      zx,zy,zz,zw, \
                      wx,wy,wz,ww}}

const MtxF desaturate = guDefMtxF(0.3086f, 0.6094f, 0.0820f, 0.f,
                                         0.3086f, 0.6094f, 0.0820f, 0.f,
                                         0.3086f, 0.6094f, 0.0820f, 0.f,
                                         0.f,     0.f,     0.f,     1.f);

void gfx_init() {
    file_t title_static = {
        NULL, z64_file_select_static_vaddr, z64_file_select_static_vsize
    };
    file_init(&title_static);

    file_t icon_item_24_static = {
        NULL, z64_icon_item_24_static_vaddr, z64_icon_item_24_static_vsize
    };
    file_init(&icon_item_24_static);

    file_t icon_item_static = {
        NULL, z64_icon_item_static_vaddr, z64_icon_item_static_vsize
    };
    file_init(&icon_item_static);

    file_t icon_item_static_gray = {
        NULL, z64_icon_item_static_vaddr, z64_icon_item_static_vsize
    };
    file_init(&icon_item_static_gray);

    struct rgba{
        uint8_t r;
        uint8_t g;
        uint8_t b;
        uint8_t a;
    };
    MtxF m = desaturate;
    for(int i=0;i<sprite_bytes(&items_sprite_gray)/4;++i){
        struct rgba p = ((struct rgba*)icon_item_static_gray.buf)[i];
        float r = p.r * m.xx + p.g * m.xy + p.b*m.xz + p.a * m.xw;
        float g = p.r * m.yx + p.g * m.yy + p.b*m.yz + p.a * m.yw;
        float b = p.r * m.zx + p.g * m.zy + p.b*m.zz + p.a * m.zw;
        float a = p.r * m.wx + p.g * m.wy + p.b*m.wz + p.a * m.ww;
        struct rgba n = {
            r = r<0x00?0x00:r>0xFF?0xFF:r,
            g = g<0x00?0x00:g>0xFF?0xFF:g,
            b = b<0x00?0x00:b>0xFF?0xFF:b,
            a = a<0x00?0x00:a>0xFF?0xFF:a,
        };
        ((struct rgba*)icon_item_static_gray.buf)[i] = n;
    }

    stones_sprite.buf = title_static.buf + 0x2A300;
    medals_sprite.buf = title_static.buf + 0x2980;
    items_sprite.buf = icon_item_static.buf;
    quest_items_sprite.buf = icon_item_24_static.buf;
    items_sprite_gray.buf = icon_item_static_gray.buf;

    dpad_sprite.buf = dpad_texture_raw;

    int font_bytes = sprite_bytes(&font_sprite);
    font_sprite.buf = heap_alloc(font_bytes);
    for (int i = 0; i < font_bytes / 2; i++) {
        font_sprite.buf[2*i] = (font_texture_raw[i] >> 4) | 0xF0;
        font_sprite.buf[2*i + 1] = font_texture_raw[i] | 0xF0;
    }
}
