def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_counts = count_characters(text)
    #print(text)
    print(f"There are {word_count} words in the above text.")
    print(char_counts)

def get_book_text(path):    
    with open(path) as f:
        return f.read()
    
def count_words(text):
    count = len(text.split())
    return count

def count_characters(text):
    lowered_string = text.lower()
    char_counts = {}
    
    for char in lowered_string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

main()