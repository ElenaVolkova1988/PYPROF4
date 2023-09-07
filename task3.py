""" Возьмите задачу о банкомате из семинара 2. Разбейте её 
на отдельные операции — функции. Дополнительно сохраняйте 
все операции поступления и снятия средств в список. """

from decimal import Decimal

                                # Пополнение
MULTIPLICITY = 50 
balans = 0
STEP = 3
TAX = Decimal (0.1) # децемал поставить для плавающей точки
sum = 5000000
all_operations=[]

x = int(input("Введите сумму для пополнения счета : "))

def add_sum(x): 
    if x >= MULTIPLICITY and x% MULTIPLICITY == 0:
        balans+=x
        all_operations.append(x)
        print(f"Ваш баланс: {balans}")
    else:
        print("Сумма пополнения должна быть кратна 50")
        print(f"Ваш баланс : {balans}")
      
  
                                 # Снятие 
def take_sum(int):                                
    y = int(input("Введите сумму для снятия со счета : "))
    if y > balans:
        print(f"На вашем счете недостаточно средств!")
        print(f"Ваш баланс : {balans}")
    elif y >= MULTIPLICITY and y% MULTIPLICITY == 0:
        balans -=y
        all_operations.append(y)
        print(f"Ваш баланс: {balans}")
    else:
        print("Сумма пополнения должна быть кратна 50")
        print(f"Ваш баланс : {balans}")

def charge (int):
    if balans > sum :
        z = take_sum * TAX
        balans -= z
        all_operations.append(z)
        print(f"Ваш баланс c учетом налога на богатство: {balans}")
    
print(all_operations)    