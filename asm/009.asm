global main
extern printf

section .data
    ; 0x0a is new line character
    msg db "Testing %i...", 0x0a, 0x00

main:
    push ebp
    mov ebp, esp
    push 123
    push msg
    call printf
    mov eax, 0      ; return value for main function
    mov esp, ebp
    pop ebp
    ret
