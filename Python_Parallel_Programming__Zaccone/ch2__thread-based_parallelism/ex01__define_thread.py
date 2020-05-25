import threading


def func(i: int) -> None:
    print(f'function called by thread {i}\n')
    return None


threads = []
for i in range(5):
    thread = threading.Thread(target=func, args=(i,))
    threads.append(thread)
    thread.start()
    thread.join()
