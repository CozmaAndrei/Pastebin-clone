from django.shortcuts import render, redirect
from .models import Text
from .forms import TextForm

def home(request):
    '''Aceasta functie face un request de tip POST, se verifica daca datele sunt valide, se salveaza in baza de date si se face redirect catre pagina home.html,
        ,daca nu este un request de tip POST se afiseaza formularul si lista de text'''
    if request.method == 'POST': 
        forms = TextForm(request.POST or None)
        if forms.is_valid(): 
            forms.save() 
            return redirect('home')    
        forms = TextForm()
        lists = Text.objects.all() 
        context = {'form': forms,'lists': lists}
        return render(request, 'htmlpages/home.html', context)
    else: 
        forms = TextForm()
        lists = Text.objects.all()
        context = {'form': forms,'lists': lists}
        return render(request, 'htmlpages/home.html', context)

def full_text(request, id):
    '''Aceasta functie face un request de tip GET, se cauta in baza de date textul cu id-ul respectiv si se afiseaza in pagina text.html'''
    text = Text.objects.get(pk=id)
    context = {'text': text}
    return render(request, 'htmlpages/text.html', context)