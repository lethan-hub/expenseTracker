# Monthly Expense Tracker
import sqlite3
database = "tracker.db"

def main():
    while True:
        mainMenu = int(input(f"\n1. View Spending\n2. Add Money to Spending\n3. Exit\n\nPlease enter your pick:  "))
        match mainMenu:
            case 1:
                view_current()
            case 2:
                add()
            case 3:
                exit()
   
        


def add():

    conn = sqlite3.connect("tracker.db")
# cursor is basically the controller
    cursor = conn.cursor()

    # Create table
    cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
data TEXT, value INTEGER
)
""")





    while True:
                
                        try:
                            data_entry = input("What did you spend it on?: ")
                            value_entry = float(input("How much money did you spend today?: "))

                            sql_entry = "INSERT INTO users(data,value) VALUES (?,?)"
                            cursor.execute(sql_entry,(data_entry,value_entry))
                            conn.commit()
                            
                
                            print(f"\nYou bought {data_entry} for $ {value_entry:.2f}")
                            break
                        except ValueError:
                            print("Please enter a valid number")






if __name__ == "__main__":
    main()
  
