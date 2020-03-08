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



def main():
    installed = [pkg.key for pkg in pkg_resources.working_set]
    package = sys.argv[1:]
    # print(package)
    if 'install' in package:
        if '-r' in package:
            PATH = os.getcwd()
            NAME = package[-1]
            f = open(NAME,'r')
            packages = f.readlines()
            for x in packages:
                install(x)
            f.close()
            with open(PATH + '/requirements.txt', 'r') as f:
                mod = f.readlines()
                f.close()
            newmod = list(set(mod) | set(packages))
            with open(PATH + '/requirements.txt', 'w') as f:
                f.truncate(0)
                for x in newmod:
                    x = x.strip()
                    # print(x)
                    f.write(f"{x}\n")
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
            PATH = os.getcwd()
            with open(PATH + '/requirements.txt','r') as f: 
                mod = set(f.readlines())
                f.close()
            newmod = list(mod - set(packages))
            for x in newmod:
                newmod[newmod.index(x)] = x.strip()
            # print(newmod)
            with open(PATH + '/requirements.txt','w') as f:
                f.truncate(0)
                for x in newmod:
                    f.write(f"{x}\n")
                f.close()

        else:
            PATH = os.getcwd()
            im = package[-1]
            if im in installed:
                f = open(PATH + '/requirements.txt','r')
                packages = f.readlines()
                f.close()
                f = open(PATH + '/requirements.txt','w')
                # print(packages)
                for x in packages:
                    packages[packages.index(x)] = x.strip()
                uninstall(im)
                # print(im)
                packages.remove(im)
                f.truncate(0)
                for x in packages:
                    # print(x)
                    f.write(f"{x}\n")
                f.close()
            else:
                print("Module " + im + " doesn't exist")
        


if __name__ == '__main__':
    main()