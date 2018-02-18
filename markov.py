import sys
import random

from string import ascii_lowercase

ALLOWED = ascii_lowercase+'0123456789\'%=/.'


def build_model(text):
    words = text.replace('\n', ' ').lower().split(' ')
    words = [word for word in words if word]
    model = {}
    for i, word in enumerate(words):
        word = ''.join(c for c in word if c in ALLOWED)
        if i == len(words) - 1 or word[-1] == '.':
            next_word = '.'
            word = word[:-1]
        else:
            next_word = ''.join(c for c in words[i+1] if c in ALLOWED)
            if len(next_word) > 0 and next_word[-1] == '.':
                next_word = next_word[:-1]
     
        if word not in model:
            model[word] = {}

        next_states = model[word]

        try:
            next_states[next_word] += 1
        except KeyError:
            next_states[next_word] = 1

    return model


def get_sentence(model, seed):
    seed = seed.lower()
    if seed not in model:
        return seed

    sentence = [seed]
    while seed != '.':
        seed = get_next_word(model[seed])
        sentence.append(seed)

    return ' '.join(sentence[:-1]).capitalize() + '.'


def get_next_word(possible):
    total = sum(possible.values())
    selection = random.randrange(0, total)
    possible = list(possible.items())
    for word in possible:
        selection -= word[1]
        if selection <= 0:
            return word[0]


meat_model = build_model(open('training.txt', 'r').read())
print(get_sentence(meat_model, sys.argv[1]))
