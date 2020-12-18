"""
    Handles opening, closing, reading, writing, etc.
    files
"""


def get_file_names(args):
    """
        get_file_names - Validate files / Print usage and exit

        Arguments:
            args - argument list run with the script
    """
    from os import path
    from utility import err_print

    usage = "Usage: ./markdown2html.py README.md README.html"
    if len(args) < 2:
        err_print(usage)
        exit(1)

    md_file = args[0]
    html_file = args[1]

    if path.exists(md_file) is False:
        err_print("Missing", md_file)
        exit(1)

    return md_file, html_file


def read_md(filename):
    """
        read_md - reads/returns text of an md file
    """

    with open(filename, 'r') as f:
        text = f.read()

    return text


def write_html(html_file, html_text):
    """
    """

    with open(html_file, 'w') as f:
        f.write(html_text[:-1])
