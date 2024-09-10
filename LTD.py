# L1 = [9,0,9,2,6,3,3,3]
# print(L1)
# print(L1[2])
# print(L1[0:3])
# print(L1[-4:-2])

#concadination
# L1=[11,22,33,44]
# L2=[10,20,30]
# res = L1+L2
# print(res)

# t1 = ("dhanush","dhoni","suriya")
# t2 = ('ajith',"vijay",90,30,"abi")
# res = t1+t2
# print(res)
#########################error##############3
# D1 = {'A':100,'B':200}
# D2 = {'x':"bn",'y':"nb"}
# res = D1+D2
# print(res)

#################dulication##############
# L1 = [10,20,30,40]
# res =L1*3
# print(res)

###############membership operator##################
# var = "python is easy"
# res = "python" in var
# print(res)

# L1 = [1,2,3,4,55,66,77,8]
# res = 55 in L1
# print(res)

# L1 = [1,0,9,2,8,3]
# res = len(L1)
# print(res)

# D1 = {'A':10,'B':20,'C':30,'D':40,'E':2, 'F':1}
#
# print(max(D1))
#
# L1 = [10,20,30,40,50]
# T1 = (10,20,30,40,50)
# D1 = {'A':10,'B':20,'C':30,'D':40,'E':50}
#
# print(type(T1))
#
# res = len(L1)
# print(res)
#
# res = max(T1)
# print(res)
#
# res = min(D1)
# print(res)

# strlist =('dhanush','ajith','dhoni','prem','virat')
# print(min(strlist))

# L1 =[10,20,40,50]
# L1.app(30)
# print(L1)
# ################'tuple' object has no attribute 'extend'
# T1 = (10,20,30,40,50)
# T1.extend(60)
# print(T1)

D1 = {'A':10,'B':20,'C':30,'D':40,'E':50}
D1.setdefault('A',60)
print(D1)
