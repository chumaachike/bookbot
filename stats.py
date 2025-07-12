def word_count(text):
    text_list = text.split()
    return len(text_list)

def char_count(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict


def sort_dictionary(dictionary):
    return sorted(
        [{"char": char, "num": num} for char, num in dictionary.items()],
        key=lambda x: x["num"], reverse=True
    )

