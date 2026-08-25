#!/usr/bin/env python3
"""
Employee Information Program

This program collects basic employee information from the user
and displays it in a clean formatted summary.
"""

name = input("Enter employee name: ")
position = input("Enter employee position: ")
department = input("Enter department: ")
age = int(input("Enter employee age: "))
years_experience = int(input("Enter years of experience: "))

print("\nEmployee Summary")
print("----------------")
print(f"Name: {name}")
print(f"Position: {position}")
print(f"Department: {department}")
print(f"Age: {age}")
print(f"Years of Experience: {years_experience}")
