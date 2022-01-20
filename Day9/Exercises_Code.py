#Day-9-1: Grading Program
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    if 91 <= score:
        student_grades[student] = "Outstanding"
    elif 81 <= score:
        student_grades[student] = "Exceeds Expectations"
    elif 71 <= score:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"


# 🚨 Don't change the code below 👇
print(student_grades)

#Day-9-2: Dictionary in List
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_visited, number_of_visits, cities_visited):
    create_dictionary = {}
    create_dictionary["country"] = country_visited
    create_dictionary["visits"] = number_of_visits
    create_dictionary["cities"] = cities_visited
    travel_log.append(create_dictionary)



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
#print(travel_log)
#Print Humberg
print(travel_log[1]["cities"][1])


