# created
from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    var = {'title':"Text Util"}
    return render(request,'textUtil.html',var)

def about(request):
    return HttpResponse(" Hey This is About US\n<a href='/'>Back</a>")
def contactus(request):
    return HttpResponse("Hey This is Contact US\n<a href='/'>Back</a>")
def tu(request):
    text = request.POST.get('text','default')
    check = request.POST.get('rp','off')
    capita = request.POST.get('ca','off')
    upper = request.POST.get('uc','off')
    newLine = request.POST.get('nlr','off')
    extraSpace = request.POST.get('esr','off')
    charCounter = request.POST.get('cc','off')
    analyze=""
    if check == 'on':
        analyze = ""
        punchuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for cha in text:
            if cha not in punchuation:
                analyze=analyze+cha
        text = analyze
        print(analyze)
    if capita == 'on':
        analyze = ""
        spa = 0
        for index,key in enumerate(text):
            if index == spa:
                analyze = analyze + text[index].upper()
            elif text[index] == " " or text[index] == "\n":
                spa = (index+1)
                analyze = analyze + text[index]
            else:
                analyze = analyze + text[index]
        text = analyze
    if upper == 'on':
        analyze = ""
        analyze = text.upper()
        text = analyze
    if newLine == 'on':
        analyze = ""
        for char in text:
            if char != '\n' and char!='\r':
                analyze = analyze + char
                # print(analyze)
        text = analyze
    if extraSpace == 'on':
        analyze = ""
        for index, key in enumerate(text):
            if not (text[index] == " " and text[index + 1] == " "):
                analyze = analyze + text[index]
        text = analyze
    if charCounter == 'on':
        analyze = ""
        analyze = len(text)
        text = text + "          " + str(analyze)
    if check == "off" and capita == "off" and upper == "off" and newLine == "off" and extraSpace == "off" and charCounter == "off":
       return HttpResponse("Please!Enter Any Operation")
    params = {'title': 'Analyze', 'analyze': text}
    return render(request, 'textUtilResult.html', params)

