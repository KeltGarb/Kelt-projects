
import os
print(os.getcwd())
os.chdir(r"C:\Users\kelto\PycharmProjects")
print(os.getcwd())

with open('story project 2.txt', 'r') as file:
    story = file.read()
    print(story)

words = set()
start_of_word = -1
target_start ='<'
target_end ='>'

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

print(words)

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ":")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])
print(story)

