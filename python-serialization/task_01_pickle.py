#!/usr/bin/python3
"""1.Pickling Custom Classes"""
import pickle


class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student
        # print(self.name)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """serialize information byte form to file"""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
                print(file)
        except Exception as e:
            print(f"Error during serialization: {e}")

    @classmethod
    def deserialize(cls, filename):
        """deserialize information from file"""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Erorr during deserialisatoin {e}")

# obj = CustomObject(name="John", age=25, is_student=True)
# print("Original Object:")
# obj.display()

# # Serialize the object
# obj.serialize("object.pkl")
