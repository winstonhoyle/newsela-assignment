import json
import re

# Function so I dont have to write this 2x for correct/incorrect
def set_dict_items(dic: dict, cleaned_text: str):
    for word in cleaned_text:
        # Check if the word is already in dictionary
        if word in dic:
            # Increment count of word by 1
            dic[word] = dic[word] + 1
        else:
            # Add the word to dictionary with count 1
            dic[word] = 1

# Open file
with open('data.json', 'r') as f:
    dic = json.load(f)

# Create dictionaries to store words and their counts
word_dict = {}
correct_dict = {}
incorrect_dict = {}

for item in dic:

    # Get item values
    percent_correct = item['percent_correct']
    text = item['text'].lower()

    # Clean text using regex
    cleaned_text = [word for word in re.split('[^a-zA-Z]', text) if word]
    # Iterate over each word in line
    if percent_correct >= 0.50:
        set_dict_items(correct_dict, cleaned_text)
    # Incorrect items
    else:
        set_dict_items(incorrect_dict, cleaned_text)

# Sort the counts of the dictionary
correct_words = sorted([(value, key) for (key, value) in correct_dict.items() if value > 5], reverse=True)
incorrect_words = sorted([(value, key) for (key, value) in incorrect_dict.items() if value > 5], reverse=True)

print("Correct")
for count, word in correct_words[:10]:
    print(f'{word}: {count}')
print("\nIncorrect")
for count, word in incorrect_words[:10]:
    print(f'{word}: {count}')
