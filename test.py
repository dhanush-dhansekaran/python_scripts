# # count = 0
# # for i in range(1,101):
# #     if(i%3==0 and i%5==0 ):
# #       count =count+1
# # print(count)
# # nums=(10,20,30,40,50,60,70,80)
# # for x in nums:
# #     if(x == 40):
# #         pass
# #     print(x)
#
# 1. 	write a program for the basketball selection,
# 	take height (float) as the input from the user and verify whethetr his height is 6.0 and above if yes
# 	he is selected , if height is less that 6.0 please print not selected
# height = float(input("height = "))
# if(height >= 6.0):
#     print("he is selected")
# else:
#     print("he is not selected")

# 2. Write a program for the school registry exmple
# please take total marks as input from user for max 100
# calculate the percentage of the total marks and verify if the student has passed in which grade
#
# >=0 and  <35    ----> FAIL
# >=35 and < 50   ====> passed in third class
# >=50 and < 60  ====> passed in second class
# >=60 and <85 ====> passed in first class
# >=85 and <= 100  ==> distinction
# # apart above any other percentage comes its invalid entry
# total_marks =int(input("enter the mark (out of 100) = "))
# percent =(total_marks/100)*100
# print("percent={percent}  %")
# if(percent >=0 and percent  < 35):
#     print("fail")
# if(percent >=35 and percent < 50):
#     print("passed in third class")
# if(percent>=50 and percent < 60):
#     print("passed in second class")
# if(percent>=60 and percent <85):
#     print("passed in first class")
# if(percent>=85 and percent <= 100):
#     print("distinction")
#
# 4.List1 =[ 50, 33 , 27 , -20 , 85 , 74 , 4,9,3,7]
# Write a program which prints how many even and odd numbers are there in the above list
List =(50,33,27,-20,85,74,4,9,3,7)
odd_count = 0
even_count = 0
for num in List:
    if(num % 2==0):
        even_count +=1
        print("Number of even number = ", even_count)

    else:
        odd_count +=1
        print("Number of odd numbers= ", odd_count)


# 5.L1 = ["python is good" , "Java is ok" , "i love python" , "c is mother lang" , "python rocks"]
#
# please print all the elements of the list which has word python present in it and count how many elements contsins python word
#
# L1 = ("python is good" , "Java is ok" , "i love python" , "c is mother lang" , "python rocks")
# count = 0
# for x in L1:
#     if("python" in x):
#         print("python is good")
#     if("python" in x):
#         print("Java is ok")
#     if(x == "python"):
#         print("i love python")
#     if(x == "python"):
#         print("c is mother lang")
#     if(x == "python"):
#         print("python rocks")
#         count = count+1
#         print(count)
#     else:
#         print("python word not found")

















