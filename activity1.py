# -*- coding: utf-8 -*-
import pandas as pd

file = pd.read_csv('C:\\Users\\meifl\\Desktop\\UCIRV201804DATA3-Class-Repository-DATA\\01-LessonPlan\\03-Python\\3\\Activities\\Unsolved\\01-Stu_CerealCleaner\\Resources\\cereal.csv', header = None)

print(file[0][file[7] >= 5])


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

file1 = pd.read_csv('C:\\Users\\meifl\\Desktop\\UCIRV201804DATA3-Class-Repository-DATA\\01-LessonPlan\\03-Python\\3\\Activities\\Unsolved\\01-Stu_CerealCleaner\\Resources\\cereal_bonus.csv')

print(file1['name'][file1['fiber'] >= 5])
