#versionControl - Everthing to do with the version type and tests
import os

path = __file__.replace("versionControl.py", "")

def getVersion():
    prefix = "TESTING "
    file = open(path + "version.txt", "r")
    version = round(float(file.read()), 4)
    file.close()
    file = open(path + "version.txt", "w")
    file.write(str(version + 0.001))
    return prefix + str(version)
