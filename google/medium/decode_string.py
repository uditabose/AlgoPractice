
def decode_string(pat_str):
    '''
    Given an encoded string, return it's decoded string.

    The encoding rule is: k[encoded_string], where the 
    encoded_string inside the square brackets is being 
    repeated exactly k times. Note that k is guaranteed to 
    be a positive integer.

    You may assume that the input string is always valid; 
    No extra white spaces, square brackets are well-formed, etc.

    Furthermore, you may assume that the original data does 
    not contain any digits and that digits are only for 
    those repeat numbers, k. For example, there won't be 
    input like 3a or 2[4].

    Examples:

    s = "3[a]2[bc]", return "aaabcbc".
    s = "3[a2[c]]", return "accaccacc".
    s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

    https://leetcode.com/problems/decode-string/description/

    Time : O(N)
    Space: O(N)
    Note :
    1. 2 stacks, one for numbers, others for the characters
    3. once `]` is reached, pop both numbers and string
    4. repeat strings, and append that to return string
    5. repeat till end
    '''

    if pat_str == None or len(pat_str) == 0:
        return pat_str

    ret_str = ""
    stack = []

    for char in pat_str:
        if char == '[':
            stack.append(' ')
        elif char == ']':
            chars = ''
            while stack[-1] != ' ':
                chars = stack.pop() + chars

            if stack and stack[-1] == ' ':
                stack.pop()

            rep = None
            if len(stack) == 0:
                rep = 1
            else:  
                rep = ''          
                while len(stack) > 0 and stack[-1].isdigit():
                    rep = stack.pop() + rep
                    
            #print(rep)  
            stack.append(chars * int(rep))
        else:
            stack.append(char)

    return "".join(stack)    

def run():
    print(decode_string("3[a]2[bc]"))
    print(decode_string("3[a2[c]]"))
    print(decode_string("2[abc]3[cd]ef"))
    print(decode_string("3[a2[c]]"))
    print(decode_string("100[leetcode]"))

    '''
    s = "3[a]2[bc]", return "aaabcbc".
    s = "3[a2[c]]", return "accaccacc".
    s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

    aaabcbc
    cccccccccccccccccccccccccccccccca
    abcabccdcdcdef
    '''

if __name__ == '__main__':
    run()

