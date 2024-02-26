global Add100

Add100:
    push ebp
    mov ebp, esp
    mov eax, [ebp+8]
    add eax, 100
    mov esp, ebp
    pop ebp
    ret
