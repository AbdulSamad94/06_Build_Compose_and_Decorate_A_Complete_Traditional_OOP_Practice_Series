def longest_word(str: str):
    arr = str.split(" ")
    lenth = 0
    word = ""
    for i in arr:
        if len(i) > lenth:
            lenth = len(i)
            word = i

    return (word, lenth)


output = longest_word("Abdul Samad is learning Python enthusiastically")
print(output)
