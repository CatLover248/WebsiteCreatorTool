#Python Version of WebsiteCreatorTool is Maintained by FatyCaty/Yusuf

#Script current: Does not work

#MIT License
#Copyright (c) 2022 Yusuf
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from tkinter import *


def GUI():
    root = Tk()

    root.geometry("500x500")
    root.title("WebsiteCreatorTool-Python GUI Edition | by FatyCaty/Yusuf")

    logo = Label(root, text="WebsiteCreatorTool Python")
    logo.pack()

    
    hF = Text()


    root.mainloop()

def webGenerator():
    html_file = open(f"{html_file_name}.html", "w")
    css_file = open(f"{css_file_name}.css", "w")

    html_file.write(f"<html>\n<head>\n<title>{html_file_title}</title>\n<link rel=\"stylesheet\" href=\"{css_file_name}.css\">\n</head>\n<body>\n<div id=\"header\">\n<h1>{html_file_header}</h1>\n</div>\n<div id=\"text\">\n<p>{html_file_text}<p>\n</div>\n</body>\n<html>")
    css_file.write("#header{\n	color: " + css_file_header + ";\n}")
    css_file.write("\n#text{\n	color: " + css_file_text + ";\n}")

    css_file.close()
    html_file.close()


GUI()
