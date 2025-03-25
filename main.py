import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_counts = count_characters(text)
    #print(text)
    #print(f"There are {word_count} words in the above text.")
    #print(char_counts)

    create_report(book_path, word_count, char_counts)

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

def create_report(book_path, word_count, char_counts):
    alpha_list = []
    
    def sort_on(dict):
        return dict["count"]

    for char in char_counts.keys():
        if char.isalpha():
            new_dict = {"letter": char, "count": char_counts[char]}
            alpha_list.append(new_dict)
    
    alpha_list.sort(reverse=True, key=sort_on)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in alpha_list:
        print(f"{item['letter']}: {item['count']}")

    print("============= END ===============")


main()