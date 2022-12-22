#!/usr/bin/env python
from constants import OPCODES, INSTRUCTIONS
from cli import create_cli


def assemble(file_contents: str) -> None:
    lines = file_contents.splitlines()
    assembled_lines = []
    for line in lines:
        line = line.split()
        if len(line) == 0:
            continue

        line_iterator = iter(line)
        assembled = []

        instruction = next(line_iterator).lower()
        if not instruction in INSTRUCTIONS:
            raise ValueError(f"Invalid instruction specified: {instruction}")
        assembled.append(OPCODES[instruction])

        for operand in line_iterator:
            if not operand.isnumeric():
                raise ValueError(f"Non numberic operand specified: {operand}")
            assembled.append(int(operand))

        # Add the assembly instruction to map to the assembled code in output
        assembled.append(" ".join(line))
        assembled_lines.append(assembled)

    print("ADDRESS  INSTRUCTION  ASSEMBLY")
    for address, assembled_line in enumerate(assembled_lines):
        instruction_text = assembled_line.pop()
        instruction = assembled_line[0]
        operand = assembled_line[1] if len(assembled_line) > 1 else 0

        print(
            f"{address:04b}     {instruction:04b} {operand:04b}    {instruction_text}"
        )


if __name__ == "__main__":
    cli = create_cli()
    args = cli.parse_args()
    assemble(args.file.read())
