import random

from django.shortcuts import render, redirect

from dj_spam import SPAM_URLS


def tickle_me_pink(request):
    return redirect(random.choice(SPAM_URLS))
