from django.shortcuts import render

from .html_tags import *
#
# from .myCode import *


s = """
<! DOCTYPE>
    <html>
    <head>
    rahile
    meryem
    rahile
        <title>
            GeeksforGeeks
        </title>
    </head>
    <body>
        <button>
            
                    <button>
        
        </button>  
                    <body>
    </body>
    </html>
"""

def indexView(request):
    keyword = request.GET.get("keyword")
    ariyorum = sayiyorum(keyword)


    kapanmayan_tag = autoComplete(s)

    # for i in kapanmayan_tag:
    #     print(i)




    print(kapanmayan_tag)
    # print(ariyorum)



    context = {

        "kapanmayan_tag": kapanmayan_tag,
        "ariyorum": ariyorum,
        "keyword": keyword,

    }
    return render(request, 'index.html', context)




def autoComplete(s):
    linesOfCode = list(s.strip().split("\n"))
    selfClosedTags = ["area", "base", "br", \
                      "col", "embed", "hr", "img", \
                      "input", "link", "meta", "param", \
                      "source", "track", "wbr"]
    # privateCarecter = ["\"", ".", ",", "<", ">", "_", "-", "!"]

    n = len(linesOfCode)
    stack = []
    for i in range(n):
        j = 0
        line = linesOfCode[i]
        while j < len(linesOfCode[i]):

            if j + 1 < len(line) and line[j] == "<" and line[j + 1] == "/":
                tag = []
                j += 2

                while j < len(line) and "a" <= line[j] <= "z":
                    tag.append(line[j])
                    j += 1
                while j < len(line) and line[j] != ">":
                    j += 1
                if stack[-1] != tag:
                    tag.append("</" + "".join(stack[-1]) + ">")
                    return tag
                    # return "</" + "".join(tag) + ">"
                stack.pop()




            elif j + 1 < len(line) and line[j] == "<" and line[j] == "!":
                continue





            elif line[j] == "<":
                tag = []
                j += 1

                while j < len(line) and "a" <= line[j] <= "z":
                    tag.append(line[j])
                    j += 1

                while j < len(line) and line[j] != ">":
                    j += 1


                if "".join(tag) not in selfClosedTags:
                    stack.append(tag)
            j += 1

    if stack:
        tag = stack.pop()
        return "</" + "".join(tag) + ">"
    return -1




def sayiyorum(hangi_tag):
    bak = list(s.strip().split("\n"))
    say = 0
    n = len(bak)
    for i in range(n):
        if hangi_tag == bak[i].strip():
            say += 1
    return say





