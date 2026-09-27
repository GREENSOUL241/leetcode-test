class Solution:
    def reverseParentheses(self, s):
        stack = ['']

        for ch in s:
            if ch == '(':
                stack.append('')
            elif ch == ')':
                word = stack.pop()
                stack[-1] += word[::-1]
            else:
                stack[-1] += ch

        return stack[0]