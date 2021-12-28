#Python Version of WebsiteCreatorTool is Maintained by FatyCaty/Yusuf

#Script current: Does not work

#MIT License
#Copyright (c) 2021 Yusuf
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from tkinter import *
import time

input_options = ["What do you want your HTML file to be named?: ", "What do you want to be the title of the website?: ", "What do you want the header of the website to be?: ", "What do you want the header of the website to be?:", "What do you want the text of your website to be?:", "What do you want your CSS file to be named?: ", "What do you want the header color of the website to be?(example - #5F9EA0): ", "What do you want the text color of your website to be?(example - #5F9EA0): "]


def GUI():
    pass

def cmd():
    inputs = []
    for i in input_options:
        inputs.append(input(i))


    #html_file_name = input("What do you want your HTML file to be named?: ")
    #html_file_title = input("What do you want to be the title of the website?: ")
    #html_file_header = input("What do you want the header of the website to be?: ")
    #html_file_text = input("What do you want the text of your website to be?: ")


    #css_file_name = input("What do you want your CSS file to be named?: ")
    #css_file_header = input("What do you want the header color of the website to be?(example - #5F9EA0): ")
    #css_file_text = input("What do you want the text color of your website to be?(example - #5F9EA0): ")

def webGenerator():
    html_file = open(f"{html_file_name}.html", "w")
    css_file = open(f"{css_file_name}.css", "w")



    html_file.write(f"<html>\n<head>\n<title>{html_file_title}</title>\n<link rel=\"stylesheet\" href=\"{css_file_name}.css\">\n</head>\n<body>\n<div id=\"header\">\n<h1>{html_file_header}</h1>\n</div>\n<div id=\"text\">\n<p>{html_file_text}<p>\n</div>\n</body>\n<html>")
    css_file.write("#header{\n	color: " + css_file_header + ";\n}")
    css_file.write("\n#text{\n	color: " + css_file_text + ";\n}")


    css_file.close()
    html_file.close()

    print("You Website Has Been Crated!")

    input("Press Enter To Close This Window")



opt = input("Welcome to Website Creator Tool\nWould you like to use the Command Line Creator or\n the GUI Creator?[CMD = CommandLine Creator| GUI = GUI Creator]: ")

if opt.upper() == "CMD":
    cmd()
elif opt.upper() == "GUI":
    GUI()
else:
    print("[Error - Wrong Value Inputted]\nQuitting...")
    time.sleep(4)
    quit()
