import csv
import random

firstNames = ["June", "Tom", "Vikram", "Vanessa", "Theo", "Priti", "Ken", "Melissa", "Gunter", "Alison", "John", "Victoria", "Prasad", "Anu", "Aditya", "Tara", "Connor", "Jen", "Raheem", "George", "Marie"]
lastNames = ["Cunningham", "Ford", "Karumbunathan", "Welsh", "Hawley", "Kohler", "Nair", "Zhang", "Lenga", "Peterson", "Bekishhov", "Wong", "Williams", "Reuben", "Stirling", "Rashford", "Russell"]
countries = ["USA", "UK", "India", "Germany", "Japan", "Canada", "France", "Sweden", "France", "South Africa", "Australia"]

companyNames = []
with open('companies.csv') as csvfile:
  companies = csv.reader(csvfile)
  line_count = 0
  for row in companies:
    if line_count != 0:
      companyNames.append(row[0])
    line_count += 1

users = []
emails = []


for company in companyNames:
  userCount = random.randint(10,25)
  for x in range(userCount):
    firstName = firstNames[random.randint(0, len(firstNames))-1]
    lastName = lastNames[random.randint(0, len(lastNames))-1]
    country = countries[random.randint(0,len(countries))-1]
    email = firstName.lower() + "." + lastName.lower() + "@" + company.lower() + ".com"
    users.append([firstName, lastName, email, country, company])
    emails.append([email])
public class AutomorphicNumberExample1  
{   
//user-defined static method that checks whether the number is automorphic or not   
static boolean isAutomorphic(int num)   
{   
//determines the square of the specified number  
int square = num * num;   
//comparing the digits until the number becomes 0  
while (num > 0)   
{   
//find the remainder (last digit) of the variable num and square and comparing them  
if (num % 10 != square % 10)   
//returns false if digits are not equal  
return false;   
//reduce num and square by dividing them by 10  
num = num/10;   
square = square/10;   
}   
return true;   
}   
//Driver code  
public static void main(String args[])   
{   
//number to be check      
//calling the method and prints the result accordingly  
System.out.println(isAutomorphic(76) ? "Automorphic" : "Not Automorphic");   
System.out.println(isAutomorphic(13) ? "Automorphic" : "Not Automorphic");   
}   
}  
Output 1:

with open('users.csv', mode='w') as user_file:
  user_writer = csv.writer(user_file)
  user_writer.writerows(users)

with open('emails.csv', mode='w') as email_file:
  email_writer = csv.writer(email_file)
  email_writer.writerows(emails)
