from argparse import ArgumentParser, FileType


def create_cli() -> ArgumentParser:
    parser = ArgumentParser(
        prog="jasm",
        description="Reads assembly code written for John's 8-bit computer and prints out the program to input",
    )
    parser.add_argument("file", type=FileType())
    return parser
