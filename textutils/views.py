from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def analyze(request):

    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc1 = request.POST.get('removepunc1', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    nlr = request.POST.get('nlr', 'off')
    extraspace = request.POST.get('extraspace', 'off')
    charcount = request.POST.get('charcount', 'off')

    # analyzed = djtext
    # print(analyzed)

    if removepunc1 == "on":
        punctuations = ''' !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~ '''
        analyzed = ""

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()

        params = {'purpose': 'changed to UpperCase Character',
                  'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (nlr == "on"):
        analyzed = ""

        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed+char.upper()

        params = {'purpose': 'Removed NewLines',
                  'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (extraspace == "on"):
        analyzed = ""

        for char in djtext:
            if char != " ":
                analyzed = analyzed+char

        params = {'purpose': 'Removed Extra Space',
                  'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (charcount == "on"):
        count = 0

        for char in djtext:
            count = count+1

        params = {'purpose': 'No of characters in text',
                  'analyzed_text': count}
        #djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (charcount != "on" and extraspace != "on" and nlr != "on" and removepunc1 != "on" and fullcaps != "on"):
        return HttpResponse("<H1>Please select anyone option:</H1> ")

    return render(request, 'analyze.html', params)


def removepunc(request):
    return HttpResponse("remove punc")


def capitalisefirst(request):
    return HttpResponse("capitalize first")


def NewLineremove(request):
    return HttpResponse("capitalize first")


def spaceRemover(request):
    return HttpResponse("space remover")


def characterCounter(request):
    return HttpResponse("charcount ")
