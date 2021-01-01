import sys
import os.path
import glob

argc = len(sys.argv)
parameters = sys.argv

command = sys.argv[0]

files = glob.glob(r"*.mp3")
count = 0

if(argc < 1):
    print("Usage: ", command, "argments .....")
    exit(1)

else:
    fileNameW = sys.argv[1]

    with open(fileNameW, "w", encoding="UTF-8") as w_file:
        for file in files:
            if count != len(files) - 1:
                w_file.write("{}\n".format(os.path.abspath(file)))
            else:
                w_file.write("{}".format(os.path.abspath(file)))
            count += 1