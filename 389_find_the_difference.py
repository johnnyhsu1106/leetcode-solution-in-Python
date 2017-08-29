'''
Given two strings s and t which consist of only lowercase letters.
String t is generated by random shuffling string s and then add one more letter at a random position.
Find the letter that was added in t.

Example:

Input:
s = "abce"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
'''

class Solution:
    def findTheDifference_1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        '''
        idea:
        brute force. two for loop. O(n^2)
        for each char in s, if char exists in t, just remove this char from t.
        '''
        s = list(s)
        t = list(t)
        for char in s:
            t.remove(char)
        return t[0]



    def findTheDifference(self, s, t):
        '''
        idea:
        Sort string and compare each letter.
        Use the zip function to generate the tuple/pair
        Then, compare the
        For example,
        s = 'abde'
        t = 'abcde'
        zip(s,t) will generate ('a','a'), ('b','b'),('d','c'),('e','d')
        for each tuple, if elements in tuple are not the same, return the later element


        For example,
        s = 'abcd'
        t = 'abcde'
        zip(s,t) will generate ('a','a'), ('b','b'),('c','c'),('d'','d')
        If every the elments pair in tuple are the same, return t[-1]
        '''
        s = sorted(s)
        t = sorted(t)
        for (charS, charT) in zip(s,t):
            if charS != charT:
                return charT
        return t[-1]



def main():
    s = "abcd"
    t = "abcde"
    solution = Solution()
    print(solution.findTheDifference_1(s,t))

if __name__ == '__main__':
    main()
