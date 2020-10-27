from labelme.__main__ import main
import subprocess
import multiprocessing
import time


def test_process():
    p1 = multiprocessing.Process(target=f, args=('process1',))
    p1.start()
    for i in range(10):
        print(f'a {i}')
        time.sleep(3)


if __name__ == "__main__":
    main()
    # test_process()