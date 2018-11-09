import time

input_words_list =[["leave", ["leav", "eavt", "eaaaaaaaaaaaaaaaaaaaaaaaaa"]],
              ["reset", "rest"],
              ["dragoon", "dragon"],
              ["leave", "leave"],
              ["sleet", "lets"],
              ["skiff", "ski"]]


def list_elements_len(*args):
    elements_len = map(len, *args)
    return elements_len


def funnel(word1, *word2):
    if isinstance(word2[0], list):
        word2 = word2[0]
    elif isinstance(word2[0], str):
        word2 = list(word2)
    if len(word1)-1 in list_elements_len(word2):
        for letter_position, _ in enumerate(word1):
            word1_without_letter = word1[:letter_position]+word1[letter_position+1:]
            if word1_without_letter in word2:
                return True
    return False


def duration(func):
    def wrapper(*wor):
        start = time.time()
        func(*wor)
        end = time.time()
        print((end-start))
    return wrapper


@duration
def my_solution(*input_words):
    for pair in input_words:
        print(funnel(*pair))


if __name__ == "__main__":
    my_solution(*input_words_list)
