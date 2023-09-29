from pathlib import Path

def common_words(filename):
    path = Path(filename)
    word = input('Please insert the word: ')
    
    try:
        contents = path.read_text('utf-8')
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)
        print(f"\nReading {filename}:")
        print(f"    this word {word} appears {word_count} times.\n")

filename = 'the_great_gatsby'
common_words(filename)

filename = 'iliad.txt'
common_words(filename)

filename = 'the_hobbit.txt'
common_words(filename)