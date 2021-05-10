import subprocess
import os
def main():
    dir = os.getcwd()
    print("Currently working in directory: " + dir)
    cmd = os.chdir(dir)
    with open("output.txt","w") as f:
        while True:
            cmd = input(">>> ")
            list_files = subprocess.run([cmd])
            print("The exit code was: %d" % list_files.returncode)
            f.write(str(list_files))
main()