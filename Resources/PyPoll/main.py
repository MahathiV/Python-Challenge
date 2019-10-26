#create file paths across operating systems - import the os module
import os
#To read CSV Files
import csv

total_votes = 0     # Variable that stores total number of votes in the csv file 

#voter_id_list = []

candidate_list = []    # Empty list to store all candidates from candidates column when reading elections data

candidate_list_sorted = []  # Sorting the candidate_list in alphabetical order using 'sorted' function in lists to get vote count.

candidate_list_unique = []  # list to store unique candidates list - one time apperance

count_vote_list = []   # list that stores votes count all candidates from candidate_list_sorted 

# Relative path - collects data from election_data.csv in Downloads folder
#Election_analysis = os.path.join('..','..','Downloads','election_data.csv')

#Election_analysis = os.path.join('..','..','Downloads','election_data.csv')
Election_analysis = os.path.join('..','..','Resources','election_data.csv')

#Read the CSV File 

with open(Election_analysis,'r') as csvfile:    #Plain Reading of CSV files
     
     read_csv = csv.reader(csvfile, delimiter=',')   #Splitting data through delimiter comma

     header = next(read_csv)        # next - moves cursor down

     for row in read_csv:           # Reading each row in the file

         total_votes=total_votes + 1       # counting the total number of votes through voter ids
         #voter_id_list.append(int(row[0]))
         candidate_list.append(row[2])   # adding all the candidates in the file to the list candidate_list
     
     
     candidate_list_sorted = sorted(candidate_list)   # using sorted function to put in alphabetical order

     for i in candidate_list_sorted:         
          if i not in candidate_list_unique:
              candidate_list_unique.append(i)      # Preparing Unique Candidate List
              count_vote_list.append(1)            # Preparing vote count for unique candidate
          else:
              set_index = candidate_list_unique.index(i)      # setting index for vote count list if there is more than 1 apperance of candidate
              count_vote_list[set_index] = count_vote_list[set_index] + 1             
            
     vote_percent_list = []
     vote_percent_list=[round((100*i/total_votes),3) for i in count_vote_list]   # calculating percentage of votes each candidate won , using round function to 3 digits    
     

     maxi=0       # To store Maximun value and get election winners name
     winner = ""  # To store Winner's name
     for i in range(len(count_vote_list)):
         if maxi < count_vote_list[i]:
             maxi=count_vote_list[i]
             winner=candidate_list_unique[i] 
     
     #print(vote_percent_list)
     
     #print(candidate_list_unique)

     #print(count_vote_list)
     
     # Sorting the candidate names using vote count as index in ascending order
     new_candidate_sort = []
     new_candidate_sort = [candidate_list_unique for count_vote_list, candidate_list_unique in sorted(zip(count_vote_list, candidate_list_unique))]

     #print(new_candidate_sort)

     count_vote_sort = []
     count_vote_sort = sorted(count_vote_list)

     #print(count_vote_sort)

     vote_percent_sort = []
     vote_percent_sort = sorted(vote_percent_list)

     #print(vote_percent_sort)

     # Displaying output at the terminal

     print(" ")
     print(f"Election Results")
     print(" ")
     print("--------------------------------------")
     print(" ")
     print(f"Total Votes : {str(total_votes)}")
     print("--------------------------------------")

     # Looping in descending order as lists are in ascending order to display candidate names , vote percentage and vote count

     for i in range(len(new_candidate_sort)-1,-1,-1):  
         #print (i)
         print(f"{new_candidate_sort[i]}:  {vote_percent_sort[i]}% ({count_vote_sort[i]})")

     print("--------------------------------------")
     print(f"Winner : {winner}")
     print("--------------------------------------")


     # Displaying Output in a Text File

     # Set variable for output file

     file_path = os.path.join('..','..','Resources','Election_Results.txt')
     with open(file_path,"w",newline="") as txt_result:    # writing all the results to the text file 'Election_Results.txt'
         txt_result.write("Election Results\n")
         txt_result.write("--------------------------------------\n")
         txt_result.write(f"Total Votes : {str(total_votes)}\n")
         txt_result.write("--------------------------------------\n")
         for i in range(len(new_candidate_sort)-1,-1,-1):  
              txt_result.write(f"{new_candidate_sort[i]}:  {vote_percent_sort[i]}% ({count_vote_sort[i]})\n")
         txt_result.write(("--------------------------------------\n"))
         txt_result.write(f"Winner : {winner}\n")
         txt_result.write("--------------------------------------\n")