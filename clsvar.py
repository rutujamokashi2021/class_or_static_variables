# python program to show that the variable variables with a values assigne in class declaration,are class variables

# class fo computer science student
class CSStudent:
    stream = 'cse'

    def __int__(self, name, roll):
        self.name = name
        self.roll = roll


# object of csstudent class
a = CSStudent('rutuja', 101)
b = CSStudent('nilam', 102)
# prints "cse"
print(a.stream)
# prints "cse"
print(b.stream)
# print rutuja
print(a.name)
# print nilam
print(b.name)
# print 101
print(a.roll)
# print 102
print(b.roll)
print(CSStudent.stream)
a.stream = 'ece'
print(a.stream)  # prints 'ece'
print(b.stream)

CSStudent.stream = 'mech'

print(a.stream)  # prints 'ece'
print(b.stream)
