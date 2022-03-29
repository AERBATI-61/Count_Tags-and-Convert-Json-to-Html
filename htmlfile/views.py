from django.shortcuts import render
import json
from django.http import JsonResponse

s = """
<html>
<html>
</b>

</html>
<p>
"""


def indexView(request):
    keyword = request.GET.get("keyword")
    ariyorum = sayiyorum()
    tag_gosteriyors = tag_goster()
    tag_gosteriyor = set(tag_gosteriyors)

    context = {
        "ariyorum": ariyorum,
        "keyword": keyword,
        "tag_gosteriyor": tag_gosteriyor,

    }
    return render(request, 'index.html', context)


def sayiyorum():
    taglar = list(s.strip().split("\n"))
    print(taglar)

    addopentags = []
    addclosetags = []
    add_open = 0
    add_close = 0

    stack = []
    n = len(taglar)
    print(n)
    j = 0
    for i in range(n):
        print(taglar[i])


        if taglar[i].strip().startswith("</") and taglar[i].strip().endswith(">"):
            addclosetags.append(taglar[i])
            add_close += 1





        if taglar[i].strip().startswith("<") and not taglar[i].strip().startswith("</"):
            addopentags.append(taglar[i])
            add_open += 1



        # j = j + i + 1
        # print(j)
        # while j < n - 1:
        #     if addclosetags[i].strip() == addclosetags[j].strip():
        #         # if kelimeler[i] != stack[i]:
        #         stack.append(addclosetags[i])
        #     j += 1
        # print(n-1)
        # print(j)
        # if j == n - 1:
        #     print(j)
        #     j = 0

    print(add_close, addclosetags)
    print(add_open, addopentags)
    # print(stack)

    return add_open













def tag_goster():
    kelimeler = list(s.strip().split("\n"))
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
