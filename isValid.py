
cases = ["()", "()(()","()[]{}","[([)]","{[]}"]
#True, False, True, False, False, True

class Solution(object):
    def isValid(self, s):
        mapping = { ")": "(", "}": "{", "]": "[" }
        stack = []
        for ch in s :
            if ch in ['(', '{',  '[' ]:
                stack.append(ch)
            else:
                top_element = stack.pop() if stack else '#'
                if mapping[ch] != top_element:
                    print("Match: ", ch, top_element)
                    return False
        if stack:
            print("Stack: ", stack)
            return False
        else:
            return True

def main():
    s = Solution()
    for c in cases:
        print(s.isValid(c))

if __name__ == '__main__':
    main()
