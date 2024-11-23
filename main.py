def main():
    with open("books/frankenstein.txt") as f:
        file_contents=f.read()
        wordcount = file_contents.split()
        low_word = file_contents.lower()
        char_dic = {}
        count = 1
        for i in low_word:
            if i in char_dic:
                char_dic[i] +=1
            else:
                char_dic.update({i:1})

        for x,y in char_dic.items():
            print(f"The '{x}' character was found {y} times")
        


main()