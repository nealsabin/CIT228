def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['Chapter10/LordOfTheRings.txt', 'Chapter10/Dune.txt', 'Chapter10/Foundation.txt']
for filename in filenames:
    count_words(filename)

#10-10
def find_words(filename,word):
    try: 
        with open(filename, encoding='utf-8') as f:
            contents2 = f.read()
    except FileNotFoundError:
        pass
    else: 
        word_count=contents2.lower().count(word.lower())
        print(f"The file {filename} has the word, {word}, {word_count} times.")

word=input("Word to search: ")
for filename in filenames:
    find_words(filename,word)