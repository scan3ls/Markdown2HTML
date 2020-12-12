#!/usr/bin/python3

"""
    Markdown to HTML script
"""

if __name__ == "__main__":
    from sys import argv
    from file_handler import get_file_names

    argv.pop(0)
    md_file, html_file = get_file_names(argv)
