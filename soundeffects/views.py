from django.shortcuts import render
from django.http import HttpResponse

from .models import SoundEffect

# Create your views here.
def index(request):
    # latest_sounds = SoundEffect.objects.order_by('-sid')[:5]
    # context = {'latest_sounds': latest_sounds}
    return render(request, 'soundeffects/index.html')

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

def sound(request):
	sound = SoundEffect.objects.get(sid=request.GET.get('q','')).sound_file
	context = {'sound': sound}
	return render(request, 'soundeffects/sound.html', context)
	# return HttpResponse("You're looking at question " + request.GET.get('q', '') + sound)

def aboutus(request):
	return render(request, 'soundeffects/aboutindex.html')

def sounds(request):
	return render(request, 'soundeffects/sounds.html')

def contact(request):
	return render(request, 'soundeffects/contact.html')
