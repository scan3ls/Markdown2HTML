"""
    Handles files
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

    return md_file, html_file
