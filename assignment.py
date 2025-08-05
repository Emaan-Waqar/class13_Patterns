n= int(input("Enter the number of rows: "))
#outer looop to handle the number of rows
for i in range (n):
    #Inner loop to handle number of columns
    for j in range(i+1):
        #display result
        print("*", end="  ")
    print()    
print("\n")
for i in range(1,n+1):
    for j in range(1,n+1):
        if (j <=n-i):
            print(' ',end= '  ')
        else:
            print('*',end='  ')    
    print()   