class Employee:

    raise_amt = 2.5

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 5.5

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


    pass

dev_1 = Developer('mat', 'pat', 10, "python") # this effects a subclass not the parent class
dev_2 = Developer('lar', 'bar', 20, "ruby") # this effects a subclass not the parent class
dev_3 = Employee('gar', 'bat', 30) # this effects parent class

print (dev_1.email)
print (dev_1.prog_lang)
# print (help(Developer)) # this tells us which attributes python tried to search through to find what youre looking for

print (dev_1.pay)
dev_1.apply_raise()
print (dev_1.pay)