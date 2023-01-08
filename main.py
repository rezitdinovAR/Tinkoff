import sys
from funcs import distance


compare_files_path = sys.argv[1]
out_path = sys.argv[2]
compare_files = open(compare_files_path, 'r')
out_file = open(out_path, 'w')

compare_files_list = compare_files.readlines()
for line in compare_files_list:
    line = line.split(' ')
    line[1] = line[1].replace('\n','')
    with open(line[0]) as f:
        a = f.read()
    with open(line[1]) as g:
        b = g.read()
    if 1-distance(a,b)/len(a) < 0:
        out_file.write('0' + '\n')
    else:
        out_file.write(str(1-distance(a,b)/len(a)) + '\n')

out_file.close()