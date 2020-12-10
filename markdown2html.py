#!/usr/bin/python3

"""
    Markdown to HTML script
"""


def get_file_names(args):
    """
        get_file_names - Validate files / Print usage and exit

        Arguments:
            args - argument list run with the script
    """
    from os import path

    usage = "Usage: ./markdown2html.py README.md README.html"
    if len(args) < 2:
        err_print(usage)
        exit(1)

    md_file = args[0]
    html_file = args[1]

    if path.exists(md_file) is False:
        err_print("Missing", md_file)

    return md_file, html_file


def err_print(*args, **kwargs):
    """
        err_print - prints to stderr

        Arguments:
            args - same as print *args
            kwargs - same as print **kwargs
    """
    from sys import stderr
    print(*args, file=stderr, **kwargs)


def main(argv):
    """
        main - entry point; Convert .md files to .html files

        Arguments:
            argv - argument list given when running the script
    """

    md_file, html_file = get_file_names(argv)


if __name__ == "__main__":
    from sys import argv
    argv.pop(0)
    main(argv)
