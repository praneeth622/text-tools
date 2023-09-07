from django.http import HttpResponse
import random
from django.template import loader
from django.shortcuts import render



def link(request):
    
    return render(request,'index.html')

def analyze(request):
    text1 =request.POST.get('text','default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    charcount =request.POST.get('charcount','off')
    # Remove Punctuations
    if removepunc == 'on':
        punctuations = '''!()-[]{;:'"\,<>./?@}#$%^&*_~'''
        analized =''
        for char in text1:
            if char not in punctuations:
                analized = analized + char
    
        text1 = analized
    # change to fullcaps
    if fullcaps == 'on':
        # text2 = request.GET.get('text','default')
        analized =''
        for char in text1:
            analized = analized+char.upper()
        text1 = analized
    #new line remover
    if(newlineremover == 'on'):
        analized = ''
        for char in text1:
            if char !='\n' and char !='\r':
                analized = analized+char
        text1 = analized
    # char count
    if(charcount == 'on'):
        index = len(text1)
        newtext = {'after':index,'purpose':'Total no of char in text is '}

        return render(request,'analyze.html',newtext)
    if(removepunc != "on" and newlineremover!="on" and  fullcaps!="on"):
        return HttpResponse("please select any operation and try again")
    
    newtext = {'after':text1,'purpose':'New line removed'}
    return render(request,'analyze.html',newtext)
