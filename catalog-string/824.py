# 824. 山羊拉丁文
# https://leetcode-cn.com/problems/goat-latin/

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        word_cnt = 0
        res = []
        for item in sentence.split(" "):
            word_cnt += 1
            if item[0].lower() in {"a", "e", "i", "o", "u"}:
                word = f"{item}ma{'a'*word_cnt}"
            else:
                word = f"{item[1:]}{item[0]}ma{'a'*word_cnt}"
            res.append(word)
        return " ".join(res)
