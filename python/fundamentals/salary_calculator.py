#!/usr/bin/env python3
"""
Salary Calculator

This program calculates an employee's weekly salary using
the hourly rate and total hours worked.
"""

employee_name = input("Enter employee name: ")
hourly_rate = float(input("Enter hourly rate: "))
hours_worked = float(input("Enter hours worked this week: "))

weekly_salary = hourly_rate * hours_worked
monthly_estimate = weekly_salary * 4

print("\nSalary Summary")
print("--------------")
print(f"Employee: {employee_name}")
print(f"Hourly Rate: ${hourly_rate:.2f}")
print(f"Hours Worked: {hours_worked}")
print(f"Weekly Salary: ${weekly_salary:.2f}")
print(f"Estimated Monthly Salary: ${monthly_estimate:.2f}")
