#list format
fname = open(r'C:\Users\Admin\Desktop\python step\project\ips.txt','r')
allname = fname.readlines()
# fname.close()
# print(allname)
###one by one name###
for n in allname:
    outfile = 'file' + n[0] + '.txt'
    print(outfile)
    filename =r'C:\Users\Admin\Desktop\python step\project\output'+"\\" + outfile
    fout = open(filename,'a')
    fout.write(n)
    fout.close()
