#Day-5-1: Average Height
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
i = 0
sum = 0
for student_height in student_heights:
  sum += student_height
  i += 1
average_height = round(sum / i)
print(average_height)

#180 124 165 173 189 169 146

#Day-5-2: High Score
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
max = 0
for student_score in student_scores:
  if student_score > max:
    max = student_score
print(f"The highest score in the class is: {max}")
#78 65 89 86 55 91 64 89

#Day-5-3:  Adding Even Numbers
#Write your code below this row 👇
sum_of_even = 0
for number in range(2,101,2):
  sum_of_even += number
print(sum_of_even)

#Day-5-4:  The FizzBuzz Job Interview Question
#Write your code below this row 👇
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
  elif number % 3 == 0:
    print('Fizz')
  elif number % 5 == 0:
    print('Buzz')
  else:
    print(number)
  #print(number)
