import subprocess
import sys
import os
import importlib
import pkg_resources


def install(pack):
    cmd = ['pip','install','--user']
    cmd.append(pack)
    execute(cmd)
    
def uninstall(pack):
    cmd = ['pip', 'uninstall', '--yes']
    cmd.append(pack)
    execute(cmd)

def execute(cmd):
    result = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    out = result.stdout.readlines()
    for x in out:
        out[out.index(x)] = x.decode('utf-8').strip()
    # out = out.splitlines()
    for x in out:
        print(x)


if __name__ == '__main__':
    installed = [pkg.key for pkg in pkg_resources.working_set]
    package = sys.argv[1:]
    # print(package)
    if 'install' in package:
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
            if im in installed:
                print("Module " + im + " exists")
            else:
                f = open(PATH + '/requirements.txt','a')
                f.write(f"{im}\n")
                install(im)
                f.close()

    elif 'uninstall' in package:
        if '-r' in package:
            NAME = package[-1]
            f = open(NAME,'r')
            packages = f.readlines()
            for x in packages:
                uninstall(x)
            f.close()
            f = open(NAME,'w')
            f.truncate(0)
            f.close()
        else:
            PATH = os.getcwd()
            im = package[-1]
            if im in installed:
                f = open(PATH + '/requirements.txt','r')
                packages = f.readlines()
                f.close()
                f = open(PATH + '/requirements.txt','w+')
                # print(packages)
                for x in packages:
                    packages[packages.index(x)] = x.strip()
                uninstall(im)
                # print(im)
                packages.remove(im)
                f.truncate(0)
                for x in packages:
                    print(x)
                    f.write(f"{x}\n")
                f.close()
            else:
                print("Module " + im + " doesn't exist")
        



