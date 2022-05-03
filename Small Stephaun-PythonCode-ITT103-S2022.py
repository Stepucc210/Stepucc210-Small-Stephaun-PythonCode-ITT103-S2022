'''Author:Stephaun Small
Date Created: 28/4/2022
Course: ITT103
Purpose: A program that calculates and prints a salesperson's compensation. The application should handle an unknown number of salespeople before terminating with a specified input. The commission rate is determined by two factors: the amount of sales and the salesperson's class.'''


print('Print 0 in class for quit')
while 1:    
    clazz = int(input('Class: '))
    sales = int(input('Sales: '))
    commission=0
    rate=0
    if clazz == 0:
        print('Programm stopped')
        break
    elif clazz == 1:
        if sales <= 1000:
            rate=6
        elif sales > 1000 and sales < 2000:
            rate=7
        else:
            rate=10
    elif clazz == 2:
        if sales < 1000:
            rate=4
        else:
            rate=6
    elif clazz == 3:
        rate=4.5
    else:
        raise ValueError("Invalid class value. Class value should be between [1,3]")
    
    commission = sales*rate/100
    print(f'commission = {commission}')



