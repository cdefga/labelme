from labelme.__main__ import main
import subprocess
import multiprocessing
import time

# subprocess.call(["./script.sh", "/home/cdefga/Projects/labelme/00ac73cfc372.dcm"])

def f(args):
    print(args)
    for i in range(10):
        print(i)
        time.sleep(5)


def test_process():
    p1 = multiprocessing.Process(target=f, args=('process1',))
    p1.start()
    # p2 = multiprocessing.Process(target)
    for i in range(10):
        print(f'a {i}')
        time.sleep(3)


if __name__ == "__main__":
    main()
    # test_process()