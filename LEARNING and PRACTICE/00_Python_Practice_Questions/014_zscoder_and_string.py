/*

zscoder and string (100 Marks)
ZScoder loves simple strings! A string t is called simple if every pair of adjacent characters are distinct. For example ab, aba, zscoder are simple whereas aa, add are not simple.

zscoder is given a string s. He wants to change a minimum number of characters so that the string s becomes simple. Help him with this task!


Input Format
You will be given a function which contains the string s, the string given to zscoder as a single argument. The string s consists of only lowercase English letters.


Constraints
1 < = |s| < = 2*105

Output Format
Return the simple string s' the string s after the minimal number of changes. If there are multiple solutions, you may output any of them.Note that the string s' should also consist of only lowercase English letters.


Sample TestCase 1
Input
aab
Output
bab



*/



if __name__ == "__main__":
    s = input()

    simple = False
    s_copy = ""


    while not simple:
        simple = True
        s_copy = ""
        for i in range(0, len(s)):
            if i + 1 < len(s) and s[i] == s[i+1]:
                if ord(chr(ord(s[i]) - 1)) >= 97:
                    s_copy = s_copy + chr(ord(s[i]) - 1)
                else:
                    s_copy = s_copy + chr(ord(s[i]) + 1)
                simple = False
            else:
                s_copy = s_copy + s[i]
        
        s = s_copy
        
            
    print(s_copy, end="")



