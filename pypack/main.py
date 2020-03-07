import subprocess
import sys
import os
import importlib


def install(pack):
    cmd = ['pip','install','--user']
    cmd.append(pack)
    result = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    out = result.stdout.readlines()
    for x in out:
        out[out.index(x)] = x.decode('utf-8').strip()
    # out = out.splitlines()
    for x in out:
        print(x)

if __name__ == '__main__':
    package = sys.argv[1:]
    # print(package)
    if '-r' in package:
        NAME = package[-1]
        f = open(NAME,'r')
        package = f.readlines()
        
        for x in package:
            install(x)
        f.close()
    else:
        PATH = os.getcwd()
        im = package[-1]
        # print(PATH)
        try:
            trypack = importlib.import_module(im)
            print("Module " + im + " exists")
        except ImportError as e:
            f = open(PATH + '/requirements.txt','a')
            f.write(f"{im}\n")
            install(im)
            f.close()




