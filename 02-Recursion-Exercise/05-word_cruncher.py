def find_all_word_variations(index, target, words_count, words_indices, used_words):
    if index >= len(target):
        print(" ".join(used_words))
        return
    if index not in words_indices:
        return
    for word in words_indices[index]:
        if words_count[word] == 0:
            continue
        used_words.append(word)
        words_count[word] -= 1

        find_all_word_variations(index + len(word), target, words_count, words_indices, used_words)

        used_words.pop()
        words_count[word] += 1


words = input().split(', ')
target = input()

words_count = {}
words_indices = {}

for word in words:
    if word in words_count:
        words_count[word] += 1
        continue
    words_count[word] = 1

    try:
        index = 0
        while True:
            index = target.index(word, index)
            if index not in words_indices:
                words_indices[index] = []
            words_indices[index].append(word)
            index += len(word)
    except ValueError:
        pass

find_all_word_variations(0, target, words_count, words_indices, [])
