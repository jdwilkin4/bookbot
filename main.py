def main():
    path = 'books/frankenstein.txt'
    book_contents = get_book(path)
    word_count = get_words(book_contents)
    letter_count = get_letters(book_contents)
    list_of_letter_dicts = get_chars_list(letter_count)
    print_report(path,word_count,list_of_letter_dicts)
    
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

def get_chars_list(letters):
    chars_list = []
    for char in letters:
        dict = {}
        dict[char] = letters[char]
        chars_list.append(dict)
        
    return chars_list

def sort_by(dict):
    return dict[list(dict.keys())[0]]

def print_report(path, words, letter_list):
    letter_list.sort(reverse=True, key=sort_by)
    
    print(f'--- Begin report of {path} ---')
    print(f'{words} words found in the document')
    print("\n")
    
    for dict in letter_list:
        for char, num in dict.items():
            print(f'The \'{char}\' character was found {num} times')
    
    print('--- End report ---')      
        
if __name__ == "__main__":
    main()