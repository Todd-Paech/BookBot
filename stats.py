def get_length(file_path: str) -> int:
    with open(file_path) as f:
        file_contents = f.read()
    length = len(file_contents.split())
    return length

def letter_count(text: str) -> dict[str, int]:
    dict = {}
    for letter in text:
        if letter.lower() in dict:
            dict[letter.lower()] += 1
        else:
            dict[letter.lower()] = 1
    return dict

def sort_on(counts: tuple[str, int]) -> int:
    return counts[1]

def chars_dict_to_sorted_list(dict: dict[str, int]) -> list[tuple[str, int]]:
    list = []
    for letter in dict:
        count = dict[letter]
        list.append((letter, count))
    sorted_list = sorted(list, reverse=True, key=sort_on)
    return sorted_list