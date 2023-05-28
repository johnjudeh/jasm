INSTRUCTION_NOP = "nop"
INSTRUCTION_LDA = "lda"
INSTRUCTION_ADD = "add"
INSTRUCTION_SUB = "sub"
INSTRUCTION_STA = "sta"
INSTRUCTION_LDI = "ldi"
INSTRUCTION_JMP = "jmp"
INSTRUCTION_JC = "jc"
INSTRUCTION_JZ = "jz"
INSTRUCTION_OUT = "out"
INSTRUCTION_HLT = "hlt"

OPCODES = {
    INSTRUCTION_NOP: 0,
    INSTRUCTION_LDA: 1,
    INSTRUCTION_ADD: 2,
    INSTRUCTION_SUB: 3,
    INSTRUCTION_STA: 4,
    INSTRUCTION_LDI: 5,
    INSTRUCTION_JMP: 6,
    INSTRUCTION_JC: 7,
    INSTRUCTION_JZ: 8,
    # ...
    INSTRUCTION_OUT: 14,
    INSTRUCTION_HLT: 15,
}

INSTRUCTIONS = set(OPCODES.keys())
PSEUDO_INSTRUCTION_DATA = "dta"

ASSEMBLED_LINE_TYPE = "type"
ASSEMBLED_LINE_TYPE_DATA = "data"
ASSEMBLED_LINE_TYPE_INSTRUCTION = "instruction"
ASSEMBLED_LINE_ADDRESS = "address"
ASSEMBLED_LINE_VALUE = "value"
ASSEMBLED_LINE_OPCODE = "opcode"
ASSEMBLED_LINE_OPERAND = "operand"
ASSEMBLED_LINE_INSTRUCTION_TEXT = "instruction_text"
