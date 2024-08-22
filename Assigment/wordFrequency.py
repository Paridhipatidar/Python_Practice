def word_frequency(sentence):
    words = sentence.split()
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq
sentence = input("Enter a sentence: ")
frequency_dict = word_frequency(sentence)
print("Word frequencies:")
for word, freq in frequency_dict.items():
    print(f"{word}: {freq}")
