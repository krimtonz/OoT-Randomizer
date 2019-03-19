file_choose:
    ori t6, r0, 0x01
    
    beq t6, t5, @@skip
    ori at, r0, 0x02

    beq at, t5, @@skip
    nop

    ori at, r0, 0x03
    beq at, t5, @@skip
    nop
    
    b @@return
    nop

@@skip:
    or t5, r0, a0

@@return:
    or t6, r0, t5
    jr ra
    sh t5, 0x4A2A(v1)


erase_input:
    ori v1, r0, 0x04
    beq v1, t3, @@return
    nop
    blez t3, @@return
    nop

    or t3, r0, a0

@@return:
    sh t3, 0xCA2A(AT)
    jr ra
    lh v1, 0x4A2A(T0)