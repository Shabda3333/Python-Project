
import sqlite3
conn = sqlite3.connect('Watchlist.db')
c = conn.cursor()
# c.execute("""CREATE TABLE Watchlist (
#             dramaName text,
#             Genre text,
#             priorityNum integer
#             ) """)

class User:
    def __init__(self,name,age):
        self.userName=name
        self.userAge=age


    #INSERTION ACCORDING TO USER INPUT
    def insertion(self):
        ans = ('yes')
        while True:
            print("\nDo you want to add  dramas into your watchlist ? (Type in yes or no)")
            ans = input('-> ')
            if (ans.lower() == 'yes'):
                name = input('\nName: ')
                genreName = input('Genre: ')
                priority= int(input('Priority(1-10, lowest-highest): '))
                c.execute("""
                INSERT INTO Watchlist(dramaName,Genre,priorityNum)
                VALUES (?,?,?)
                """, (name, genreName, priority))
                conn.commit ()
                print ( '\nYOUR DATA HAS BEEN ENTERED SUCCESSFULLY :)' )  
            else:
                break

        print('INSERTION HAS FINISHED!!')



    #SEARCHING ACCORDING TO GENRE OF DRAMA
    def search(self):
        searchBase = input("\nEnter a Genre of the drama you want to watch: ")
        selection = ''' SELECT * from Watchlist where Genre like '%{}%' '''.format(searchBase)
        result = c.execute(selection)
        condition = False
        for data in result:
            condition = True
            print(f"\nDrama Name: {data[0]}")
            print(f"Priority: {data[2]}")  
            print('------------------*------------------')
            conn.commit()
        if condition == False:
            print(':( OOPS!! THE DRAMA YOU SEARCHED IS NOT IN YOUR WATCHLIST.')
            
        
        
        
            
    #DELETION ACCORDING TO NAME OF DRAMA
    def delete(self):
        delBase = input("\nEnter the Drama Name you want to delete: ")
        sel = ''' SELECT * from Watchlist where dramaName like '%{}%' '''.format(delBase)
        result = c.execute(sel)
        
        for data in result:
            delSel = ''' DELETE from Watchlist where dramaName like '%{}%' '''.format(delBase)
            c.execute(delSel)
            print(f"{data[0]} deleted succesfully!!")
            conn.commit()
            return
        print(':( OOPS!! THE DRAMA YOU WANT TO DELETE IS NOT IN YOUR WATCHLIST')



    #selection   
    def select(self):
        choice = 1 or 2 or 3 
        while True:
            print("\n**************************************************************")
            print("*  Select 1 to Insert the Drama Name in your Watchlist.      *")
            print("*  Select 2 to Search Drama from your Watchlist.             *")
            print("*  Select 3 to Delete the watched Drama from your Watchlist. *")
            print("*  Select 4 to exit.                                         *")
            print("**************************************************************\n")
            choice = int(input('YOUR SELECTED NUMBER: '))
             
            match (choice):
                case 1:
                    user1.insertion()
                case 2:
                    user1.search()
                case 3:
                    user1.delete()
                case 4:
                    break
                case _:
                    print("\nPlease, select the correct option.")
                



# driver code
print("\n*******************************")
print("**      DRAMA WATCHLIST      **")
print("*******************************")
print("\nHi,")
name=input('\nEnter your Name: ')
try:
    age=int(input('Enter your Age: '))
    if age<12:
        raise ValueError("\nSORRY (T_T) YOU ARE NOT ELIGIBLE FOR WATCHING DRAMAS.\n")
except ValueError as ve:
    print(ve)
    exit()

user1=User(name,age)
user1.select()


 

 
        
        
    
 


        

        

