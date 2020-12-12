#!/usr/bin/python3

"""
    Markdown to HTML script
"""

if __name__ == "__main__":
    from sys import argv
    from file_handler import get_file_names, read_md, write_html
    from parser import parse

    # Remove command-name from argv
    argv.pop(0)

    md_file, html_file = get_file_names(argv)
    md_text = read_md(md_file)

    html_text = ""
    sections = parse(md_text)
    for section in sections:
        snippet = '\n'.join(section)
        html_text += snippet + "\n"

    write_html(html_file, html_text)
