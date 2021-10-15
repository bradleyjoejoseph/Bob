#modules
import versionControl
import commands

#modules


#global variables
version = versionControl.getVersion()
#global variables


#main code

def main():
    choice = None
    welcome()
    promt()

#main code


#welcome function

def welcome():
    print("Hey there my name is Bob, you are currently running version", version)

#welcome function

#promt functions TODO

def checkPromt(cmd):
    if cmd not in commands.cmds:
        print(cmd, " is not in our command libarary are you sure you spelt it correctly. /cmds to see all commands.")
        return False
    else:
        return True


def promt():
    while True:
        cmd = input("Type '/' command, '/cmds' for list of commands or '/quit' to exit\n")
        check = checkPromt(cmd)
        if check == True:
            commands.cmdExec(cmd)


#promt functions



main()