import csv
import os
with open('election_data.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    poll = list(csv_reader)
total=len(poll)
can1=0
can2=0
can3=0
can4=0
winner=0
i=1
print("-------------------------")
print("Election results: ")
print("-------------------------")
print("Total votes: "+str(total))
print("-------------------------")
while i!=len(poll)-1:
    i=i+1
    if poll[i][2]=="Khan":
        can1=can1+1
i=1
while i!=len(poll)-1:
    i=i+1
    if poll[i][2]=="Correy":
        can2=can2+1
i=1
while i!=len(poll)-1:
    i=i+1
    if poll[i][2]=="Li":
        can3=can3+1
i=1
while i!=len(poll)-1:
    i=i+1
    if poll[i][2]=="O'Tooley":
        can4=can4+1
print("Khan: "+str(can1/len(poll)*100)+"% ("+str(can1)+")")
print("Correy: "+str(can2/len(poll)*100)+"% ("+str(can2)+")")
print("Li: "+str(can3/len(poll)*100)+"% ("+str(can3)+")")
print("O'Tooley: "+str(can4/len(poll)*100)+"% ("+str(can4)+")")
candidate_num=(can1, can2, can3, can4)
candidates=("Khan","Correy","Li","O'Tooley")
winner=candidates[candidate_num.index(max(candidate_num))]
print("-------------------------")
print("The winner is "+winner+" at "+str(max(candidate_num)/len(poll))+"%.")
print("-------------------------")

with open('poll_output.txt', 'w') as Poll_results:
    Poll_results.write("-------------------------\n")
    Poll_results.write("Election results: \n")
    Poll_results.write("-------------------------\n")
    Poll_results.write("Total votes: "+str(total)+"\n")
    Poll_results.write("-------------------------\n")
    Poll_results.write("Khan: "+str(can1/len(poll)*100)+"% ("+str(can1)+")\n")
    Poll_results.write("Correy: "+str(can2/len(poll)*100)+"% ("+str(can2)+")\n")
    Poll_results.write("Li: "+str(can3/len(poll)*100)+"% ("+str(can3)+")\n")
    Poll_results.write("O'Tooley: "+str(can4/len(poll)*100)+"% ("+str(can4)+")\n")
    Poll_results.write("-------------------------\n")
    Poll_results.write("The winner is "+winner+" at "+str(max(candidate_num)/len(poll))+"%.\n")
    Poll_results.write("-------------------------\n")