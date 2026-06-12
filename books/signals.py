from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import connection
from .models import Book

import threading
import time

signal_thread_id = None
signal_transaction = None

@receiver(post_save, sender=Book)
def book_saved(sender, instance, **kwargs):
    global signal_thread_id
    global signal_transaction

    signal_thread_id = threading.get_ident()
    signal_transaction = connection.in_atomic_block

    if instance.title == "Sync Test":
        time.sleep(3)

