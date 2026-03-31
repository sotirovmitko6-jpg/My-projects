while True:
    print("\n ---КАЛКУЛАТОР---")
    
    num = (input('Въведи число (или q за изход):'))
    
    if num == 'q':
        print('Край')
        break
    
    try:
        num = float(num)
    except:
        print('Трябва да въведеш число!')
        continue
    
    operation = (input('Въведи опетация (+, -, *, /, **): '))
    
    num2 = (input('Въведи второ число(или q за изход): '))
    
    if num2 == "q":
        print("Край")
        break
    
    try:
        num2 = float(num2)
    except:
        print("Трябва да въведеш число!")
        continue
        
    if operation == ("+"):
        result = num + num2
    elif operation == ("-"):
       result = num + num2
    elif operation == ("*"):
        result = num * num2
    elif operation == ("/"):
        result = num / num2
        if num2 == 0:
            result = ("Не можеш да делиш на 0!")
            
    elif operation == ("**"):
        result = num ** num2
    else:
        result = ("Невалидна операция!")
        
    print(result)