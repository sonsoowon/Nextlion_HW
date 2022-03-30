from dataclasses import replace
from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    no_blank_text = text.replace(' ', '')
    
    words_count = len(text.split(' ')) if text != '' else 0
        

    return render(request, 'result.html', {
        'text' : text,
        'total_len': len(text), 'total_byte' : len(text.encode('utf-8')),
        'no_blank_len' : len(no_blank_text), 'no_blank_byte' : len(no_blank_text.encode('utf-8')),
        'words_count' : words_count})