# Monthly Expense Tracker

database = {} # Dictionary to hold the value and the amount


def main():
    while True:
        mainMenu = int(input(f"1. View Spending\n2. Add Money to Spending\n3. Exit\n\nPlease enter your pick:  "))
        match mainMenu:
            case 1:
                view_current()
            case 2:
                add(database)
            case 3:
                exit()
   
        
def view_current(database):
    if not database:
        print("Your database is currently empty")
    return database

def add():
    while True:
                
                        try:
                            data = input("What did you spend it on?: ")
                            value = float(input("How much money did you spend today?: "))
                
                            print(f"You bought {data} for $ {value:.2f}")
                            break
                        except ValueError:
                            print("Please enter a valid number")




if __name__ == "__main__":
    main()
  
