class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __repr__(self):
        return f'{self.name} is {self.age} years old'   
    
input_data={}

input_data['name']= input('what is your name? ')
input_data['age']= input('what is your age? ')

person=Person(input_data['name'],input_data['age'])

print(person)
print(input_data)

