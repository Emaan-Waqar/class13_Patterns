#take input from the user
n= int(input("Enter the number of rows: "))

#upper half
for i in range(1, n+1, 2):
    spaces= (n-i) //2
    print(" " * spaces, end= "")
    for j in range(1, i +1):
        print(j, end="")
    print() 
#Lower half
for i in range(n-2, 0, -2) :
    spaces =  (n-i) // 2
    print(" " * spaces, end= "")
    for j in range(1,i+1):
        print( j, end="")
    print()    