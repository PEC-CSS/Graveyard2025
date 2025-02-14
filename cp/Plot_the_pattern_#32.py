n = int(input("Enter size parameter of square(N): "))
prnum=0

for i in range(0,2*n):
    
    cutout= []
    
    # Printing each line of main square
    for j in range(1,2*n+1):
        if i<n and j>=n-i+1 and j<=n+i and i!=0 and i!=2*n-1:
            print(" ",end="")
            cutout.append(prnum)
        elif i>=n and j>i-n+1 and j<=2*n-(i-n+1) and i!=0 and i!=2*n-1:
            print(" ",end="")
            cutout.append(prnum)
        else:
         print(prnum,end="")
        prnum+=1
        if prnum==10:
            prnum=0
            
    # Printing the cutout for each line
    
    print(" "*(int(3+(n-1-(len(cutout)/2)))),end="")
    for num in cutout:
        print(num,end="")
    print()