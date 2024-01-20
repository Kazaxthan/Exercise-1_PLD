#exercise 1 

number_1 =  int(input("Enter number 1:"))
number_2 =  int(input("Enter number 2:"))

def enter(number_1 ,number_2):

    product = number_1 * number_2

    if product <=1000:
        return product
    else:
        return number_1 + number_2

result =  enter(number_1, number_2)
print ("the result is", result)

    


