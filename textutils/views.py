# I created this file - Abhishek

from django. http import HttpResponse

from django.shortcuts import render

def index (request):
    return render (request, 'index.html')

def analyze (request):
    djtext = request . POST . get ('text' , 'default')
    removepunc = request . POST . get ('removepunc', 'off')
    allcaps = request . POST . get ('allcaps', 'off')
    removenewline = request . POST . get ('removenewline', 'off')
    removeextraspace = request . POST . get ('removeextraspace', 'off')
    countcharacters = request . POST . get ('countcharacters', 'off')
    if removepunc == 'on' or allcaps == 'on' or removenewline == 'on'or removeextraspace == 'on'or countcharacters == 'on' :
        purpose = ''
        if removepunc == 'on':
            analyzed = ''
            add_purpose = '  |  Removed Punctuations'
            punctuations = '''.,?!:;-()"'}\{[]'''
            for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed + char
            djtext = analyzed
            purpose = purpose + add_purpose
        if allcaps == 'on':
            analyzed = ''
            add_purpose = '  |  Changed to All Caps'
            for char in djtext:
                analyzed = analyzed + char . upper ()
            djtext = analyzed
            purpose = purpose + add_purpose
        if removenewline == 'on':
            analyzed = ''
            add_purpose = '  |  Removed Lines'
            for char in djtext:
                if char != '\n' and char != '\r':
                    analyzed = analyzed + char
            djtext = analyzed
            purpose = purpose + add_purpose
        if removeextraspace == 'on':
            analyzed = ''
            add_purpose = '  |  Removed Space'
            for index, char in enumerate (djtext):
                if (index+1) != len (djtext):
                    if not (djtext [index] == ' ' and djtext [index + 1] == ' '):
                        analyzed = analyzed + char
            djtext = analyzed
            purpose = purpose + add_purpose
        if countcharacters == 'on':
            add_purpose = '  |  Counted Characters'
            analyzed = analyzed + '\n\n---- Number of characters in your text is: ' + str (len (djtext))
            purpose = purpose + add_purpose
    else:
        return HttpResponse ("Please select any of the operations")
    
    params = {'purpose': purpose, 'analyzed_text': analyzed}
    return render (request , 'analyze.html', params)

def aboutUs (request):
    return render (request, 'about.html')

def contactUs (request):
    return render (request, 'contact.html')