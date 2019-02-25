menu_fix_tradequest:
    addiu sp, sp, -0x18
    sw ra, 0(sp)
    sw t9, 4(sp)
    sw t5, 8(sp)
    sw t1, 0xc(sp) 
    or a0, r0, t5
    jal display_tradequest
    nop
    ori t1, r0, 0x01
    beq v0, t1, @@skip
    lw ra, 0(sp)

    lw t1, 0xC(sp)
    lw t5, 8(sp)
    b @@return  
    lw t9, 4(sp)

@@skip:
    addiu ra, ra, 0xC60

@@return:
    jr ra
    addiu sp, sp, 0x18