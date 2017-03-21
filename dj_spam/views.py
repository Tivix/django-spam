import random

from django.shortcuts import render, redirect

from django.conf import settings


def tickle_me_pink(request):
    return redirect(random.choice(settings.SPAM_URLS))
