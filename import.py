

filelist = [
    "./data/corpus-min-amr.txt",
    "./data/corpus-min-ucca.txt",
    "./data/corpus-min-drs.txt",
    "./data/corpus-min-ud.txt",
]


if __name__ == "__main__":
    file = filelist[0]

    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if not line:
                continue
            print(line)