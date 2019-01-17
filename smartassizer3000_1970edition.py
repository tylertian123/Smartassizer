import json
import random
import sys
import string

with open("ea-thesaurus/ea-thesaurus.json") as f:
    thesaurus = json.load(f)

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

def substitute(word):
    if word == "":
        return ""
    ec = word[-1] if word[-1] in string.punctuation else ""
    if ec != "":
        word = word[:-1]
    if word.upper() in thesaurus and word.lower() not in forbidden:
        keys = [list(x.keys())[0] for x in thesaurus[word.upper()]]
        values = [int(list(x.values())[0]) for x in thesaurus[word.upper()]]

        f = random.choices(keys, values)[0]
        if word[0].isupper():
            return f.title() if ec == "" else f.title() + ec
        else:
            return f.lower() if ec == "" else f.lower() + ec
    else:
        return word if ec == "" else word + ec

def smartassize(str):
    out = []
    for line in str.splitlines(keepends=False):
        out.append(" ".join(substitute(x) for x in line.split(" ")))
    return "\n".join(out)

in_ = sys.stdin.read()

print(smartassize(in_))