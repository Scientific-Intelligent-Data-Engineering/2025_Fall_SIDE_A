#Q1
def add_values(a, b=1,c=2):
    return a+b+c

print(add_values(1,2,3))
print(add_values(1))

#Q2
def check_range(n):
    if(n >= -2 and n <= 5):
        return "True"
    else:
        return "False"

print(check_range(n=3))
print(check_range(n=10))

#Q3
def product_values(n):
    mul = 1
    for i in n:
        mul *= i
    return mul

a = [1,2,3]
v = product_values(a)
print(v)

#Q4
def get_even(n):
    li = []
    for i in n:
        if(i % 2 == 0):
            li.append(i)
    return li

print(get_even([0,1,2,3,4]))

#Q5
def clac(a):
    for i, ch in enumerate(a):
        if(ch == '+'):
            return int(a[:i]) + int(a[i+1:])
        elif(ch == '-'):
            return int(a[:i]) - int(a[i+1:])
        elif(ch == 'x'):
            return int(a[:i]) * int(a[i+1:])
        elif(ch == '/'):
            return int(a[:i]) / int(a[i+1:])

print(clac('1+2'))
print(clac('1-2'))
print(clac('2x3'))
print(clac('3/2'))

#Q6
def sort_str(a):
    li = a.split("-")
    return sorted(li)

name = 'Data-Science-and-Business-Analytics'
print(sort_str(name))

#Q7
def convert_input(a):
    try:
        return int(a)
    except ValueError:
        try:
            return float(a)
        except ValueError:
            return a

a = 'text'
print(convert_input(a))
a = '223'
print(convert_input(a))
a = '223.1234'
print(convert_input(a))
a = '0223'
print(convert_input(a))

#Q8
def all_add(*args):
    return sum(args)

print(all_add(1,2))
print(all_add(1,2,3,4))

#Q9
def count_upper_lower_char(a):
    upcnt = 0
    lowcnt = 0

    for i in a:
        if(i.isupper()):
            upcnt += 1
        elif(i.islower()):
            lowcnt += 1
    return upcnt, lowcnt

print(count_upper_lower_char("Data Science"))

#Q10
def get_unique(a):
    return [x for x in a if a.count(x) == 1]

print(get_unique(['A','A','B','C','D','D']))

#Q11
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def calc_area(self):
        return self.height * self.width
    
    def clac_perimeter(self):
        return 2*(self.width+self.height)
    
rec = Rectangle(height=3, width=5)
print(rec.calc_area())
print(rec.clac_perimeter())

#Q12
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, in0):
        self.balance += in0
    def withdraw(self, out0):
        if(self.balance < out0):
            print("잔액 부족")
        else:
            self.balance -= out0
    
    def get_balance(self):
        return self.balance

class SavingAccount(BankAccount):
    def __init__(self,owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

account1 = BankAccount("이재옹", 1000)
account1.deposit(500)
account1.withdraw(200)
print("잔액: ", account1.get_balance())

account2 = SavingAccount("이제용", 2000, 0.05)
account2.add_interest()
print("잔액: ", account2.get_balance())

#Q13
class Calculator:
    def __init__(self, value=0, stack=False):
        self.value = value
        self.stack = stack

    def _add(self, num):
        self.value += num
        return self.value

    def _minus(self, num):
        self.value -= num
        return self.value

    def _mul(self, num):
        self.value *= num
        return self.value

    def _div(self, num):
        self.value /= num
        return self.value

    def calc(self, expr: str):
        expr = expr.strip()

        if not self.stack:
            for i, ch in enumerate(expr):
                if ch in "+-*/":
                    left  = int(expr[:i])
                    right = int(expr[i+1:])
                    if   ch == '+': self.value = left + right
                    elif ch == '-': self.value = left - right
                    elif ch == '*': self.value = left * right
                    elif ch == '/': self.value = left / right
                    self.stack = True
                    result_str = f"{left} {ch} {right} = {self.value}"
                    print(result_str)
                    return result_str

        else:
            op, num = expr[0], int(expr[1:])
            before = self.value
            if   op == '+': self._add(num)
            elif op == '-': self._minus(num)
            elif op == '*': self._mul(num)
            elif op == '/': self._div(num)
            result_str = f"{int(before)} {op} {num} = {self.value}"
            print(result_str)
            return result_str

    def clear(self):
        self.value = 0
        self.stack = False


calculator = Calculator()
calculator.calc('2+3')
calculator.calc('/5')
calculator.clear()
print(calculator.value)