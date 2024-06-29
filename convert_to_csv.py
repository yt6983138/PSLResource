import os

def main():
    os.makedirs("./csv/", exist_ok=True)

    diffSrc = open("./difficulty.tsv", encoding="utf8")
    nameSrc = open("./info.tsv", encoding="utf8")

    diffDes = open("./csv/difficulty.csv", "w", encoding="utf8")
    nameDes = open("./csv/info.csv", "w", encoding="utf8")

    diffDes.write(diffSrc.read().replace('\t', ','))
    print("convert diff done")
    nameDes.write(nameSrc.read().replace('\t', '\\'))
    print("convert info done")

if __name__ == "__main__":
    main()