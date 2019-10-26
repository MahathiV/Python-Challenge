#create file paths across operating systems - import the os module
import os
#To read CSV Files
import csv

#List to store all dates column from csv file
dates_list = []
#List to store all profit and loss values column from csv file
total = []
#List to store changes in profit and loss in the entire period
change = []

# Relative path - collects data from budget_data.cvs in Downloads folder
#Financial_analysis = os.path.join('..','..','Downloads','budget_data.csv')
Financial_analysis = os.path.join('..','..','Resources','budget_data.csv')

#Read the CSV File 

with open(Financial_analysis,'r') as csvfile:    #Plain Reading of CSV files
     
     read_csv = csv.reader(csvfile, delimiter=',')   #Splitting data through delimiter comma

     header = next(read_csv)       # next - moves cursor down
     #read_csv.header
     
     for row in read_csv:
         
         dates_list.append(row[0])   # adding all values of column2, row index =0 to empty list 'dates_list'
         #number_of_months = number_of_months + 1
         total.append(int(row[1]))      # adding all the values of column2 , row index =1 to empty list 'total'

         
     for i in range(len(dates_list)-1):    #looping through 'total' list to add changes in profit/loss in the entire period
         change.append(total[i+1]-total[i])  # adding the differences to 'change' list
         greatest_increase = max(change)    # used the 'max' and 'min' List functions to get greatest increase and greatest decrease
         greatest_decrease = min(change)
         if change[i] == greatest_increase:
              date_increased=dates_list[i+1]    # getting the date for maximum change , storing the date in 'date_increased' variable
         if change[i] == greatest_decrease:
              date_decreased=dates_list[i+1]    # getting the date for minimum change , storing the date in 'date_decreased' variable

     average=round(sum(change)/(len(change)),2)   # calculating average of values in 'change' list
     

     # displaying the results to the terminal
     print(" ")
     print("Financial Analysis") 
     print(" ")
     print("--------------------------------------")
     print(" ")
     print(f"Total Months : {str(len(dates_list))}")
     print(f"Total : ${str(sum(total))}")     # using sum function to sum up all values in the list "total"
     print(f"Average Change: ${str(average)}")
     print(f"Greatest Increase in Profits: {str(date_increased)} (${str(greatest_increase)})")   
     print(f"Greatest Decrease in Profits: {str(date_decreased)} (${str(greatest_decrease)})")


     #displaying results to the text file

     #setting file path

     file_path = os.path.join("..","..","Resources","Financial_results.txt")
     with open(file_path,"w",newline="") as txt_result:
          txt_result.write(f"Financial Analysis\n")
          txt_result.write("--------------------------------------\n")
          txt_result.write(f"Total Months : {str(len(dates_list))}\n")
          txt_result.write(f"Total : $ {sum(total)}\n")
          txt_result.write(f"Average Change: ${str(average)}\n")
          txt_result.write(f"Greatest Increase in Profits: {str(date_increased)} (${str(greatest_increase)})\n") 
          txt_result.write(f"Greatest Decrease in Profits: {str(date_decreased)} (${str(greatest_decrease)})\n")
         