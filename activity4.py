# -*- coding: utf-8 -*-
p = 'C:\\Users\\meifl\\Desktop\\UCIRV201804DATA3-Class-Repository-DATA\\01-LessonPlan\\03-Python\\3\\Activities\\Unsolved\\04-Stu_Email\\Resources\\employees.csv'

import csv

with open('C:\\Users\\meifl\\Desktop\\UCIRV201804DATA3-Class-Repository-DATA\\01-LessonPlan\\03-Python\\3\\Activities\\Unsolved\\04-Stu_Email\\output\\employee emails.csv', 'w', newline='') as csvfile:
    file1 = csv.DictReader(open(p))
    fieldnames = ['First Name', 'Last Name', 'SSN', 'Emails']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)   
    writer.writeheader()
    for row in file1:
        writer.writerow({'First Name': row['First Name'], 'Last Name': row['Last Name'], 'SSN': row['SSN'], 'Emails': (row['First Name'] + '.' + row['Last Name'] + '@example.com')})
    
    
    
    
    
    
    
# =============================================================================
# file1 = csv.DictReader(open(p))
# 
# new_employee_data = []
# 
# for row in file1:
#     new_employee_data.append(row['First Name'] + '.' + row['Last Name'] + '@example.com')
# 
# =============================================================================
