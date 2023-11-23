from django.shortcuts import render
from .cat import Cat

# Create your views here.

cat = Cat()
def create_cat(request):
    print(request.POST.get('cat_name'))
    return render(request, 'main.html')

def cat_page(request):
    if request.method =='POST':
        cat.name = request.POST.get('cat_name')
        context = {
            'image': cat.cat_image(),
            'name': cat.name,
            'age': cat.age,
            'hunger': cat.hunger,
            'happiness': cat.happiness
        }
    return render(request, 'cat_page.html', context)

def cat_action(request):
    if request.method == 'POST':
        cat.action_choose(request.POST.get('action'))
        context = {
                    'image': cat.cat_image(),
                    'name': cat.name,
                    'age': cat.age,
                    'hunger': cat.hunger,
                    'happiness': cat.happiness
                }
    return render(request, 'cat_page.html', context)