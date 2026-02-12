import art
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

math_operations = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide,
}
def calculator():
    continue_calc = True
    #only shown the first time
    print(art.logo)
    # first number in the calculator can later be the result
    first_number = float(input("What is the first number?"))
    while continue_calc:
        # show the user the choice of operations
        for operation in math_operations:
            print(operation)
        # user input to choose an operation
        operation_chosen = input("Pick an operation: ")

        # ask the user for the next number
        second_number = float(input("What is the next number?"))
        answer = math_operations[operation_chosen](first_number, second_number)
        print(f"{first_number} {operation_chosen} {second_number} = {answer}")
        new_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if new_calc == 'y':
            #first number becomes the answer and we pick up at operation picking
            first_number = answer
            continue_calc = True
        elif new_calc == 'n':
            #new numbers and reshow logo
            print("\n"*20)
            calculator()
calculator()