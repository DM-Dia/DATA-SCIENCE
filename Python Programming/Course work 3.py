from abc import ABC, abstractmethod

#TASK 1
class Person(ABC):
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Address: {self.address}"

    def greet(self, other):
        return f"Hello {other.name}! My name is {self.name}."

    @abstractmethod
    def introduce(self):
        pass

    @staticmethod
    def is_adult(age):
        return age >= 18

#TASK 2
class Employee(Person):
    _counter = 0  # Ensure this is an integer

    def __init__(self, name, age, gender, address, salary):
        super().__init__(name, age, gender, address)
        Employee._counter += 1  # Increment the counter properly
        self.__employee_id = f"EMP{Employee._counter:02d}"
        self._salary = salary

    @property
    def employee_id(self):
        return self.__employee_id

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, amount):
        if amount > 0:
            self._salary = amount

    @classmethod
    def get_counter(cls):
        return cls._counter

    def introduce(self):
        return f"Hello, I am {self.name} and I work as an Employee. My ID is {self.employee_id}."

    def __del__(self):
        Employee._counter -= 1

#TASK 3
class Teacher(Employee):
    _counter = 0  # Counter for teachers

    def __init__(self, name, age, gender, address, salary, subjects):
        super().__init__(name, age, gender, address, salary)
        Teacher._counter += 1
        self.__teacher_id = f"TEC{Teacher._counter:02d}"
        self.subjects = subjects if subjects else []

    @property
    def teacher_id(self):
        return self.__teacher_id

    @property
    def employee_id(self):
        raise AttributeError(f"{self.__class__.__name__} object has no attribute 'employee_id'")

    @classmethod
    def get_counter(cls):
        return cls._counter

    def add_subject(self, subject):
        if subject not in self.subjects:
            self.subjects.append(subject)

    def remove_subject(self, subject):
        if subject in self.subjects:
            self.subjects.remove(subject)

    def introduce(self):
        return f"Hello, I am {self.name}. My ID is {self.teacher_id}, and I teach {', '.join(self.subjects)}."

    def __del__(self):
        Teacher._counter -= 1

# Testing
if __name__ == "__main__":
    teacher1 = Teacher("A", 30, "Female", "123 St", 60000, ["Math", "Physics"])
    teacher2 = Teacher("B", 35, "Male", "456 St", 55000, ["English", "History"])

    print(teacher1.introduce())
    print(teacher2.introduce())

    print(teacher1.greet(teacher2))
    print(f"Is {teacher1.name} an adult? {Person.is_adult(teacher1.age)}")