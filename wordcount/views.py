from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def result(request):
    text=request.GET['fulltext']
    words=text.split() #이거 자체가 리스트
    word_dictionary={} #빈사전 만들기

    for word in words: #words는 리스트 word는 반복문 변수
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            #add to dictionary
            word_dictionary[word]=1

    return render(request,'result.html', {'full':text, 'total': len(words), 'dictionary' : word_dictionary.items()})