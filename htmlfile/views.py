from django.shortcuts import render

from .html_tags import *

#
# from .myCode import *


s = """
<html>
<html>

<b>

</b>
</b>
<h1>
</h1>
<h1>

<body>
</body>
</body>

</html>

"""


def indexView(request):
    keyword = request.GET.get("keyword")
    ariyorum = sayiyorum(keyword)
    tag_gosteriyor = tag_goster()

    context = {
        "ariyorum": ariyorum,
        "keyword": keyword,
        "tag_gosteriyor": tag_gosteriyor
    }
    return render(request, 'index.html', context)


def sayiyorum(hangi_tag):
    bak = list(s.strip().split("\n"))
    say = 0
    n = len(bak)
    for i in range(n):
        if hangi_tag == bak[i].strip():
            say += 1
    return say


def tag_goster():
    kelimeler = list(s.strip().split("\n"))
    stack = []
    uzunluk = len(kelimeler)
    j = 0

    for i in range(uzunluk):
        j = j + i + 1
        while j < uzunluk - 1:
            if kelimeler[i].strip() == kelimeler[j].strip():
                stack.append(kelimeler[i].strip())
            j += 1
        if j == uzunluk - 1:
            j = 0

    return stack
