def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    print(text)
    print(f"There are {word_count} words in the above text.")

def get_book_text(path):    
    with open(path) as f:
        return f.read()
    
def count_words(text):
    count = len(text.split())
    return count

main()