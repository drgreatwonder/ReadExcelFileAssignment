# -*- coding: utf-8 -*-
"""
Created on Sun May  3 21:14:59 2020

@author: Dr Great Wonder
"""


import pandas as pd
from pandas import DataFrame

excelsheet = pd.ExcelFile("excelfile.xlsx")

loadjobs = excelsheet.parse("jobs")
loadcarmodels = excelsheet.parse("CarModels")
loadcitizensheet = excelsheet.parse("CitizenSheet")
loadschools = excelsheet.parse("Schools")
loadstudentreport = excelsheet.parse("StudentReport")
loadLaptopsInfo = excelsheet.parse("LaptopsInfo")
loaddrugproduction = excelsheet.parse("DrugProduction")
loaddrugtrial = excelsheet.parse("DrugTrial")
loadexportinfo = excelsheet.parse("ExportInfo")
loadpopulations = excelsheet.parse("Populations")


print(loadjobs, "\n")
print(loadcarmodels, "\n")
print(loadcitizensheet, "\n")
print(loadschools, "\n")
print(loadstudentreport, "\n")
print(loadLaptopsInfo, "\n")
print(loaddrugproduction, "\n")
print(loaddrugtrial, "\n")
print(loadexportinfo, "\n")
print(loadpopulations)