from django.http import HttpResponse
from .models import Book
from django.db import transaction, connection
from django.shortcuts import render
from django.http import JsonResponse

import time
import threading


def home(request):
    return render(request, 'books/home.html')


def test1(request):

    duration = None

    return render(
        request,
        "books/test1.html",
        {
            "duration": duration
        }
    )

def test2(request):

    caller_thread = threading.get_ident()

    Book.objects.create(title="Thread Test")

    from .signals import signal_thread_id

    result = caller_thread == signal_thread_id

    return render(
        request,
        "books/test2.html",
        {
            "caller_thread": caller_thread,
            "signal_thread": signal_thread_id,
            "result":result,
        }
    )



def test3(request):

    with transaction.atomic():
        caller_transaction = connection.in_atomic_block

        Book.objects.create(title="Transaction Test")

        from .signals import signal_transaction
    result = caller_transaction == signal_transaction
    return render(
        request,
        "books/test3.html",
        {
            "caller_transaction": caller_transaction,
            "signal_transaction": signal_transaction,
            "result": result,
        }
    )
def run_test1(request):

    start = time.time()

    Book.objects.create(title="Sync Test")

    duration = round(time.time() - start, 2)

    return JsonResponse({
        "duration": duration
    })