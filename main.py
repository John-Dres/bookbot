def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = character_count(text)
    char_list = dict_into_list(chars_dict)
    #print(char_list)
    char_list.sort(reverse=True, key=sort_on)
    #character_report = report(char_list)
    #print(character_report)
    report(char_list, book_path, num_words)
    #print(f"{num_words} words found in the document")
    #print(character_count(lower_case_book(book_path)).sort(reverse=True, key=sort_on))
    #print(character_count(lower_case_book(book_path)))
    #print(character_count(lower_case_book("books/frankenstein.txt")).sort(reverse=True))
    #print(dict_into_list(character_count))

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def character_count(text):
    count_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered in count_dict:
            count_dict[lowered] += 1
        else:
            count_dict[lowered] = 1
    return count_dict

def dict_into_list(chars_dict):
    char_list = []
    for c in chars_dict:
        char_list.append({"char": c, "num": chars_dict[c]})
    return char_list


def sort_on(chars_dict):
    for c in chars_dict:
        return chars_dict["num"]

def report(char_list, book_path, num_words):
    print("--- Begin report of " ,book_path, "---")
    print(f"{num_words} words found in the document")
    print()
    for c in char_list:
        if c["char"].isalpha():
            print(f"The '{c["char"]}' character was found {c["num"]} times")
    print("--- End report ---")

main()