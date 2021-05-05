class Cinema():
    tickets_purchased=0
    current_income=0
    max_total_income=0
    seat_wise_info={}
    booked_seats=[]
    price1=10
    price2=8
    def __init__(self,r,c):
        self.row=r
        self.col=c
        self.total_seats=self.row*self.col
    
    def seat_display(self):
        if self.booked_seats==[]:
            l=[]
            k=['S']*self.col
            for i in range(self.row):
                l.append(k)
            j=list(map(str,list(range(1,self.col+1))))
            print(" "+" "+(" ").join(j))
            for i in range(1,r+1):
                print(str(i) + " " + (" ").join(l[i-1]))
        else:
            l=[]
            for i in range(self.row):
                l.append(['S']*self.col)
            for i in self.booked_seats:
                l[i[0]-1][i[1]-1]='B'
            print(" "+" "+(" ").join(list(map(str,list(range(1,self.col+1))))))
            for i in range(1,r+1):
                print(str(i) + " " + (" ").join(l[i-1]))
            
    
    
    def buy_ticket(self):
        status='not vacant'
        while status=='not vacant':
            a=int(input('Select row no-'))
            b=int(input('Select column no-'))
            if (a,b) in self.booked_seats:
                print("Please choose a different seat as this one is already booked")
            elif a not in range(1,self.row+1) and b not in range(1,self.col+1):
                print("Error: absurd value detected. Both row and column address should be non-zero positive integer less than equal to row and column respectively")
            else:
                if self.total_seats<=60:
                    self.max_total_income=self.price1*self.total_seats
                    print("Price of this seat is ${}".format(self.price1))
                    if input("Do you want to confirm this booking? Yes/No")=="Yes":
                        status="vacant"
                        self.tickets_purchased+=1
                        self.current_income+=self.price1
                        self.booked_seats.append((a,b))
                        print("Please enter your following details")
                        name=input("What's your name")
                        gender=input("M/F/Other")
                        age=int(input('How old are you?'))
                        phone_no=input('contact number')
                        print("Seat booked successfully")
                        self.seat_wise_info[(a,b)]=(name,gender,age,phone_no,self.price1)
                    else:
                        print("OK, you will now be directed to the initial menu")
                else:
                    self.max_total_income=(self.price1*(self.row//2)*self.col)+(self.price2*(self.row-(self.row//2))*self.col)
                    if a<=self.row//2:
                        print("Price of this seat is ${}".format(self.price1))
                        if input("Do you want to confirm this booking? Yes/No:")=="Yes":
                            status="vacant"
                            self.tickets_purchased+=1
                            self.current_income+=self.price1
                            self.booked_seats.append((a,b))
                            print("Please enter your following details")
                            name=input("What's your name? ")
                            gender=input("M/F/Other: ")
                            age=int(input('How old are you? '))
                            phone_no=input('contact number: ')
                            print("Seat booked successfully")
                            self.seat_wise_info[(a,b)]=(name,gender,age,phone_no,self.price1)
                    else:
                        print("Price of this seat is ${}".format(self.price2))
                        if input("Do you want to confirm this booking? Yes/No")=="Yes":
                            status="vacant"
                            self.tickets_purchased+=1
                            self.current_income+=self.price2
                            self.booked_seats.append((a,b))
                            print("Please enter your following details")
                            name=input("What's your name? ")
                            gender=input("M/F/Other: ")
                            age=int(input('How old are you? '))
                            phone_no=input('contact number: ')
                            print("Seat booked successfully")
                            self.seat_wise_info[(a,b)]=(name,gender,age,self.price2,phone_no)
                        
         
                  
                    
           
    def stat(self):
        print('No of purchased tickets: {}'.format(self.tickets_purchased))
        print('% tickets booked: {}%'.format((self.tickets_purchased/self.total_seats)*100))
        print('Current Income: ${}'.format(self.current_income))
        print('Total Income: ${}'.format(self.max_total_income))
    
        
    def show_info(self):
        print("What seats information do you want?")
        y=int(input("Row number:"))
        z=int(input("Column number:"))
        if (y,z) in self.seat_wise_info:
            print("Name: {}\nGender: {}\nAge: {}\nPhone no: {}\nTicket price: {}".format(self.seat_wise_info[(y,z)][0],self.seat_wise_info[(y,z)][1],self.seat_wise_info[(y,z)][2],self.seat_wise_info[(y,z)][3],self.seat_wise_info[(y,z)][4]))
        else:
            print("This seat is vacant given it's in the realm of reality")


x = 10
r=int(input('No of rows in cinema are : '))
c=int(input('No of seats in a row are : '))
moviehall=Cinema(r,c)

while x!=0:
    print('1=> Show the seats')
    print('2=> Buy a Ticket')
    print('3=> Statistics')
    print('4=> Show booked Tickets User Info')
    print('0 to Exit')
    x=int(input())
    if x==1:
        moviehall.seat_display()
    elif x==2:
        moviehall.buy_ticket()
    elif x==3:
        moviehall.stat()
    elif x==4:
        moviehall.show_info()
    elif x==0:
        print('Maybe some other movie, see u nxt time')
