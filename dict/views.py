from django.shortcuts import render
from PyDictionary import PyDictionary

def index(request):
    return render(request,'index.html')

def word(request):
    if request.method == 'POST':
        word = request.POST.get('search', None)
        if word:
            dictionary = PyDictionary()
            meaning = dictionary.meaning(word)
            if meaning:
                # Check if the 'Noun' key exists in the meaning dictionary
                noun_meaning = meaning.get('Noun', None)
                if noun_meaning:
                    # Get the first meaning for the 'Noun' key
                    noun_meaning_first = noun_meaning[0]
                else:
                    noun_meaning_first = "Noun meaning not available"
                return render(request, 'word.html', {'meaning': noun_meaning_first})
            else:
                return render(request, 'word.html', {'meaning': "Meaning not found"})
        else:
            return render(request, 'word.html', {'meaning': "Please provide a word to search"})
    return render(request, 'word.html')



