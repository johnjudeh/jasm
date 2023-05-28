#!/usr/bin/env python
from constants import (
    OPCODES,
    INSTRUCTIONS,
    PSEUDO_INSTRUCTION_DATA,
    ASSEMBLED_LINE_TYPE,
    ASSEMBLED_LINE_TYPE_DATA,
    ASSEMBLED_LINE_TYPE_INSTRUCTION,
    ASSEMBLED_LINE_ADDRESS,
    ASSEMBLED_LINE_VALUE,
    ASSEMBLED_LINE_OPCODE,
    ASSEMBLED_LINE_OPERAND,
    ASSEMBLED_LINE_INSTRUCTION_TEXT,
)
from cli import create_cli


def assemble(file_contents: str) -> None:
    lines = file_contents.splitlines()
    assembled_lines = []
    for line in lines:
        line = line.split()
        if len(line) == 0:
            continue

        line_iterator = iter(line)
        assembled_line = {}

        instruction = next(line_iterator).lower()

        if instruction == PSEUDO_INSTRUCTION_DATA:
            assembled_line[ASSEMBLED_LINE_TYPE] = ASSEMBLED_LINE_TYPE_DATA

            address = next(line_iterator)
            if not address.isdigit():
                raise ValueError(f"Non numeric address specified: {address}")
            assembled_line[ASSEMBLED_LINE_ADDRESS] = int(address)

            value = next(line_iterator)
            if not value.isdigit():
                raise ValueError(f"Non numeric value specified: {value}")
            assembled_line[ASSEMBLED_LINE_VALUE] = int(value)

        elif instruction in INSTRUCTIONS:
            assembled_line[ASSEMBLED_LINE_TYPE] = ASSEMBLED_LINE_TYPE_INSTRUCTION
            assembled_line[ASSEMBLED_LINE_OPCODE] = OPCODES[instruction]

            try:
                operand = next(line_iterator)
            except StopIteration:
                pass
            else:
                if not operand.isdigit():
                    raise ValueError(f"Non numberic operand specified: {operand}")
                assembled_line[ASSEMBLED_LINE_OPERAND] = int(operand)
        else:
            raise ValueError(f"Invalid instruction specified: {instruction}")

        assembled_line[ASSEMBLED_LINE_INSTRUCTION_TEXT] = " ".join(line)
        assembled_lines.append(assembled_line)

    print("ADDRESS  INSTRUCTION  ASSEMBLY")

    for l, line in enumerate(assembled_lines):
        if line[ASSEMBLED_LINE_TYPE] == ASSEMBLED_LINE_TYPE_DATA:
            address = line[ASSEMBLED_LINE_ADDRESS]
            instruction = f"{line[ASSEMBLED_LINE_VALUE]:08b}"
            instruction = f"{instruction[:4]} {instruction[4:]}"
        else:
            address = l
            instruction = f"{line[ASSEMBLED_LINE_OPCODE]:04b} {line.get(ASSEMBLED_LINE_OPERAND, 0):04b}"
        print(
            f"{address:04b}     {instruction}    {line[ASSEMBLED_LINE_INSTRUCTION_TEXT]}"
        )


if __name__ == "__main__":
    cli = create_cli()
    args = cli.parse_args()
    assemble(args.file.read())
