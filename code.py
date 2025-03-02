def add_expense(expenses, amount, category):
  #The expenses parameter of your add_expense function will be a list o expenses.

  #Create a dictionary with a key 'amount' and value of the amount parameter and category pass your new dictionary to the .append() call.
  #All paramater form add_expense was on below code
    expenses.append({'amount': amount, 'category': category})


#2-define a function named print_expenses that takes one parameter expenses. This function will later be used to display each expense in your list. 

#create a for loop that iterates over each item in the expenses list.

# interpolating the expense dictionary in your f-string. Modify the f-string expression to access the value of the 'amount' key and the 'category' key in the expense dictionary.
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')


#3-need a function to calculate the total amount of expenses.
#Lambda functions are brief, anonymous functions in Python, ideal for simple, one-time tasks.  

#(sum(map(test, [2, 3, 5, 8])))
#map()-which executes a specified function for each element in a collection of objects, such as a list:
#map(lambda x: x * 2, [1, 2, 3])
#map has 2 argument
#The function to execute is passed as the first argument, and the iterable is passed as the second argument.
#result of the example above would be [2, 4, 6]



#in the total_expenses function, you'll now integrate a lambda function. a lambda function that has expense as its parameter.
#expense is expected to be a dictionary, and your lambda function should return the value of the 'amount' key in the expense dictionary.
#has we gonna sum all the total expense,we need to count each amout that being store inside expense dictionary, that why we use expenses as second argument in map()

#Finally, pass your map() call to the sum() function to obtain the total expenses and return the result ----result will return to while loop that we created below


def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))


#The filter() function allows you to select items from an iterable, such as a list, based on the output of a function:    

#filter() takes a function as its first argument and an iterable as its second argument. It returns an iterator, which is a special object that enables you to iterate over the elements of a collection, like a list.
    
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
    
#A while loop is another kind of loop that runs a portion of code as long as a specified condition is True. The loop terminates when the condition becomes False:


def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')


        #The input() function takes a user input and it returns the user input in the form of a string.
       
        choice = input('Enter your choice: ')

        #After getting the amount and category using input(), call the add_expense function, passing three arguments: expenses, amount and category.

        #expenses is the empty list created in the main function earlier in this project.
        #amount is the amount of the expense.
        #category is the category of the expense.

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')


            #you need to filter the expenses and print the filtered list. Declare a variable expenses_from_category and assign it a call to filter_expenses_by_category passing expenses and category as the argument.
            
           expenses_from_category = filter_expenses_by_category(expenses, category)
           print_expenses(expenses_from_category)
    
        elif choice == '5':
            print('Exiting the program.')
            break
