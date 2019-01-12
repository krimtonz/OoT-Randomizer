#include "rainbow.h"

#include "z64.h"

typedef struct
{
    uint8_t r;
    uint8_t g;
    uint8_t b;
} colorRGB_t;

uint8_t *scene_lighting = NULL;
uint8_t num_lighting = 0;

static uint32_t frames = 0;
static colorRGB_t colors[] =
{
    { 0xE0, 0x10, 0x10 }, //red
    { 0xE0, 0xE0, 0x10 }, //yellow
    { 0x10, 0xE0, 0x10 }, //green
    { 0x10, 0xE0, 0xE0 }, //cyan
    { 0x10, 0x10, 0xE0 }, //blue
    { 0xE0, 0x10, 0xE0 }, //purple
    { 0xE0, 0x10, 0x10 }, //red
};

// Config Variables
uint8_t rainbow_cycle_frames = 0x10;
uint8_t enable_rainbow_navi = 0x00;
uint8_t enable_rainbow_sword = 0x00;
uint8_t enable_rainbow_kokiri_tunic = 0x00;
uint8_t enable_rainbow_goron_tunic = 0x00;
uint8_t enable_rainbow_zora_tunic = 0x00;
uint8_t enable_rainbow_fog = 0x00;


colorRGB_t get_color(int index, int f)
{
    colorRGB_t ret;
    float tweenA, tweenB;

    tweenB = ((float)f / rainbow_cycle_frames);
    tweenA = 1 - tweenB;

    colorRGB_t cA = colors[index];
    colorRGB_t cB = colors[index + 1];

    ret.r = (uint8_t)((cA.r * tweenA) + (cB.r * tweenB));
    ret.g = (uint8_t)((cA.g * tweenA) + (cB.g * tweenB));
    ret.b = (uint8_t)((cA.b * tweenA) + (cB.b * tweenB));

    return ret;
}

void process_lighting(z64_game_t *game, uint32_t *header) {
    uint32_t *scene_file = ((uint32_t**)((uint32_t)game + 0xB0))[0];
    num_lighting = (header[0] & 0x00FF0000) >> 16;
    scene_lighting = (uint8_t*)(((uint32_t)scene_file) + (header[1] & 0x00FFFFFF));
}

void do_rainbow()
{
    frames++;
    if (frames >= rainbow_cycle_frames * 6)
        frames = 0;

    int index = frames / rainbow_cycle_frames;
    int f = frames % rainbow_cycle_frames;

    colorRGB_t color = get_color(index, f);

    if(enable_rainbow_fog){
        for(int i=0;i<num_lighting;i++){
            scene_lighting[(i*0x16) + 0] = color.r;
            scene_lighting[(i * 0x16) + 1] = color.g;
            scene_lighting[(i * 0x16) + 2] = color.b;
            scene_lighting[(i * 0x16) + 15] = color.r;
            scene_lighting[(i * 0x16) + 16] = color.g;
            scene_lighting[(i * 0x16) + 17] = color.b;
        }
    }

    if (enable_rainbow_sword) {
        uint8_t *sword_trail = (uint8_t*)0x80115DCE;
        for (int i = 0; i < 16; i += 4) {
            sword_trail[i] = color.r;
            sword_trail[i + 1] = color.g;
            sword_trail[i + 2] = color.b;
        }
    }
    if (enable_rainbow_navi) {
        if (z64_game.actor_list[7].first != NULL) {
            z64_actor_t *fairy = z64_game.actor_list[7].first;
            if (fairy->actor_id != 0x18 || fairy->variable != 0x00) {
                while (fairy->next != NULL) {
                    fairy = fairy->next;
                    if (fairy->actor_id == 0x18 && fairy->variable == 0x00) break;
                }
            }
            if (fairy != NULL) {
                float *fairyrgb = (float*)(((uint32_t)fairy) + 0x234);
                fairyrgb[0] = (float)color.r;
                fairyrgb[1] = (float)color.g;
                fairyrgb[2] = (float)color.b;
            }
        }

    }
    colorRGB_t *tunics = (colorRGB_t*)0x800F7AD8;
    if (enable_rainbow_kokiri_tunic) {
        tunics[0] = color;
    }

    if (enable_rainbow_goron_tunic) {
        tunics[1] = color;
    }

    if (enable_rainbow_zora_tunic) {
        tunics[2] = color;
    }

}