marks=int(input('enter students marks :'))
while (marks>=0) and marks <=100:
    def progress():
        if (marks>=1) and marks <=30:
            print('E')
        elif (marks>30) and marks <=40:
            print('D')
        elif (marks >=41) and marks <=50:
            print('C')
        elif (marks>=51) and marks <=60:
            print('B')
        elif (marks >=70) and marks <=100:
            print('A')
        else:
            print('enter valid marks ')
     
    progress()             
    marks=int(input('enter students name'))



