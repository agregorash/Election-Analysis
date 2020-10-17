# Election-Analysis

## Project Overview
Tom, a Colorado Board of Elections employee has given me the task of completing the election audit of a recent local congressional election.  

The following data was gathered and formatted for the election audit:

1. The total number of votes cast
2. A complete list of candidates who received votes
3. The percentage of votes each candidate won
4. The total number of votes each candidate won
5. The winner of the election based on popular vote
6. A complete list of the counties that cast votes
7. The percentage of total votes cast from each county
8. The total number of votes cast from each county
9. The county that cast the most votes

## Resources
- Data Source: [election_results.csv](https://github.com/agregorash/Election-Analysis/blob/main/Resources/election_results.csv)
- Software: Python 3.8.3, Visual Studio Code, 1.50.0

## Election-Audit Results
#### The analysis of the election show that:  

     -369,711 votes were cast in the election

#### The counties were:

     -Jefferson  

     -Denver

     -Arapahoe

#### -The county results were:

     -Jefferson: 10.5% of the total vote (38,855 votes)

     -Denver: 82.8% of the total vote (306,055 votes)

     -Arapahoe: 6.7% of the total vote (24,801 votes)

#### -Denver county had the most votes in the election with 306,055 votes, accounting for 82.8% of the total votes cast

#### -The candidates were:  

     -Charles Casper Stockham  
  
     -Diana DeGette  
  
     -Raymon Anthony Doane  
  
#### -The candidate results were  

     -Chalres Casper Stockham received  23.0% of the votes (85,213 total votes)  
  
     -Diana DeGette received 73.8% of the votes (272,829 total votes)  
  
     -Raymon Anthony Doane received 3.1% of the votes (11,606 total votes)  
  
#### -Diane DeGette won the election with 272,829 total votes, accounting for 73.8% of the popular vote

## Election-Audit Summary
As it can be seen, the [PyPoll_Challenge.py](https://github.com/agregorash/Election-Analysis/blob/main/PyPoll_Challenge.py) script effectively dissects the congressional election data from the [election_results.csv](https://github.com/agregorash/Election-Analysis/blob/main/Resources/election_results.csv) file and provides us with accurate election results in the text editor terminal, as well as, in the provided [election_analysis.txt](https://github.com/agregorash/Election-Analysis/blob/main/Analysis/election_analysis.txt) file. However, with some simple modifications this same script could be used to perform an election audit on local senatorial elections and other local elections such as city mayoral elections even if the election data was given in a different format.
#### Modifying the script
1. Update the file_to_load path and/or the file_ save_path on line 9 and line 11.
```
file_to_load = os.path.join('Folder_xyz', 'election_results_xyz.csv'
file_to_save = os.path.join("new_analysis", "new_election_analysis.txt")
```
2. If it is a mayoral election or a national election, change all variables throughout script to their appropriate name to give the reader a better context of what is happening 
For example, on line 21:
```
county_list = []
```
Change to:
```
district_list = []
```
or
```
state_list = []
```
3. If the file provided has the data in a different order or more/ less columns, be sure to update the script to pull the data from the proper column.
For example, if the candidate names were in the 2nd column and the county names were in the 3rd column, make these changes to line 47 and 50
```
candidate_name = row[1]
county_name = row[2]
```
