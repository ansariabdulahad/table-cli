index=1
def Table(number, lastNumber) :
    global index
    if index <= lastNumber :
        print(f"{number} * {index} = ",number * index) # 2 * 2 = 4
        index = index+1
        Table(number, lastNumber)


def App() : 
    print("Print Custome Table")
    number = int(input("Enter a number to print a table\n"))
    lastNumber = int(input("Enter last number to end table\n"))
    print("================================")
    Table(number, lastNumber)
App()