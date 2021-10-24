#commands - Everything to do with commands
import timer
import os
import versionControl

cmds = ["/cmds", "/quit", "/timer", "/chrome", "/path", "/version"]

def cmdExec(cmd):
    if cmd == "/cmds":
        print("\n\t".join(cmds))
    if cmd == "/quit":
        exit()
    if cmd == "/timer":
        h = int(input("Hours: "))
        m = int(input("Minutes: "))
        s = int(input("Seconds: "))
        timer.timer(h, m, s)
    if cmd == "/chrome":
        os.startfile("C:\Program Files\Google\Chrome\Application\Chrome")
    if cmd == "/path":
        print(versionControl.path)
    if cmd == "/version":
        print(versionControl.getVersion())
