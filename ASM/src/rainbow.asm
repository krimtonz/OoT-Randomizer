save_lighting_settings:
    addiu   sp, sp, -0x10
    sw      ra, 0x00(sp)
    sw      v0, 0x04(sp)
    sw      v1, 0x08(sp)
    sw      a0, 0x0C(sp)
    jal     process_lighting
    nop
    lw      a0, 0x0C(sp)
    lw      v1, 0x08(sp)
    lw      v0, 0x04(sp)
    lw      ra, 0x00(sp)
    addu    at, at, a0
    sw      t3, 0x0ADC(at)
    jr      ra
    addiu   sp, sp, 0x10