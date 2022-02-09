#Lab Tech Assistant 1.0
#Coder: Christopher J. Martino
#Date: October 28, 2021
#This will assist the Lab Tech with daily things like conversions, tasks list and other items

import datetime as dt
now = dt.datetime.now()

users = []

#Class contains code for displaying formatted time and date
class Timedate:
    def get_time():
        now = dt.datetime.now()
        return f"{now:%I:%M %p}"

    def get_date():
        now = dt.datetime.now()
        return f"{now:%A, %B %d, %Y}"

def task_list(add_item):
    with open("Tasks_List.txt", "a") as f:
        f.write("\n" + add_item)
        f.close()

print("Welcome to Lab Tech Assistant!")   
name = input("What's your name? \n")
users.append(name)
print("")

#This will determine the time of day and how it will respond to user
if now.hour < 12:
    print("Good Morning, " + name + "!")
elif now.hour < 18:
    print("Good Afternoon, " + name + "!")
elif now.hour >= 18:
    print("Good Evening, " + name + "!")
    
print("The current time is " + str(Timedate.get_time()) + " and todays date is " + str(Timedate.get_date()))
print('')
start_up = input("Would you like to access Scientific Assistant, " + name + "?\n")

while start_up == "yes" or start_up == "y":
#Menu items for LabTechAssistant
    print("-" * 60)
    print(f"{'1) Temperature Conversion':<8} {'2) Metric Conversion':<10} \n {'3) Task List':<9} {'4) Lab Book':<10} {'5) Access Task List':<0} {'6) Access Lab Book':<18} \n {'**Type Exit to Close Program**':<18}")
    print("-" * 60)
    choice = input("What would you like to do today, " + name + "? \n").lower()

    print("")

#This will give the Lab Tech a choice between converting between different types of temperature measurements: Celsius, Fahrenheit, Kelvin
    if choice == "1":
        temp_query = input("What temperature conversions would you like to do today? \n 1) Celsius to Fahrenheit 2) Fahrenheit to Celsius 3) Celsius to Kelvin 4) Fahrenheit to Kelvin \n")
        if temp_query == "1":
            cel_temp = input("What is the Celsius temperature that you wish to convert to Fahrenheit? \n")
            fah_conversion = (float(cel_temp) * 9 / 5) + 32
            cel_to_fah = round(fah_conversion, 6)
            print(f"{cel_temp} Celsius has been converted to {cel_to_fah} Fahrenheit.")
        if temp_query == "2":
            fah_temp = input("What is the Fahrenheit temperature that you wish to convert to Celsius? \n")
            cel_conversion = (float(fah_temp) - 32) * 5 / 9
            fah_to_cel = round(cel_conversion, 6)
            print(f"{fah_temp} Fahrenheit has been converted to {cel_conversion} Celsius.")
        if temp_query == "3":
            cel_temp2 = input("What is the Celsius temperature you would like to convert to Kelvin?\n")
            kel_conversion = (float(cel_temp2) + 273.15)
            cel_to_kel = round(kel_conversion, 6)
            print(f"{cel_temp2} Celsius has been converted to {cel_to_kel}.")
        if temp_query == "4":
            fah_temp2 = input("What is the Fahrenheit temperature that you wish to convert to Kelvin? \n")
            kel_conversion2 = (((float(fah_temp2) -32) * 5 ) / 9) + 273.15
            kel_to_cel = round(kel_conversion, 6) 
            print(f"{fah_temp2} Fahrenheit temperature has been converted to {kel_to_cel} Kelvin.")

#This will allow a user to perform various metric conversions.
    if choice == "2":
        metric_query = input("What metric conversions would you like to perform? \n 1) in to cm 2) cm to in 3) ft to meters 4) meters to feet 5) miles to km 6) km to miles \n")
        if metric_query == "1":
            in_conver = input("How many inches would you to convert to centimeters?\n")
            cm_conver = float(in_conver) * 2.54
            in_to_cm = round(cm_conver, 6)
            print(f"{in_conver} inches has been converted to {in_to_cm} centimeters.")
        if metric_query == "2":
            cm_conver2 = input("How many centimeters would you to convert to inches?\n")
            in_conver2 = float(cm_conver2) / 2.54
            cm_to_in = round(in_conver2, 6)
            print(f"{cm_conver2} centimeters has been converted to {cm_to_in} inches.")
        if metric_query == "3":
            ft_conver = input("How many feet would you like to convert to meters? \n")
            m_conver = float(ft_conver) / 3.281
            ft_to_m = round(m_conver, 6)
            print(f"{ft_conver} feet has been converted to {ft_to_m} meters.")
        if metric_query == "4":
            m_conver2 = input("How many meters would you like to convert to feet? \n")
            ft_conver2 = float(m_conver2) * 3.281
            m_to_ft = round(ft_conver2, 6)
            print(f"{m_conver2} meters has been converted to {m_to_ft} feet.")
        if metric_query == "5":
            mile_conver = input("How many miles would you like to convert to kilometers? \n")
            km_conver = float(mile_conver) * 1.609344
            miles_to_km = round(km_conver, 6)
            print(f"{mile_conver} miles has been converted to {miles_to_km} kilometers.")
        if metric_query == "6":
            km_conver2 = input("How many kilometers would you like to convert to miles? \n")
            miles_conver2 = float(km_conver2) / 1.609344
            km_to_miles = round(miles_conver2, 6)
            print(f"{km_conver2} kilometers has been converted to {km_to_miles} miles.")

#Allows user to add dated tasks to a list. Side note: Figure out how to make program create new text document, but once created not have it over written.
    if choice == "3":
        task_file = open("Tasks_List.txt", "a")
        
        question = input("Would you like to add anything to this? Y/N \n").lower()
    
        while question == "y":
            task_file.write(str(Timedate.get_date()) + " " + str(Timedate.get_time()) + "\n")
            add_item = input("What would you like to add? \n")
            task_file.write(add_item + "\n")
            question = input("Would like to add anything else to the list? Y/N \n").lower()
            if question == "n":
                break

    
#Allows a user to create a lab book of experiments
    if choice == "4":
        lab_book = open("Lab_Book.txt", "a")
        lab_book.write(str(Timedate.get_date()) + " " + str(Timedate.get_time()) + "\n")
        lab_book.write("Experiment Name: ")
        experiment_name = input("Enter Experiment Name\n")
        lab_book.write(experiment_name + "\n")
        lab_book.write("\n")
        lab_book.write("Procedure: ")
        exp_procedure = input("Type the procedures used for this experiment\n")
        lab_book.write(exp_procedure + "\n")
        lab_book.write("\n")
        lab_book.write("Data: ")
        data = input("Type the data of the experiment\n")
        lab_book.write(data + "\n")
        lab_book.write("\n")
        lab_book.write("Results: ")
        results = input("Type the results of the experiment\n")
        lab_book.write(results + "\n")
        lab_book.write("\n")
    
#Allows a user to access task list
    if choice == "5":
        task_file = open("Tasks_List.txt", "r")
        print(task_file.read())
    
#Allows a user to access task list
    if choice == "6":
        lab_file = open("Lab_Book.txt", "r")
        print(lab_file.read())
        
    if choice == "exit":
        break