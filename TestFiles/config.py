import sys
from funcs import distance


compare_files_path = sys.argv[1]
out_path = sys.argv[2]
compare_files = open(compare_files_path, 'r')
out_file = open(out_path, 'w')

compare_files_list = compare_files.readlines()
for line in compare_files_list:
    line = line.split(' ')
    with open(line[0]) as f:
        a = f.read()
    with open(line[1]) as g:
        b = g.read()
    out_file.write(str(distance(a,b)/len(a)) + '\n')

out_file.close()