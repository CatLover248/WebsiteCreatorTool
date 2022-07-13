package me.fatycaty;


/*

MIT License

Copyright (c) 2022 Yusuf

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


 */

import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static String name = "WebsiteCreatorV2";
    public static String version = "0.1-beta2";

    public static void main(String[] args){

        Scanner scan = new Scanner(System.in);

        System.out.println("Welcome to " + name + "\nMade By github.com/FatyCaty/");

        //html input
        System.out.print("What do you want the generated html file name to be?: ");
        String htmlFileName = scan.next();

        System.out.print("What do you want the title of the website to be?: ");
        String htmlTitle = scan.next();

        System.out.print("What do you want the header of the website to be?: ");
        String htmlHeader = scan.next();

        System.out.print("What do you want the text of the website to be?: ");
        String htmlText = scan.next();

        //css input
        System.out.print("What do you want the generated css file name to be?: ");
        String cssFileName = scan.next();

        System.out.print("What do you want the header color of the website to be?: ");
        String cssHeaderColor = scan.next();

        System.out.print("What do you want the text color of the website to be?: ");
        String cssTextColor = scan.next();
        try {
            //html
            FileWriter a = new FileWriter(htmlFileName + ".html");
            a.write("<html>\n<head>\n<link rel=\"stylesheet\" href=\"" + cssFileName + ".css\">\n<title>" + htmlTitle + "</title>\n</head>\n<body>\n<div id=\"dH\">\n<h1>" + htmlHeader + "</h1>\n<div>\n<div id=\"dT\">\n<p>" + htmlText + "<p>\n</div>\n</body>\n</html>");
            a.close();
            System.out.println(htmlFileName + ".html Generated!");
            //css
            FileWriter b = new FileWriter(cssFileName+ ".css");
            b.write("#dH{\n color: " + cssHeaderColor.trim() + ";\n}\n#dT{\n color: " + cssTextColor.trim() + ";\n}");
            b.close();
            System.out.println(cssFileName + ".css Generated!");
        } catch(IOException e){
            System.out.println("Exception: \n" + e);
        }
    }
}
