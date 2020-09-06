import os
import csv

#set the file path
budget_path = os.path.join("Resources","PyBank_Resources_budget_data.csv")

#open file
with open(budget_path) as file:
    
    reader = csv.reader(file,delimiter = ",")

    #reader header
    header = next(reader)

    total_months = 0
    net_total_amount = 0
    #create a months list
    month_list = []

    #create a profit/loss list
    profit_loss_list = []
    
    for row in reader:
        total_months += 1
        net_total_amount += int(row[1])
        
        month_list.append(row[0])
        profit_loss_list.append(row[1])

    #print(f'month list is {month_list}')

    #calculate total change of each month
    total_change = 0.0
    change_list = []
    for i in range(1,len(profit_loss_list)):
        total_change += float(profit_loss_list[i]) - float(profit_loss_list[i-1])
        change_list.append(float(profit_loss_list[i]) - float(profit_loss_list[i-1]))

    average_change = round(total_change / (total_months - 1),2)
  

    #find the greatest increase value
    greatest_increase_value = int(max(change_list))
    #find the greaatest decrease value
    greatest_decrease_value = int(min(change_list))



    #find the locations for both
    greatest_increase_location = change_list.index(max(change_list)) + 1
    greatest_decrease_location = change_list.index(min(change_list)) + 1

    #find the months for both
    greatest_increase_month = month_list[greatest_increase_location]
    greatest_decrease_month = month_list[greatest_decrease_location]



    #print to the ternimal
    print("Financial Analysis")
    print("----------------------")
    print(f'Total Months: {total_months}')
    print(f'Total: ${net_total_amount}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {greatest_increase_month} ({greatest_increase_value})')
    print(f'Greatest Decrease in Loss: {greatest_decrease_month} ({greatest_decrease_value})')

     
    #set output path
    output_path = os.path.join("analysis","financial analysis.csv")

    #open with write mode
    with open(output_path,'w',newline='') as output_file:
        writer = csv.writer(output_file, delimiter = ",")

        writer.writerow(['Financial Analysis'])
        writer.writerow(["----------------------"])
        writer.writerow([f'Total Months: {total_months}'])
        writer.writerow([f'Total: ${net_total_amount}'])
        writer.writerow([f'Average Change: ${average_change}'])
        writer.writerow([f'Greatest Increase in Profits: {greatest_increase_month} ({greatest_increase_value})'])
        writer.writerow([f'Greatest Decrease in Loss: {greatest_decrease_month} ({greatest_decrease_value})'])





    
    
    
