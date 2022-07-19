import csv
import os

#csvpath=os.path.join('budget_data.csv')
#with open(csvpath, encoding='utf-8') as csvfile:
#    budget=csv.reader(csvfile, delimiter=',')
#    print(budget)
with open('budget_data.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    budget = list(csv_reader)

number_list=[]
differ=[]
i=0
first=0
second=1
if first<len(budget):
    second=first+1
#print(budget)
print("Total months: "+str(len(budget)))
while i!=len(budget)-1:
    i=i+1
    number_list.append(int(budget[i][1]))
print("Total: $"+str(sum(number_list)))
avg=sum(number_list)/len(number_list)
print("Average change: $"+str(avg)) 
while first!=len(budget)-1:
    first=first+1
    if first<len(budget)-1:
        second=first+1
    differ.append(int(budget[second][1])-int(budget[first][1]))
print("Greatest increase in profits: " +budget[differ.index(max(differ))][0]+", "+str(max(differ)))
print("Greatest decrease in profits: " +budget[differ.index(min(differ))][0]+", "+str(min(differ)))
