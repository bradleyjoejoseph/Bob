#versionControl - Everthing to do with the version type and tests

def getVersion():
    path = "C:/Users/PC/OneDrive/Documents/Programming Stuff/Laboratory/Python/Bob/version.txt"
    prefix = "TESTING "
    file = open(path, "r")
    version = round(float(file.read()), 4)
    file.close()
    file = open(path, "w") #comment out when published
    file.write(str(version + 0.001)) #comment out when published
    return prefix + str(version)