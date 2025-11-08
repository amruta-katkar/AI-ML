# # lecture 5 --> threading
import threading
# def cube(num):
#     print("Cube of number is: ", num**3)
# def square(num):
#     print("Square of number is: ", num**2)

# if __name__ == "__main__":
#     num = 5
#     t1 = threading.Thread(target=cube, args=(num,))
#     t2 = threading.Thread(target=square, args=(num,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()

import os
def assigntask1():
    print("task 1 assigned to thread {}".format(threading.current_thread()))
    print("id of process {}".format(os.getpid()))
def assigntask2():
    print("task 2 assigned to thread {}".format(threading.current_thread()))
    print("id of process {}".format(os.getpid()))
    
if __name__ == "__main__":
    print("id of running process {}".format(os.getpid()))
    t1 = threading.thread(target=assigntask1,name = 't1')
    t2 = threading.thread(target=assigntask2,name = 't2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()