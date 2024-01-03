sentence = input("Insert sentence: ")
words = sentence.split()
k_words = [word for word in words if word.lower().startswith('k')]
if k_words:
    print(f"Words that start with 'k': {', '.join(k_words)}")
else:
    print("There are no words starting with 'k' in the sentence.")