# Reading the data from, text file
# fnames = open(r'C:\Users\Admin\Desktop\python step\file\names.txt ','r')
# data =fnames.read()
# data =fnames.readlines()
# fnames.close()
# print(data)
# print(type(data))

# ## create a new text file and write data in text file
# fvar = open(r'C:\Users\Admin\Desktop\python step\file\newfile.txt','w')
# data = """dhanush got a job"""
# fvar.write(data)
# fvar.close()
# print(data)

########write data in created file##############
# fnames = open(r'C:\Users\Admin\Desktop\python step\file\players.txt','w')
# players =["dhoni","jadeja","dube","nattu"]
# fnames.writelines(players)
# fnames.close()
# print(players)
#
#
fnames = open(r'C:\Users\Admin\Desktop\python step\file\players.txt','w')
players =["dhoni","jadeja","dube","nattu"]
player =[]
for x in players:
    player.append(x+'\n')
fnames.writelines(player)
fnames.close()
print(player)
##########append mode
# fvar = open(r'dhanush d .txt' , 'w')
#
# data = """Congrats Modi for becoming
# PM 3 times in row
# June 8th is the
# swearing day
# Good luck
# """
#
# fvar.write(data)
# print(data)