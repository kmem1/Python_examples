import sys, os

def my_lister(currdir):
    print('[',currdir,']')
    for file in os.listdir(currdir):
        path = os.path.join(currdir, file)
        if not os.path.isdir(path):
            print(path)
        else:
            my_lister(path)

my_lister(os.getcwd())
