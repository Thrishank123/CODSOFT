class Calculator:
    def addition(self,a,b):
        return a+b
    def subtraction(self,a,b):
        return a-b
    def mulplication(self,a,b):
        return a*b
    def division(self,a,b):
        return a/b

def display_menu():
    print("Menu".center(24,"-"))
    print("What do you want to perform ")
    print("1.Addition\n2.Subtaction\n3.Multiplication\n4.Division")


def main():
    calculator=Calculator()
    display_menu()
    choice=int(input("Enter choice : "))
    match choice:
        case 1:
            a=int(input("Enter number 1 : "))
            b=int(input("Enter number 2 : "))
            print("Sum :",calculator.addition(a,b))
        case 2 :
            a=int(input("Enter number 1 : "))
            b=int(input("Enter number 2 : "))
            print("Subtraction :",calculator.subtraction(a,b))
        case 3 :
            a=int(input("Enter number 1 : "))
            b=int(input("Enter number 2 : "))
            print("Multiplication :",calculator.mulplication(a,b))
        case 4:
            a=int(input("Enter number 1 : "))
            b=int(input("Enter number 2 : "))
            print("Division :",round(calculator.division(a,b),2))
        case _:
            print("Invalild Choice !")


if __name__=="__main__":
    main()

