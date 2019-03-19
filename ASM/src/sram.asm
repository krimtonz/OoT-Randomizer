load_rando_sram:
    addiu   sp, sp, -0x18
    sw      ra, 0x10(sp)
    sw      s0, 0x14(sp)
    jal     load_rando_save_ctxt
    nop
    lw		s0, 0x14(sp)
    lw      ra, 0x10(sp)
    addiu   sp, sp, 0x18
    lw      t6, 0x1354 (s0)   ; displaced
    jr      ra
    lw      t8, 0x0020 (sp)   ; displaced
