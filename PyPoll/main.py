import os
import csv

#set input path
input_path = os.path.join('Resources','election_data.csv')

#read csv file
with open(input_path) as inputfile:
    reader = csv.reader(inputfile,delimiter=",")

    header = next(reader)

    total_cast = 0
    candidates_list_original= []
    counter_Khan = 0
    counter_Correy = 0
    counter_Li = 0
    counter_Tooley = 0
    for row in reader:
        total_cast += 1
        candidates_list_original.append(row[2]) 
        if row[2] == "Khan": counter_Khan += 1 
        if row[2] == "Correy": counter_Correy += 1
        if row[2] == "Li": counter_Li += 1
        if row[2] == "O'Tooley": counter_Tooley += 1  


    #to get non-duplicated list
    candidates_list_edited = []
    for candidate in candidates_list_original:
        if candidate not in candidates_list_edited:
            candidates_list_edited.append(candidate)


    #to get each percentages
    percentage_Khan = "{:.3%}".format(counter_Khan / total_cast)
    percentage_Correy = "{:.3%}".format(counter_Correy / total_cast)
    percentage_Li = "{:.3%}".format(counter_Li / total_cast)
    percentage_oTooley = "{:.3%}".format(counter_Tooley / total_cast)

    #create a list of each counter
    counter_list = []
    counter_list.append(counter_Khan)
    counter_list.append(counter_Correy)
    counter_list.append(counter_Li)
    counter_list.append(counter_Tooley)

    #to find out the winner
    name_counter_dict = dict(zip(candidates_list_edited,counter_list))
    for name,counter in name_counter_dict.items():
        if counter == max(counter_list):
            winner = name
    
    #to print out the result
    print("Election Results")
    print("-------------------")
    print(f'Total Votes: {total_cast}')
    print("-------------------")
    print(f'{candidates_list_edited[0]}: {percentage_Khan} ({counter_Khan})')
    print(f'{candidates_list_edited[1]}: {percentage_Correy} ({counter_Correy})')
    print(f'{candidates_list_edited[2]}: {percentage_Li} ({counter_Li})')
    print(f'{candidates_list_edited[3]}: {percentage_oTooley} ({counter_Tooley})')
    print("-------------------")
    print(f'Winner: {winner}')
    print("-------------------")

    #set up output path
    output_path = os.path.join("analysis","election_results.csv")

    #write the results
    with open(output_path,'w') as csvoutput:
        writer = csv.writer(csvoutput,delimiter=",")

        writer.writerow(["Election Results"])
        writer.writerow(["-------------------"])
        writer.writerow([f'Total Votes: {total_cast}'])
        writer.writerow(["-------------------"])
        writer.writerow([f'{candidates_list_edited[0]}: {percentage_Khan} ({counter_Khan})'])
        writer.writerow([f'{candidates_list_edited[1]}: {percentage_Correy} ({counter_Correy})'])
        writer.writerow([f'{candidates_list_edited[2]}: {percentage_Li} ({counter_Li})'])
        writer.writerow([f'{candidates_list_edited[3]}: {percentage_oTooley} ({counter_Tooley})'])
        writer.writerow(["-------------------"])
        writer.writerow([f'Winner: {winner}'])
        writer.writerow(["-------------------"])
