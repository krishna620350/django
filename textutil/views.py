# i have created this file
from django.http import HttpResponse # only write html code in side
from django.shortcuts import render  # adding templates in webpages


# only for some practice
# def index(request):
#     return HttpResponse("<h1>hello krishna</h1>")
#
#
# def about(request):
#     return HttpResponse("hello manish")


def index(request):
    # return HttpResponse("<h1>home</h1><a href = 'http://127.0.0.1:8000/removepunk'>removepunk</a>")
    return render(request, "index.html")


# def removepunk(request):
#     # print(request.GET.get('text', 'default'))
#     djtext = request.GET.get('text', 'default')
#     # analyse text
#     return HttpResponse(djtext)
def analyses(request):
    # print(request.GET.get('text', 'default'))
    # djtext = request.GET.get('text', 'default')
    # removepunk = request.GET.get('removepunk', 'off')
    # fullcaps = request.GET.get('fullcaps', 'off')
    # newline = request.GET.get('newline', 'off')
    # space = request.GET.get('space', 'off')
    # get the value using post method
    djtext = request.POST.get('text', 'default')
    removepunk = request.POST.get('removepunk', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newline = request.POST.get('newline', 'off')
    space = request.POST.get('space', 'off')
    # analyse text
    # return HttpResponse(djtext)
    # analysed = djtext
    if removepunk == "on":
        punchuationlist  = """{},!,\,/,;,:,@,$,<,#,%"""
        analysed = ""
        for char in djtext:
            if char not in punchuationlist:
                analysed = analysed + char
        parms = {
            'purpose': 'remove puncuation',
            'analyser_text': analysed
        }
        return render(request, "analyse.html", parms)
    elif fullcaps == 'on':
        analysed =""
        for char in djtext:
            analysed += char.upper()
        parms = {
            'purpose': 'change to uppercase',
            'analyser_text': analysed
        }
        return render(request, "analyse.html", parms)
    elif newline == 'on':
        analysed =""
        for char in djtext:
            if char!="\n":
                analysed += char.upper()
        parms = {
            'purpose': 'new lines',
            'analyser_text': analysed
        }
        return render(request, "analyse.html", parms)
    elif space == 'on':
        analysed =""
        for index, char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analysed += char.upper()
        parms = {
            'purpose': 'space remover',
            'analyser_text': analysed
        }
        return render(request, "analyse.html", parms)
    else:
        return HttpResponse("error")

# def capataLize(request):
#     return HttpResponse("<h3>capatalize</h3>")
#
#
# def newlineRemover(request):
#     return HttpResponse("dsgvsdgbfdb")
#
#
# def spaceRemover(request):
#     return HttpResponse("gdsgsdhbfj")
#
#
# def characterCount(request):
#     return HttpResponse("sdgvfsdhdgbh")
