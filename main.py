import random
import pandas


new_list = []

for x in range(100):
    new_list.append(x)

new_numbers = [n + 100 for n in new_list]

print(new_numbers)

new_list = [n + n for n in range(1,5)]

print(new_list)




def int_list(f):
    with open(f) as txt_one:
        data = txt_one.readlines()
    list_ready = [int(sym.replace("\n", "")) for sym in data]
    return list_ready


file_one = int_list("file1.txt")

file_two = int_list("file2.txt")

new_list = [n for n in file_one if n in file_two]

print(new_list)

names = ["John", "Vanessa", "Milly", "Igor", "Vasiliy", "Peotr"]

students_scores = { key:random.randint(1,100) for key in names}
print(students_scores)

passed_students = {student:score for (student, score) in students_scores.items() if score > 60}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()
print(words)

new_words = { word:len(word) for word in sentence.split()}
print(new_words)









































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































