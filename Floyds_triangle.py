#Take input from the user
rows= int(input("Enter the total number of rows:"))
num= 1  #initialize 1

print("Floyd's Triangle")
#outer loop for number of rows
for i in range(1, rows, 1):
    #inner loop for number of columns
    for j in range(1,i +1):
        #display result
        print(num, end='  ')
        num+=1
    print()    