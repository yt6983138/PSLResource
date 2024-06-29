from configparser import ConfigParser
import os
import sys

def main(targetFolder):
    files = os.listdir(targetFolder)
    if (len(files) != 2):
        print("file count error")
        print(files)

    obbFile = ""
    apkFile = ""

    for file in files:
        if file.lower().endswith("obb"):
            obbFile = file
        elif file.lower().endswith("apk"):
            apkFile = file
        else:
            print("error file '" + file + "'")
    
    import gameInformation
    gameInformation.run(os.path.join(targetFolder, apkFile))

    c = ConfigParser()
    c.read("config.ini", "utf8")
    types = c["TYPES"]

    import resource_customformat
    resource_customformat.run(os.path.join(targetFolder, obbFile), 
    {
        "avatar": types.getboolean("avatar"),
        "Chart": types.getboolean("Chart"),
        "IllustrationBlur": types.getboolean("illustrationBlur"),
        "IllustrationLowRes": types.getboolean("illustrationLowRes"),
        "Illustration": types.getboolean("illustration"),
        "music": types.getboolean("music"),
        "UPDATE": {
            "main_story": c["UPDATE"].getint("main_story"),
            "side_story": c["UPDATE"].getint("side_story"),
            "other_song": c["UPDATE"].getint("other_song")
        }
    })

    import convert_to_csv
    convert_to_csv.main()

if __name__ == "__main__":
    main(sys.argv[1])
