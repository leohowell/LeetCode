class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiouAEIOU'
        length = len(s)
        list_s = list(s)
        start = 0
        end = length - 1
    
        def find_left_vowel(s, start, end):
            while start < end:
                if s[start] not in vowels:
                    start += 1
                else:
                    return start
    
        def find_right_vowel(s, start, end):
            while start < end:
                if s[end] not in vowels:
                    end -= 1
                else:
                    return end
    
        def join2string():
            return ''.join(list_s)
    
        while start < end:
            start = find_left_vowel(s, start, end)
            if not isinstance(start, int):
                return join2string()
            end = find_right_vowel(s, start, end)
            if not end:
                return join2string()
            list_s[start], list_s[end] = list_s[end], list_s[start]
            start += 1
            end -= 1
        else:
            return join2string()
