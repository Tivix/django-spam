import random

from django.shortcuts import render, redirect

from django.conf import settings


def tickle_me_pink(request):
    return redirect(settings.SPAM_URLS[random.randint(0, len(settings.SPAM_URLS)-1)])
