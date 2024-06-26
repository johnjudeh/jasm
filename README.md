# jasm

## What is it?

After building a
[programmable 8-bit computer](https://github.com/johnjudeh/breadboard-computer)
on breadboards with simple electronic components, I now have a computer with a
brand-new instruction set that I designed! The only language that it understands
is the low-level opcodes that map to each instruction. This makes it difficult
to program anything that's non-trivial without making a mistake.

So I can now appreciate why we need assemblers (and compilers for that matter).
To continue my journey up the stack, I've built an extremely simple assembler.
And of course I had to give it a great, snappy name. Meet [jasm](jasm.py), i.e.
John's assembler.

## How to use it?

Make sure you've got a modern version of python installed and clone the repo. You can run the program as simply as:

```bash
python jasm.py <file>
```

Or, a slightly less verbose way:

```bash
./jasm.py <file>
```

To see it in action, try it with one of the [example pograms](./example_programs/)

```bash
./jasm.py example_programs/add_forever
ADDRESS  INSTRUCTION  ASSEMBLY
0000     0101 0000    LDI 0
0001     0010 1111    ADD 15
0010     1110 0000    OUT
0011     0110 0010    JMP 1
```
