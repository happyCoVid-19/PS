def solution(word):
    ans = 0
    dictionary = []
    aeiou = ["A", "E", "I", "O", "U"]
    def make_dic(cnt, letter):
        if cnt == 5:
            return 
        for i in range(len(aeiou)):
            dictionary.append(letter+aeiou[i])
            make_dic(cnt + 1, letter + aeiou[i])
    make_dic(0, "")
    return dictionary.index(word) + 1