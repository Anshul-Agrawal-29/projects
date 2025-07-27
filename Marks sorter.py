
students=int(input("enter the no of students"))





report={"name" : "abc",
        "english" : 00,
        "maths" : 00,
        "science" : 00,
        "sst" : 00,
        'percentage' : 00,
        "grade" : 00
        
        
}


for ni in range(students):
    name2=input("enter the name of the student")
    n1=int(input("enter the marks in eng"))
    n2=int(input("enter the marks in maths"))
    n3=int(input("enter the marks in science"))
    n4=int(input("enter the marks in sst"))




    total=(n1+n2+n3+n4)
    per= (total/4)
    if per>= 85:
        report["grade"]='A'
    elif per>= 75:
        report["grade"]='B'
    elif per>= 65:
        report["grade"]='C'
    else:
        report["grade"]='D'






    report["name"]= name2
    report["maths"]= n2
    report["english"]= n1
    report["science"]= n3
    report["sst"]= n4
    report["percentage"]= per

    
    

    for key, value in report.items():
        print(key,":", value)





    