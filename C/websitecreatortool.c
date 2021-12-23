#Code By ComputeriFan431


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
struct website
{
    char* fileName;
    char* title;
    char* header;
    char* text;
};

int main()
{
    printf("Welcome to Website Creator Console Edition Version 1.0 \n");
    
    printf("Press ENTER to begin\n");
    
    scanf("%s", "");
    
    struct website html;
    html.fileName = "";
    printf("What do you want your HTML file to be named?: \n");

    scanf("%[^\n]s", html.fileName);
    
    printf("What do you want to be the title of the website?: \n");
    
    scanf("%[^\n]s", html.title);

    printf("What do you want the header of the website to be?: \n");
    
    scanf("%[^\n]s", html.header);

    printf("What do you want the text of your website to be?: \n");
    
    scanf("%[^\n]s", html.text);
    struct website css;

    printf("What do you want your CSS file to be named?: \n");    
    scanf("%[^\n]s", css.fileName);

    printf("What do you want the header color of the website to be?(example - #5F9EA0): \n");
    scanf("%[^\n]s", css.header);

    printf("What do you want the text color of your website to be?(example - #5F9EA0): \n");
    scanf("%s", css.text);

    FILE* websiteFilePointer;
    FILE* cssFilePointer;
    websiteFilePointer = fopen(strcat(html.fileName, ".html"), "w");
    cssFilePointer = fopen(strcat(css.fileName, ".css"), "w");

    char* htmlScript = "<html>\n<head>\n<title>";
    strcat(htmlScript, html.title);
    strcat(htmlScript, "</title>\n<link rel=\"stylesheet\" href=\"");
    strcat(htmlScript, css.fileName);
    strcat(htmlScript, ".css\">\n</head>\n<body>\n<div id=\"header\">\n<h1>");
    strcat(htmlScript, html.header);
    strcat(htmlScript, " </h1> \n</div>\n <div id = \"text\">\n<p>");
    strcat(htmlScript, html.text);
    strcat(htmlScript, "<p>\n</div>\n</body>\n<html>");

    fprintf(websiteFilePointer, "%s", htmlScript);
    fclose(websiteFilePointer);
    free(websiteFilePointer);

    char* cssScript = "#header\n{\n    color: ";
    strcat(cssScript, css.header);
    strcat(cssScript, ";\n}\n #text\n{\n   color: ");    
    strcat(cssScript, css.text);
    strcat(cssScript, "}");
    fprintf(cssFilePointer, "%s", cssScript);

    fclose(cssFilePointer);
    free(websiteFilePointer);

    return 0;
}
//int main()
//{
//    printf("Welcome to Website Creator Console Edition Version 1.0 \n");
//    
//    printf("Press ENTER to begin\n");
//    
//    scanf("%s", "");  
//    
//    printf("What do you want your HTML file to be named?: \n");
//    char* html_fileName;
//    scanf("%[^\n]s", html_fileName);
//    
//
//    printf("What do you want to be the title of the website?: \n");
//    char* html_title;
//    scanf("%[^\n]s", html_title);
//
//    printf("What do you want the header of the website to be?: \n");
//    char* html_header;
//    scanf("%[^\n]s", html_header);
//
//    printf("What do you want the text of your website to be?: \n");
//    char* html_text;
//    scanf("%[^\n]s", html_text);
//
//    printf("What do you want your CSS file to be named?: \n");    
//    char* css_fileName;
//    scanf("%[^\n]s", css_fileName);
//
//    printf("What do you want the header color of the website to be?(example - #5F9EA0): \n");
//    char* css_header;
//    scanf("%[^\n]s", css_header);
//
//    printf("What do you want the text color of your website to be?(example - #5F9EA0): \n");
//    char* css_text;
//    scanf("%s", css_text);
//
//    FILE* websiteFilePointer;
//    FILE* cssFilePointer;
//    websiteFilePointer = fopen(strcat(html_fileName, ".html"), "w");
//    cssFilePointer = fopen(strcat(css_fileName, ".css"), "w");
//
//    char* htmlScript = "<html>\n<head>\n<title>";
//    strcat(htmlScript, html_title);
//    strcat(htmlScript, "</title>\n<link rel=\"stylesheet\" href=\"");
//    strcat(htmlScript, css_fileName);
//    strcat(htmlScript, ".css\">\n</head>\n<body>\n<div id=\"header\">\n<h1>");
//    strcat(htmlScript, html_header);
//    strcat(htmlScript, " </h1> \n</div>\n <div id = \"text\">\n<p>");
//    strcat(htmlScript, html_text);
//    strcat(htmlScript, "<p>\n</div>\n</body>\n<html>");
//
//    fprintf(websiteFilePointer, "%s", htmlScript);
//    fclose(websiteFilePointer);
//    free(websiteFilePointer);
//
//    char* cssScript = "#header\n{\n    color: ";
//    strcat(cssScript, css_header);
//    strcat(cssScript, ";\n}\n #text\n{\n   color: ");    
//    strcat(cssScript, css_text);
//    strcat(cssScript, "}");
//    fprintf(cssFilePointer, "%s", cssScript);
//
//    fclose(cssFilePointer);
//    free(websiteFilePointer);
//
//    return 0;
//}
