n=int(input())

for i in range(0,9):

    for j in range(0,9):

     if(i>4):

        p=8-i

     else:

        p=i

     if(j>4):

        k=8-j

     else:

        k=j

     if(p<k):

        print(4-p+n,end=" ")

     else:

        print(4+n-k,end=" ")

    print(" ")
