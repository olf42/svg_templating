#!/usr/bin/env python3
"""
This tool is a prototype to demonstrate a svg templating workflow
using jinja2 templating language for the lightning talk at
Coding da Vinci Ost http://codingdavinci.de/events/ost

Author: Florian Rämisch <raemisch@ub.uni-leipzig.de>
Copyright: 2018, Universitaetsbibliothek Leipzig
License: GNU General Public License v3

"""
from os.path import join, abspath, dirname
from os import listdir
from base64 import b64encode
from jinja2 import Template

# CONSTANTS
BASE_DIR = join(dirname(abspath(__file__)))
TEMPLATE = join(BASE_DIR, "template.svg")
CONTENT_DIR = join(BASE_DIR, "img")
OUT_DIR = join(BASE_DIR, "output")

# FUNCTIONS
def read_template(template=TEMPLATE):
    """
    reads a svg template and returns it as jinja2 template
    :param template: Path to the template file
    :return:
    """
    with open(template, "r") as template_file:
        svg_template = template_file.readlines()
    return Template("".join(svg_template))

def read_content(content_filename):
    """
    Reads a pixel image (png oder jpg) and returns its base64 encoded representation.
    :param content: filename (with path) to the content file
    :return: base64 string of the file content
    """
    with open(content_filename, "rb") as content_file:
        content = content_file.readlines()
    c2 = b''
    for line in content:
        c2+= line
    # content = bytes("".join(str(content)).encode("utf-8"))
    return b64encode(c2)

def read_content_dir(content_dir=CONTENT_DIR):
    """
    Generator that reads contents of the given directory and returns
    its base64 representations.
    :param content_dir: path to the content directory
    :return: yield ...
    """
    for content_filename in listdir(content_dir):
        yield content_filename, read_content(join(content_dir, content_filename))

def main(out_dir=OUT_DIR):
    """
    Main Wrapper Function.
    :param out_dir: directory where the output is written to.
    :return:
    """
    svg_template = read_template()
    for content_filename, content in read_content_dir():
        out_filename = "".join(content_filename.split(".")[:-1])+".svg"
        with open(join(out_dir, out_filename), "w") as out_file:
            out_file.write(svg_template.render(headline=content_filename[18:22], image=content.decode("utf-8")))

if __name__ == "__main__":
    main()