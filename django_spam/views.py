import random

from django.shortcuts import render, redirect

from django_spam import SPAM_URLS


def ten_hours(request):
    return redirect(random.choice(SPAM_URLS))
