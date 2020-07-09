import multiprocessing

def f1():
    import RDA_main_1

def f2():
    import NFBTk_pre 

t1=multiprocessing.Process(target=f1)
t2=multiprocessing.Process(target=f2)

t1.start()
t2.start()

t1.join()
t2.join()
