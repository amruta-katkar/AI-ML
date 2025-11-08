sub1=int(input("Enter subject1 marks:"))
sub2=int(input("Enter subject2 marks:"))
sub3=int(input("Enter subject3 marks:"))

if sub1<35 or sub2<35 or sub3<35 :
    print("fail")
else:
    avg=(sub1+sub2+sub3)/3
    if avg<35:
        print("fail")
    else:
        print("pass")

