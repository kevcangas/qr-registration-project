import platform
import subprocess


def getIP():
    if platform.system() == 'Windows':
        local = subprocess.getoutput("""for /f "tokens=2 delims=[]" %a in ('ping -n 1 -4 "%computername%"') do @echo %a""")
    else:
        local = subprocess.getoutput("ifconfig | grep 'inet ' | grep -Fv 127.0.0.1 | awk '{print $2}'")
    return local


def run():
    print(getIP())


if __name__ == '__main__':
    run()