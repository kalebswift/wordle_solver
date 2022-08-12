#####################
# imports and setup #
#####################
import itertools

# get text
with open('words.txt', 'r') as f:
    vocab = [word.strip('\n') for word in f.readlines()]

##################
# function setup #
##################


# get all eligible words given a guess, pattern and corpus
def next_words(guess, pattern, corpus):
    greens = [guess[i] for i in range(len(guess)) if pattern[i] == 'g']
    yellows = [guess[i] for i in range(len(guess)) if pattern[i] == 'y']
    greys = set([guess[i] for i in range(len(guess)) if pattern[i] == '-'])
    for i in range(len(pattern)):
        code = pattern[i]
        letter = guess[i]
        if code == 'g':
            corpus = [word for word in corpus if word[i] == letter] # only take words with same greens
            print('\ngreen check', letter)
            for word in corpus:
                print(word)
        if code == 'y':
            corpus = [word for word in corpus if word[i] != letter]  # remove words with unmoved yellows
            print('\nyellow check', 1, letter)
            for word in corpus:
                print(word)
            # make sure words have enough of yellow characters
            count = len([l for l in greens + yellows if l == letter])
            required_amount = lambda g, l, c: True if len([let for let in g if let == l]) >= c else False
            corpus = [word for word in corpus if required_amount(word, letter, count)]
            print('\nyellow check', 2, letter)
            for word in corpus:
                print(word)
        if code == '-':
            # make sure words don't have more than the permitted amount of a greyed letter
            count = len([letter for letter in greens + yellows if letter == guess[i]])
            allowed_amount = lambda g, l, c: True if len([let for let in g if let == l]) <= c else False
            corpus = [word for word in corpus if allowed_amount(word, letter, count)]
            print('\ngrey check', letter)
            for word in corpus:
                print(word)
    return corpus


# determine the probability of a pattern occurring for a guess in a corpus
def pattern_probability(guess, pattern, corpus):
    pass


# main script
if __name__ == '__main__':
    # input patterns with the following rules
    # - green: "g"
    # - yellow: "y"
    # - grey: "-"
    tmp_vocab = ['helps', 'trots', 'mists', 'pully', 'phlem', 'minty']
    tmp_guess = 'print'
    tmp_pattern = '--yyy'
    print(next_words(tmp_guess, tmp_pattern, tmp_vocab))