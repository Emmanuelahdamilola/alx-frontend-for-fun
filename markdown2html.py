#!/usr/bin/python3
"""
Converts a Markdown file to an HTML file.

Usage: ./markdown2html.py README.md README.html
"""

import sys
import os.path


def main():
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py <input_file.md> <output_file.html>\n")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    # Conversion logic (not implemented in this example)

    sys.exit(0)


if __name__ == "__main__":
    main()
