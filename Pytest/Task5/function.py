def count_chars(string):
    output = [0, 0, 0]
    for i in string:
        output[ord(i) - ord("a")] += 1
    return output