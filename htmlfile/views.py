from django.shortcuts import render
import json
from django.http import JsonResponse
from collections import Counter

from .tags import tags

def indexView(request):
    keyword = request.GET.get("keyword")
    acik_tag = acik_tags()
    context = {
        "acik_tag": acik_tag,
    }
    return render(request, 'index.html', context)




def acik_tags():

    taglar = list(tags.strip().split("\n"))

    addopentags = []
    add_open = 0

    addclosetags = []
    add_close = 0

    n = len(taglar)
    print(n)


    for i in range(n):
        print()
        if taglar[i].strip().startswith("<") and not taglar[i].strip().startswith("</")\
                and taglar[i].strip().endswith(">") and len(taglar[i]) <= 15:
            addopentags.append(taglar[i].strip())
            add_open += 1

    for i in range(n):
        if taglar[i].strip().startswith("</") and taglar[i].strip().endswith(">"):
            addclosetags.append(taglar[i].strip())
            add_close += 1



    html_open_tags = Counter(addopentags)
    print(addopentags)
    for x, y in html_open_tags.items():
        print(x, y)

    print(addclosetags)
    html_close_tags = Counter(addclosetags)
    for x, y in html_close_tags.items():
        print(x, y)

    return html_open_tags









# def kapali_tags():
#     taglar = list(tags.strip().split("\n"))
#
#     addclosetags = []
#     add_close = 0
#
#     n = len(taglar)
#
#     for i in range(n):
#         if taglar[i].strip().startswith("</") and taglar[i].strip().endswith(">"):
#             addclosetags.append(taglar[i].strip())
#             add_close += 1
#
#     html_close_tags = Counter(addclosetags)
#
#     for x, y in html_close_tags.items():
#         print(x, y)
#
#     return html_close_tags

























def tag_goster():
    kelimeler = list(tags.strip().split("\n"))
    stack = []
    uzunluk = len(kelimeler)
    j = 0
    for i in range(uzunluk):
        j = j + i + 1
        while j < uzunluk - 1:
            if kelimeler[i].strip() == kelimeler[j].strip():
                # if kelimeler[i] != stack[i]:
                stack.append(kelimeler[i].strip())
            j += 1
        if j == uzunluk - 1:
            j = 0
    return stack


def jsonView(request):
    keyword = request.GET.get("ariyorum")

    jsons = {
        "input": "Arafat",
        "text": "Emin",
        "number": 391248,
        "checkbox": True,
        "tel": "5380514510",
        "email": 'arafatemin34@gmail.com',
        "password": "Password",
        "date": "03/26/2022",
        "search": "search",
        "button": "button",
        "textarea": "What is Lorem Ipsum?Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
        "select":
            {"Html": "Html", "Css": "Css", "Javascript": "Javascript", "Php": "Php", "SQL": "SQL"},
    }
    key = ""
    for i, j in jsons.items():
        if i == keyword:
            key = j

    data = {
        "input": jsons.get('input'),
        "text": jsons.get('text'),
        "number": jsons.get('number'),
        "textarea": jsons.get('textarea'),

        "search": jsons.get('search'),
        "button": jsons.get('button'),
        "checkbox": jsons.get('checkbox'),
        "select": jsons.get('select'),

        "tel": jsons.get('tel'),
        "email": jsons.get('email'),
        "password": jsons.get('password'),
        "date": jsons.get('date'),

    }

    context = {
        "data": data,
        "jsons": jsons,
        "keyword": keyword,
        "key": key
    }

    return render(request, 'json.html', context)
