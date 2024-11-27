import sys
n = sys.argv[3]
if n != "-1":
    f_in = open(sys.argv[1], 'w', encoding='utf-8') # +".txt"
    f_out = open(sys.argv[2], 'w', encoding='utf-8')
    with open("timian.md", 'r', encoding='utf-8') as q:
        line = q.readline()
        while line:
            if "样例 #"+n in line:
                for i in range(4):
                    line = q.readline()
                while line:
                    line = q.readline()
                    if("```" in line):
                        break
                    f_in.write(line)
                print("Successfully get Sample Input #"+n)
                for i in range(4):
                    line = q.readline()
                while line:
                    line = q.readline()
                    if("```" in line):
                        break
                    f_out.write(line)
                print("Successfully get Sample Output #"+n)
                break
            line = q.readline()
    f_in.close()
    f_out.close()
else:
    print("Using lagre sample...")