dognames_dic = dict()
with open("dognames.txt", "r") as f:
    # Reads in dognames from first line in file
    line = f.readline()
    while line != "":
        line = line.strip()
        if line not in dognames_dic:
            dognames_dic[line] = [1]
        line = f.readline()
print(dognames_dic)
