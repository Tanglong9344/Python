import string

with open('ss.txt', 'r', encoding='utf-8') as text:
    words = text.read().split()
    print(words)
    for word in words:
        print('{}:{} times'.format(word, words.count(word)), end=', ')
    print()

print('---------------')
with open('ss.txt', 'r') as text:
    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    words_index = set(words)
    print(words_index)
    counts_dict = {index: words.count(index) for index in words_index}
    print(counts_dict)
    for word in sorted(counts_dict, key=lambda x: counts_dict[x], reverse=True):
        print('{}:{} times'.format(word, counts_dict[word]), end=', ')
    print()
