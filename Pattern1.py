n=int(input())

p=0

x=n

for i in range(1,n+1):

    print(2*(i-1)*'*',end="")

    for j in range(1,(n-i+1)+1):

              print(j+p,'0',end="",sep="")

    for k in range(1,(n-i+1)+1):

              print(k+p+x**2,end="",sep="")

              if k<x:

                 print('0',end="",sep="")

    x=x-1

    p=p+n-i+1

    print(end="\n")
