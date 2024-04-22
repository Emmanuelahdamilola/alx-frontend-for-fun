#!/usr/bin/python3
"""
Converts a Markdown file to an HTML file.

Usage: ./markdown2html.py <input_file.md> <output_file.html>
"""


import sys
import os.path
import re


def convert_heading(match):
    """
    Converts Markdown heading syntax to HTML.
    Example: "# Heading level 1" -> "<h1>Heading level 1</h1>"
    """
    heading_level = len(match.group(1))
    heading_text = match.group(2)
    return f"<h{heading_level}>{heading_text}</h{heading_level}>"

def convert_unordered_list(match):
    """
    Converts Markdown unordered list syntax to HTML.
    Example: "- Hello" -> "<li>Hello</li>"
    """
    list_item = match.group(1)
    return f"<li>{list_item}</li>"

def main():
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py <input_file.md> <output_file.html>\n")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    # Read the input Markdown file
    with open(input_file, "r") as md_file:
        markdown_content = md_file.read()

    # Convert Markdown headings to HTML
    html_content = re.sub(r"^(#{1,6})\s+(.+)$", convert_heading, markdown_content, flags=re.MULTILINE)

    # Convert Markdown unordered lists to HTML
    html_content = re.sub(r"^\s*-\s+(.+)$", convert_unordered_list, html_content, flags=re.MULTILINE)

    # Write the HTML content to the output file
    with open(output_file, "w") as html_file:
        html_file.write(html_content)

    sys.exit(0)



if __name__ == "__main__":
    main()
