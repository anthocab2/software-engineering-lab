#!/usr/bin/env python3
"""
Grade Average Calculator

This program calculates the average grade from three scores.
It practices input, type conversion, arithmetic, and formatted output.
"""

student_name = input("Enter student name: ")

grade_one = float(input("Enter first grade: "))
grade_two = float(input("Enter second grade: "))
grade_three = float(input("Enter third grade: "))

average = (grade_one + grade_two + grade_three) / 3

print("\nGrade Summary")
print("-------------")
print(f"Student: {student_name}")
print(f"Grade 1: {grade_one:.2f}")
print(f"Grade 2: {grade_two:.2f}")
print(f"Grade 3: {grade_three:.2f}")
print(f"Average Grade: {average:.2f}")
