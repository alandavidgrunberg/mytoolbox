def try_me():
    return "testing testing testing 123 123 123"

def sarcasticize(text):
    char_list = []
    count = 0
    for char in text:
        if count % 2 == 0:
            char_list.append(char.lower())
        else:
            char_list.append(char.upper())
        count += 1
    sarcasticized = ''.join(char_list)
    print(sarcasticized)
    return sarcasticized
