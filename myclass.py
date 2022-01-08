# class Student: 
#     def __init__(self, name, grade, marks):
#         self.name=name
#         self.grade=grade
#         self.marks=marks

#     def language(self, lang):
#         self.lang=lang
#         return f"{self.name} speaks {self.lang}"


# # creating the object
# student1= Student("Yuv", 10, "A+")
# #print(student1.name)
# print(student1.language("Punjabi"))

class Car:
    def __init__(self, model, fuelCapacity, year):
        self.model=model
        self.fuelCapacity=fuelCapacity
        self.year=year
    def changingOil(self, oil):
        self.oil=oil
        return f"{self.oil}"

car1 = Car("Dodge", "300 miles/hr", 2022)
print(car1.model)
print(car1.changingOil("Change"))