# Newsela Assignment
Take home assignment: 

### Problem
_What words or phrases appear more frequently in questions that students tend to do poorly on, and what appear more frequently in questions that students do well on?_

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) and [virtualenv](https://virtualenv.pypa.io/en/latest/) to install dependences. 

```bash
virtualenv -p=python3.9 venv
python -m pip install -r requirements.txt
```

Depending on use of [nltk](https://www.nltk.org/) before you may have to start a python terminal for this function or else you'll get errors:
```python
import nltk
nltk.download('punkt')
```

## Usage

```shell
usage: common_phrases.py [-h] [-l LENGTH] [-ol OUTPUT_LIMIT]

Find common phrases in output file from Newsela

optional arguments:
  -h, --help            show this help message and exit
  -l LENGTH, --length LENGTH
                        Input for phrases with <length: int> words
  -ol OUTPUT_LIMIT, --output-limit OUTPUT_LIMIT
                        <output-limit: int> phrases with <length: int> will be outputed
```
Phrase length is default at 3 but you can use 4, 5, 6 to see any paterns.
Output limit is the number of phrases outputted in both correct and incorrect texts.
Example output of length, 5 and output limit, 10:
```shell
time python common_phrases.py -l 5 -ol 10
Correct: 6960
the sentence from the article: 673
read the sentence from the: 625
select the paragraph from the: 497
select the paragraph from ``: 299
which of the following is: 247
to include in a summary: 232
important to include in a: 230
include in a summary of: 225
the paragraph from the article: 222
the paragraph from the section: 219

Incorrect: 3231
select the paragraph from the: 400
the sentence from the article: 268
the paragraph from the article: 260
paragraph from the article that: 258
read the sentence from the: 249
select the paragraph from ``: 143
to include in a summary: 122
the paragraph from the section: 121
important to include in a: 119
include in a summary of: 111

real    0m12.703s
user    0m4.197s
sys     0m2.614s
```

## Process
I first wrote the script `count_words.py` but with an output like this, I knew I was in trouble.
```shell
time python count_words.py
Correct
the: 16253
of: 4851
article: 3248
to: 3219
that: 2828
is: 2640
in: 2568
from: 2489
a: 2489
sentence: 2227

Incorrect
the: 8526
of: 2467
article: 1832
that: 1752
from: 1477
to: 1434
a: 1231
in: 1202
is: 1058
which: 985

real    0m0.460s
user    0m0.223s
sys     0m0.049s
```

I knew I would have to make an exclusionary string list. But, that exclusionary test list I made had 25+ items of articles and prepositions. So, I approached it from another direction. I have never really worked in a domain where I would need to do this type of language processing, so I went to google and found a [decent solution](https://www.markhneedham.com/blog/2015/01/19/pythonnltk-finding-the-most-common-phrases-in-how-i-met-your-mother/) that is scalable and developed an extension to allow user input to increase or decrease phrase lengths. 