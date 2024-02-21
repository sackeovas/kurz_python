#1.Výpis prvních how_many přirozených čísel
def first_numbers(how_many): 
    for result in range(1,how_many+1): 
        print(result)

#2.Výpis všech sudých přirozených čísel menších než daná hranice upper_bound
def upper_bound(bound):
    number=2
    while number < bound:
        print (number)
        number+=2

#3.Výpis prvních how_many mocnin čísla base
def how_many(number,base): 
    for result in range(1,number+1):
        print(base**result)
    
#4.Výpis prvních how_many členů Fibonacciho posloupnosti
def fibonacci(how_many): 
    first_num=0
    second_num=1
    print (first_num)
    print (second_num)
    for result in range(how_many-2):
        third_num = first_num + second_num
        first_num = second_num
        second_num = third_num
        print(third_num)

              #???
    

        
#4.Výpočet faktoriálu
def factorial(number):
        """
        while
        decreased = number-1
        print(decreased)
        print(number*decreased)
        """
    
        result=1
        for x in range(2, number+1):
            result *= x
        if number < 0 or type(number) is float : #proč float nefunguje?
            print("Factorials exist only for natural numbers and 0")
        else:
            print(result)
              
#5.Test čísla na prvočíselnost pomocí postupného dělení
def prime_test(number):
    """
    if number < 2:
        return False
    elif number!=2 is True and number%2 == 0:
        return False
    elif number%3 == 0:
        return False
    elif number!=5 is True and number%5 == 0:
        return False
    elif number!=7 is True and number%7 == 0:
        return False
    elif number!=11 is True and number%11 == 0:
        return False
    else:
        return True
    print("Is the number prime?" + number)
    """
    for i in range(2,number):
        if number%i == 0:
            return False
    return True
    
#6.Vrácení počtu dělitelů daného čísla
    
#7.Test čísla na prvočíselnost s využitím předchozí funkce
#9.Výpis prvních how_many prvočísel
def how_many(amount):
    for number in range:
        pass

#Ciferní součet
#Výpis how_many náhodně vygenerovaných čísel, jejich minimum, maximum a průměr
