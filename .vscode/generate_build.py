import os, sys

fileList = ignore = []
sourcePrefix = "src"
buildPrefix = "builds"
buildName = "a"
needRebuild = False
workspaceFolder = os.getcwd()
sourceFolder = os.path.join(workspaceFolder, sourcePrefix)
buildFolder = os.path.join(workspaceFolder, buildPrefix)
buildExe = os.path.join(buildFolder, buildName + ".exe")
includeFolder = os.path.join(workspaceFolder, "include")
libFolder = os.path.join(workspaceFolder, "lib")
extras = [
    "-g",
    "-I"+includeFolder,
    "-L"+libFolder,
    "-lmingw32",

    # Uncomment the following lines if you use SFML (you have to change the last line for other Graphical libraries)
    # "-Wl,-subsystem,windows",
    # "-lsfml-graphics -lsfml-window -lsfml-system"
    ]

def extraListToString():
    result = ""
    for arg in extras:
        result += " " + arg
    return result

for file in os.listdir(sourceFolder):
    if file.endswith(".cpp") and not file in ignore:
        fileList.append(sourcePrefix + "/" + file)
        if not os.path.exists(buildExe) or os.stat(os.path.join(sourceFolder, file)).st_mtime > os.stat(buildExe).st_mtime:
            needRebuild = True

if os.stat(__file__).st_mtime > os.stat(buildExe).st_mtime:
    needRebuild = True

if needRebuild:
    print "building ..."
    cmd = "g++ " + " ".join(fileList) + extraListToString() + " -o " + buildPrefix + "/" + buildName
    os.system(cmd)
