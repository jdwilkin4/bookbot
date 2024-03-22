def main():
    path = 'books/frankenstein.txt'
    book_contents = get_book(path)
    word_count = get_words(book_contents)
    print(word_count)
    
def get_book(path):
    with open(path) as f:
        return f.read()
    
def get_words(book):
    return len(book.split())
        
if __name__ == "__main__":
    main()