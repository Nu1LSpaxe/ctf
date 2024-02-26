global _start

section .texxt
_start:
    mov ebx, 42     ; exit status is 42
    mov eax, 1      ; sys_exit system call
    jmp skip        ; jump to "skip" label
    mov ebx, 13     ; exit status is 13 (won't be executed)
                    ; first "echo $?" after compile will be 42

skip:
    int 0x80
