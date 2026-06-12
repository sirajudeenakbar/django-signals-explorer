import time
def run_sync_test():
    start = time.time()

    time.sleep(10)

    end = time.time()

    return round(end - start, 2)