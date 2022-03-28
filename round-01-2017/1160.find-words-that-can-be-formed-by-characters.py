from collections import Counter, defaultdict


class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        total_len = 0

        cnt = Counter(chars)

        for word in words:
            if len(word) > len(chars):
                continue

            word_char_cnt = defaultdict(lambda: 0)
            for c in word:
                if c not in cnt:
                    break
                word_char_cnt[c] += 1
                if word_char_cnt[c] > cnt[c]:
                    break
            else:
                total_len += len(word)

        return total_len


def test():
    res = Solution().countCharacters(["hello","world","leetcode"], "welldonehoneyr")
    print(res)


test()
