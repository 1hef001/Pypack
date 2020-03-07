import subprocess
import sys


def install(pack):
    cmd = ['pip','install','--user']
    cmd.append(pack)
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    print(result.stdout)

if __name__ == '__main__':
    package = sys.argv[1:]
    # print(package)
    if('-r' in package):
        NAME = package[-1]
        f = open(NAME,'r')
        package = f.readlines()
        
        for x in package:
            install(x)
        f.close()
    else:
        f = open('requirements.txt','a')
        f.write(f"{package[-1]}\n")
        install(package[-1])




