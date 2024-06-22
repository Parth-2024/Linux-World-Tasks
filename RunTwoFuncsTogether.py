from multiprocessing import Process

rocket = 0

def lwa():
    while True:
        print("aaaaa")

def lwb():
    while True:
        print("bbbb")

if __name__=='__main__':
    p1 = Process(target=lwa)
    p1.start()
    p2 = Process(target=lwb)
    p2.start()
    # p1.join()
    # p2.join()