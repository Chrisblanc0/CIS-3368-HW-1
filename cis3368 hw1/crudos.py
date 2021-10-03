import mysql.connector
from mysql.connector import Error #importing the database
from sql import create_connection #from sql import the create connection
from sql import execute_query #from sql import the execute query
from sql import execute_read_query #import the read query
import datetime
from datetime import date #want it in standard date time



#create connection to mysql database
conn = create_connection("cis3368.c3wbowheifjy.us-east-2.rds.amazonaws.com", "admin", "Morena.1974", "cis3368fall21")

#showing the shoppinlist table and data
select_shoppinglist = "SELECT * FROM shoppinglist"
shoppinglist = execute_read_query(conn, select_shoppinglist)
print(shoppinglist)

query = "INSERT INTO invoices (id, itemdescription, quantity, dateadded)"

while(True): # a true statment and shows command line to let the shopper choose an option
    print("\nMENU: " )
    print("a - add item")
    print("d - remove item")
    print("u - update item details")
    print("r1 - outputs all items in alphabetical order")
    print("r2 - output all items by sorted by quantity(ascending)")
    print("q - quit")



     choice = str(input("please select an option: ")) #asking the shopper what do they want to choose

     if(choice == "a"): #if they choose to remove an item
         execute_query(conn, shoppinglist) #use the execute query function to add something
         z = str(input("please select an item to add")) #ask for what item
         y = str(input("how many do you want to add?")) #ask how many
         shoppinglist_itemdescription = z
         shoppinglist_quantity = y
         select_shoppinglist = "SELECT * FROM shoppinglist" #uses that info and adds that amkunt to that item

     if(choice == "d"): #this is for when they want to delete an item
         shoppinglist_itemdescription_to_delete = str(input("please select the item description to delete")) #ask what item to delete
         delete_statement = "DELETE FROM shoppinglist WHERE itemdescription = shoppinglist_itemdescription_to_delete" % (shoppinglist_itemdescription_to_delete) #deletes it in the database
         execute_query(conn, delete_statement) #executes that action

     if(choice == "u"): #this is for when they choose to update a new item to quantity
         new_quantity = int(input("")) #ask the user how much they want to add
         update_shoppinglist_query = " " " 
         UPDATE quantity #this is the code from class to update something 
         SET amount = new_quantity



     if(choice =="r1"): #if they want to print out the shopping list in alphabetical order
         select_shoppinglist = "SELECT * FROM shoppinglist"
         shoppinglist = execute_read_query(conn, select_shoppinglist)
         sorted_list = sorted(shoppinglist)#https://www.kite.com/python/answers/how-to-sort-a-list-alphabetically-in-python
         print(sorted_list)
    
     if(choice == "r2"):
         select_shoppinglist = "SELECT * FROM shoppinglist"
         shoppinglist = execute_read_query(conn, select_shoppinglist)#this sort the list in ascending order by quantity
         shoppinglist.sort() #https://www.tutorialsteacher.com/python/list-sort
         print('List in ascending order: ', shoppinglist)



     if(choice == "q"): #this is to quit and return to main()
         quit()
    
    










         






   


