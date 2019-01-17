import random
import string
import sys

thesaurus = {}
with open("words.txt") as words:
    for syn in words:
        syns = syn[:-1].split(",")
        word = syns[0]

        thesaurus[word] = syns

forbidden = (
    'i',
    'you',
    'he',
    'she',
    'the',
    'a',
    'an',
    'is',
)

def substitute_2(word):
    if word == "":
        return ""
    ec = word[-1] if word[-1] in string.punctuation else ""
    if ec != "":
        word = word[:-1]
    if word.lower() in thesaurus and word.lower() not in forbidden:
        keys = thesaurus[word.lower()]
        values = [len(syn) for syn in thesaurus[word.lower()]]

        f = random.choices(keys, values)[0]
        if word[0].isupper():
            return f.title() if ec == "" else f.title() + ec
        else:
            return f.lower() if ec == "" else f.lower() + ec
    else:
        return word if ec == "" else word + ec

def smartassize(str, func=substitute_2):
    out = []
    for line in str.splitlines(keepends=False):
        out.append(" ".join(func(x) if random.random() > 0.5 else x for x in line.split(" ")))
    return "\n".join(out)

if __name__ == "__main__":
    in_ = sys.stdin.read()
    print(smartassize(in_, func=substitute_2))
