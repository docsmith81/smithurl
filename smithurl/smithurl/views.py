from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import UrlForm
from .shorten import shorten_url
from .database import collision_detector
from .database import insert_entry
from .database import url_lookup

def get_url(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            long_url = request.POST.get("long_url", "")
            if "http" not in long_url:
                long_url = "http://" + long_url
            short_url = shorten_url()
            while collision_detector(short_url) >= 1:
                short_url = shorten_url()
            insert_entry(long_url,short_url)
            return HttpResponse("Your shortened URL: {}".format(short_url))

    else:
        form = UrlForm()

    return render(request, 'get_url.html', {'form': form})

def redirect_url(request):
    long_url = url_lookup(request.build_absolute_uri())
    #return HttpResponse("{}".format(long_url))
    return HttpResponseRedirect(long_url)
