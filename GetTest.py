import sys
n = sys.argv[3]
if n != "-1":
    f_in = open(sys.argv[1], 'w') # +".txt"
    f_out = open(sys.argv[2], 'w')
    with open("timian.md", 'r') as q:
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
                sys.exit(0)
            line = q.readline()
    f_in.close()
    f_out.close()
    print("Failed to get Sample #"+n)
    sys.exit(1)
else:
    print("Using lagre sample...")
