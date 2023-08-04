#!/usr/bin/python

class Solution:
    def isValid(self, s: str) -> bool:
        # Here I try to keep track of important symbols
        # By appending them on stack.
        # If stack is not empty on the end of algorithm,
        # or expected closing parenthesis doesn't correspond
        # to a given one - return False.

        # This solution tries to reduce amount of calls to the dictionary
        # by hardcoding letters list
        corresponding = {
                '(': ')',
                '{': '}',
                '[': ']'
        }
        stack = []
        for letter in s:
            if letter in '})]' and (not stack or stack.pop() != letter):
                return False
            elif letter in '[({':
                stack.append(corresponding[letter])
        return not stack


if __name__ == '__main__':
    cases = [
        ('([{(fsdfsdf)fdsfsd}], fsdfsd)', True),
        ('[{(})]', False),
        ('[({})]', True),
        ('', True)
    ]
    solver = Solution()
    for case, answer in cases:
        assert answer == solver.isValid(case)
    print("Succeeded")
