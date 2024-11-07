.global _start
.section .text
_start:
	mov r0, #42
	mov r7, 0x01
	swi 0