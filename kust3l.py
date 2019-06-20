import subprocess
from github import Github
import getpass

#def getfiles(path,gh) :


if __name__ == "__main__":
    with open(r'giturls.txt','r') as f:
        for line in f :
            line = line.replace('tree/master','trunk')
            arr = line.split('=')
            if arr[0].strip() == 'base1' :
                out = subprocess.Popen(['mkdir','-p', './kustdemo1','./kustdemo1/overlay1'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                stdout,stderr = out.communicate()
                print(stdout)
                print(stderr)
                out1 = subprocess.Popen(['svn', 'export', arr[1].strip(),'./kustdemo1/base'] ,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                stdout,stderr = out1.communicate()
                print(stdout)
                print(stderr)
            if arr[0].strip() == 'base2' :
                out = subprocess.Popen(['mkdir','-p' ,'./kustdemo1/overlay1/overlay2'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                stdout,stderr = out.communicate()
                print(stdout)
                print(stderr)
                out1 = subprocess.Popen(['svn', 'export', arr[1].strip(),'./kustdemo1/overlay1/platform1'] ,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                stdout,stderr = out1.communicate()
                print(stdout)
                print(stderr)
            if arr[0].strip() == 'base3' :
                out1 = subprocess.Popen(['svn', 'export', arr[1].strip(),'./kustdemo1/overlay1/overlay2/microservice1'] ,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                stdout,stderr = out1.communicate()
                print(stdout)
                print(stderr)
