import argparse
from ast import parse
import json
import re
import string

from collections import Counter

import nltk

# May need to download
#nltk.download('punkt')

def parse_args():
    parser = argparse.ArgumentParser(description='Find common phrases in output file from Newsela')
    parser.add_argument('-l', '--length', type=int, default=3,
                        help='Input for phrases with <length: int> words')
    parser.add_argument('-ol', '--output-limit', type=int, default=10,
                        help='<output-limit: int> phrases with <length: int> will be outputed')

    args = parser.parse_args()
    return args

# Untoken from nltk 
def untokenize(ngram):
    tokens = list(ngram)
    return "".join(
        [
            ' ' + i
            if not i.startswith("'") and i not in string.punctuation and i != "n't"
            else i
            for i in tokens
        ]
    ).strip()

# Counter with the extact phrases from nltk 
def extract_phrases(text: str, phrase_counter: Counter, length: int):
    for sent in nltk.sent_tokenize(text):
        strip_speaker = non_speaker.match(sent)
        if strip_speaker is not None:
            sent = strip_speaker.group(1)
        words = nltk.word_tokenize(sent)
        for phrase in nltk.ngrams(words, length):
            if all(word not in string.punctuation for word in phrase):
                phrase_counter[untokenize(phrase)] += 1

if __name__ == '__main__':

    args = parse_args()

    # Open file
    with open('data.json', 'r') as f:
        dic = json.load(f)


    # Clean for the <blockquote>
    regex = re.compile(r'<[^>]+>')
    # Clean for just letters 
    non_speaker = re.compile('[A-Za-z]+: (.*)')

    # Define correct and incorrect counters
    correct_phrase_counter = Counter()
    incorrect_phrase_counter = Counter()
    correct = 0
    incorrect = 0

    # Loop through items
    for item in dic:

        # Get item values
        percent_correct = item['percent_correct']
        text = regex.sub('', item['text'].lower())

        # If you want to see strings of n length change this parameter
        if percent_correct >= 0.50:
            extract_phrases(text, correct_phrase_counter, args.length)
            correct+=1
        else:
            extract_phrases(text, incorrect_phrase_counter, args.length)
            incorrect+=1

    print(f"Correct: {correct}")
    most_common_correct_phrases = correct_phrase_counter.most_common(args.output_limit)
    for k, v in most_common_correct_phrases:
        print(f'{k}: {v}')

    print(f"\nIncorrect: {incorrect}")
    most_common_incorrect_phrases = incorrect_phrase_counter.most_common(args.output_limit)
    for k, v in most_common_incorrect_phrases:
        print(f'{k}: {v}')
