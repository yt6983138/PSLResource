import os
import sys
import subprocess

if __name__ == "__main__":
    targetFolder = sys.argv[1]
    os.makedirs(targetFolder, exist_ok=True)
    print("listing devices...")
    os.system(".\\adb.exe devices")
    input("enter if has device")
    print("finding path...")
    res = str(subprocess.check_output("""adb shell su -c "find /data/app/ | grep com.PigeonGames.Phigros | grep base.apk" """).strip()).replace("'", "")
    res = res.startswith("b") and res[1::] or res
    print(res)
    print("copying apk...")
    cmd = ".\\adb.exe shell su -c cp \"" + res + "\" /storage/emulated/0/dump/"
    print(cmd)
    os.system(cmd)
    print("pulling apk...")
    os.system(".\\adb.exe pull /storage/emulated/0/dump/base.apk .\\" + targetFolder + '\\')
    output = os.popen(".\\adb shell ls /storage/emulated/0/Android/obb/com.PigeonGames.Phigros/").read()
    output = output.replace("\n", "")
    print("pulling obb...")
    os.system(".\\adb pull /storage/emulated/0/Android/obb/com.PigeonGames.Phigros/" + output + " .\\" + targetFolder + '\\')
    print("doing shits in wsl now...")
    print("wsl -e python3 auto_linux.py " + targetFolder)
    os.system("wsl -e python3 auto_linux.py " + targetFolder)

