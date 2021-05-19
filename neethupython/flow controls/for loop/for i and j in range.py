#111 222 333
# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end=" ")
#     print( )

#123 123 123
# for i in range(1,4):
#     for j in range(1,4):
#         print(j,end=" ")
#     print( )

#1
#12
#123
# for i in range(1,4):  #1
#     for j in range(1,i+1):  #1  2
#         print(j,end=" ")  #1  2
#     print( )

#5 4 3 2 1
#4 3 2 1     i reperesent as row wise
#3 2 1        j represent column wise
#2 1
#1
# for i in range(0,5):   #0 1
#     for j in range(5-i,0,-1): #5,0   5-1,0
#         print(j,end=" ") # 5 4 3 2 1   4,
#     print( )
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5
# for i in range(1,6): #2
#     for j in range(1,i+1):   1,3
#         print(i,end=" ")  1
#     print( )
#*
#**
#***
#****
#*****
# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print( )
#1
#5 5 5 5 5
#4 4 4 4
#3 3 3
#2 2
#1
#
# for i in range(5,0,-1):  #5
#     for j in range(1,i+1):  #
#         print(i,end=" ") #5
#     print( )

#1 1 1 1 1
#2 2 2 2
#3 3 3
#4 4
#5

# for i in range(1,6):  #1
#     for j in range(i-1,5):  #0 5
#         print(i,end=" ")
#     print( )

#0 1 2 3 4 5
#0 1 2 3 4
#0 1 2 3
#0 1 2
#0 1

# for i in range(5,0,-1):  #1
#     for j in range(0,i+1):  #5
#         print(j,end=" ")
#     print( )





#1
#2 1
#3 2 1
#4 3 2 1
#5 4 3 2 1
# 6 5 4 3 2 1
# for i in range(0,6):  #0 1
#     for j in range(i+1,0,-1): #1,0
#         print(j,end=" ")#0
#     print( )

#pyramid
for i in range(0,5):
    for j in range(0,5-i-1):
         print(end=" ")

    for j in range(0,i+1):
        print('*',end=" ")
    print( )