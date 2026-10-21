# Monthly Expense Tracker


def main():
    print(f"1. View Current Spending\n2. Add Money to Spending\n3. See History ")






def display():
    

    while True:
        try:
            daily_expense = float(input("How much money did you spend today?: "))

            print(f"Your food expense today was $ {daily_expense:.2f}")
            break
        except ValueError:
            print("Please enter a valid number")



if __name__ == "__main__":
    main()
  
