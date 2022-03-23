
from .html_tags import *

def autoComplete(s):



    kod_satiri = list(s.strip().split("\n"))

    selfClosedTags = ["area", "base", "br", \
                      "col", "embed", "hr", "img", \
                      "input", "link", "meta", "param", \
                      "source", "track", "wbr"]

    n = len(kod_satiri)
    stack = []
    for i in range(n): #12
        j = 0
        line = kod_satiri[i]
        while j < len(kod_satiri[i]): # 16
            if j + 1 < len(line) and line[j] == "<" and line[j + 1] == "/":
                tag = []
                j += 2
                while j < len(line) and "a" <= line[j] <= "z":
                    tag.append(line[j])
                    j += 1
                print(" ")
                print("ben j: ", j)
                while j < len(line) and line[j] != ">":
                    j += 1

                print("ust ben stack ", stack)
                print("ust ben tag ", tag)
                if stack[-1] != tag:
                    tag = stack[-1]

                    return "</" + "".join(tag) + ">"
                print(stack.pop())

                if stack == [] and tag == True:
                    return tag





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



# buls = autoComplete(bul)
# print(f"Bu {buls} tag'i yazmayi unuttunuz.")







# say = 0
#     bak = s.split()
#     for i in bak:
#         if i == sani:
#             say += 1
#         if say == 0:
#             print("This tag is not in the Html_File")
#         else:
#             return say
# sani = input("Hangi tag'i saymak istersiniz? ")