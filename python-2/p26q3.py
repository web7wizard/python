import csv

with open('red.csv','w',newline='') as mfile:
    writer=csv.writer(mfile)
    writer.writerow(['rollno','name','grade'])
    writer.writerow(['2501','jiya','destinction'])
    writer.writerow(['2502','amina','destinction'])

with open (r"red.csv") as myfile:
    read_csv=csv.reader(myfile)
    for lines in read_csv:
        print(lines)

