global _start

_start:
    call func
    mov eax, 1
    int 0x80

func:
    mov ebx, 42
    ; return - method 1
    ; pop eax     ; return address
    ; jmp eax     ; return (base on address stored in eax)
    ; return - method 2
    ret
