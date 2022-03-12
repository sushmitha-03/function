def fun():
    a=0
    i=0
    s=0
    while i<3:
        n=int(input("enter a no"))
        s=s+n
        a=a+n
        i+=1
    print("sum:",s)
    print("average:",a//3)
fun()