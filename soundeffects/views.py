from django.shortcuts import render
from django.http import HttpResponse

from .models import SoundEffect
from django.db.models import Q
import json

# Create your views here.
def index(request):
    # latest_sounds = SoundEffect.objects.order_by('-sid')[:5]
    # context = {'latest_sounds': latest_sounds}
    return render(request, 'soundeffects/index.html')

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

def sound(request):
	search = request.GET.get('q','')
	sound = SoundEffect.objects.filter(Q(sid=search) | Q(tags__icontains=search) | Q(category=search) )
	print type(sound)
	# print json.dumps(sound)
	context = {'sound': sound}
	return render(request, 'soundeffects/sound.html', context)
	# return HttpResponse("You're looking at question " + request.GET.get('q', '') + sound)

def aboutus(request):
	return render(request, 'soundeffects/aboutindex.html')

def sounds(request):
	return render(request, 'soundeffects/sounds.html')

def contact(request):
	return render(request, 'soundeffects/contact.html')
