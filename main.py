def main():
    path = 'books/frankenstein.txt'
    book_contents = get_book(path)
    word_count = get_words(book_contents)
    letter_count = get_letters(book_contents)
    print(letter_count)
    
def get_book(path):
    with open(path) as f:
        return f.read()
    
def get_words(book):
    return len(book.split())

def get_letters(book):
    dict = {}
    
    for char in book:
        lowercase_char = char.lower()
        if lowercase_char.isalpha():
            if lowercase_char in dict:
                dict[lowercase_char] += 1
            else:
                dict[lowercase_char] = 1
    return dict
            
        
if __name__ == "__main__":
    main()