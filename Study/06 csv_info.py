import csv
#
# with open(r'employee.csv','r') as rf:
#     data=csv.reader(rf)
#     for row in data:
#         print(row[0], row[1],row[4])
#         print(len(row[0]))

with open(r'tech.csv','w',newline='') as wf:
    tech=csv.writer(wf)
    tech.writerow(["SN","Tech_Name","Exp"])
    tech.writerow([1,"Python",16])
    tech.writerow([2,"AIML",15])
    tech.writerows([[3,'BigData',11],[4,'Snowflakes',6]])