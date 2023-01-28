p=int(input())

n=2*p-1

for i in range(n):

    for j in range(n):

        if(i<n/2):

            p=i

        else:

            p=n-1-i

        if(j<n/2):

            k=j

        else:

            k=n-1-j

        if(p>k):

            print(chr(k+97),end=" ")

        else:

            print(chr(p+97),end=" ")

    print(" ")
