"""
    Parses Markdown text and returns html elements
"""


def get_tags(tag):
    """
    """
    open_tag = "<{}>".format(tag)
    close_tag = "</{}>".format(tag)

    return open_tag, close_tag

def headings(line=""):
    """
        headings - generate html headings from md headings

        Arguments
            text: markdown text to parse
    """
    import re

    if line == "":
        return None

    line.lstrip(' ')

    h_tags = {
        0: None,
        1: "h1", 2: "h2", 3: "h3",
        4: "h4", 5: "h5", 6: "h6"
    }

    result = re.match(r"(^#+) (.+$)", line)
    if result is None:
        return None

    groups = result.groups()
    h_level = len(groups[0])
    text = groups[1]
    
    open_tag, close_tag = get_tags(h_tags[h_level])
    html = "{}{}{}".format(
        open_tag, text, close_tag
    )

    return(html)


def ulist(lines):
    """
    """
    import re

    list_content = []
    for line in lines:
        line.lstrip()
        result = re.match(r"(^- )(.*)", line)
        if result is not None:
            item = result.groups()[1]
            list_content.append(item)
        else:
            list_content.append(None)

    for index, item in enumerate(list_content):
        if list_content[index] is not None:
            list_content[index] = "\t<li>{}</li>".format(item)
        else:
            list_content[index] = lines[index]

    index = [idx for idx, s in enumerate(list_content) if '<li>' in s][0]
    list_content.insert(index, "<ul>")
    list_content.append("</ul>")
    html = list_content

    return html


def olist(lines):
    """
    """
    import re

    list_content = []
    for line in lines:
        line.lstrip()
        result = re.match(r"(^\* )(.*)", line)
        if result is not None:
            item = result.groups()[1]
            list_content.append(item)
        else:
            list_content.append(None)

    for index, item in enumerate(list_content):
        if list_content[index] is not None:
            list_content[index] = "\t<li>{}</li>".format(item)
        else:
            list_content[index] = lines[index]

    index = [idx for idx, s in enumerate(list_content) if '<li>' in s][0]
    list_content.insert(index, "<ol>")
    list_content.append("</ol>")
    html = list_content

    return html

def parse(text=""):
    """
        parse - main parse function

        Arguments:
            text: markdown text to parse
    """
    import re

    html_text = ""
    lines = text.split('\n')

    sections = []
    html_list = []
    while len(lines) != 0:
        end = lines.index('')
        sections.append(lines[0:end])
        del lines[:end + 1]

    for section in sections:

        # Change Heading
        for index, line in enumerate(section):
            html = headings(line) 
            if html is not None:
                section[index] = html

        # Change unordered lists
        is_ulist = False
        for line in section:
            line.lstrip()
            pattern = '(^\- )(.*)'
            result = re.search(pattern, line)
            if result is not None:
                is_ulist = True
                break

        if is_ulist:
            html = ulist(section)
            section = html

        # Change ordered lists
        is_olist = False
        for line in section:
            line.lstrip()
            pattern = '(^\* )(.*)'
            result = re.search(pattern, line)
            if result is not None:
                is_olist = True
                break

        if is_olist:
            html = olist(section)
            section = html

        # Find normal text and add <br/>
        for index, line in enumerate(section):
            line.lstrip()
            if line[0] not in ['<', '\t']:
                html = '<p>\n\t{}\n</p>'.format(line)
                section[index] = html

        for index, line in enumerate(section):
            try:
                next_line = section[index + 1]
            except:
                continue
            next_tag = next_line[1]
            cur_tag = line[-2]

            if next_tag == cur_tag:
                section[index] = line[:-5]
                section[index + 1] = section[index + 1][4:]
                section.insert(index + 1, "\t\t<br />")

        # bold and emphasis normal text
        for index, line in enumerate(section):
            match = re.search('\*\*.+\*\*', line)
            if match != None:
                result = re.sub(r'(\*\*)(.+)(\*\*)', r'<b>\2</b>', line)
                section[index] = result

        for index, line in enumerate(section):
            match = re.search('__.+__', line)
            if match != None:
                result = re.sub(r'(__)(.+)(__)', r'<em>\2</em>', line)
                section[index] = result
                continue

        html_list.append(section)

    return html_list
