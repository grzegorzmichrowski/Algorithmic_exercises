import sys


def main():
    with open('anagrams.csv', 'r') as f:
        words = f.read().splitlines()

    sorted_words = []
    for word in words:
        sorted_word = ''.join(sorted(word))
        sorted_words.append(sorted_word)

    anagrams = []
    for i in range(len(sorted_words)):
        for j in range(len(sorted_words)):
            if sorted_words[i] == sorted_words[j] and words[i] != words[j]:
                anagrams.append([words[i], words[j]])

    for row in anagrams:
        print(row)  # change print to use format
# check pass


main()