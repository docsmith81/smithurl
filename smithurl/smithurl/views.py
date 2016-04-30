from django.shortcuts import render
from django.http import HttpResponse

from .forms import UrlForm
from .shorten import shorten_url
from .database import collision_detector
from .database import insert_entry

def get_url(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            long_url = request.POST.get("long_url", "")
            short_url = shorten_url()
            while collision_detector(short_url) >= 1:
                short_url = shorten_url()
            insert_entry(long_url,short_url)
            return HttpResponse("Your shortened URL: {}".format(short_url))

    else:
        form = UrlForm()

    return render(request, 'get_url.html', {'form': form})
