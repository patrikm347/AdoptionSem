from django.shortcuts import render, get_object_or_404
from .models import Dog, Breed
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

def home(request):
    dogs = Dog.objects.all()
    context = {
        'dogs': dogs
    }

    return render(request, 'adoption/home.html', context)

def detail(request, dog_id):
    dog = does_object_exist(dog_id)

    context = {
        'dog': dog
    }

    return render(request, 'adoption/detail.html', context)

def delete(request, dog_id):
    dog = does_object_exist(dog_id)

    Dog.objects.filter(pk=dog_id).first().delete()

    return render(request, 'adoption/delete.html', {})

def update(request, dog_id):
    dog = does_object_exist(dog_id)
    if request.method == 'POST':
        dog.breed = Breed.objects.filter(breedType=request.POST['breed']).first()
        dog.name = request.POST['name']
        dog.description = request.POST['description']
        dog.age = request.POST['age']
        dog.weight = request.POST['weight']
        dog.gender = request.POST['gender']
        dog.image = request.POST['image']
        dog.save()

        return HttpResponseRedirect(reverse('adoption:home'))
        

    breeds = Breed.objects.all()
    context = {
        'dog': dog,
        'breeds': breeds
    }

    return render(request, 'adoption/update.html', context)

def create(request):
    if request.method == 'POST':
        dog = Dog.objects.create(
            breed=Breed.objects.filter(breedType=request.POST['breed']).first(),
            name=request.POST['name'],
            description=request.POST['description'],
            age=request.POST['age'],
            weight=request.POST['weight'],
            gender=request.POST['gender'],
            image=request.POST['image']
        )
        dog.save()

        return HttpResponseRedirect(reverse('adoption:home'))

    breeds = Breed.objects.all()
    context = {
        'breeds': breeds
    }

    return render(request, 'adoption/create.html', context)

def does_object_exist(dog_id):
    try:
        dog = get_object_or_404(Dog, pk=dog_id)
    except Dog.DoesNotExist:
        raise Http404("Dog with this id doesn't exist.")

    return dog
