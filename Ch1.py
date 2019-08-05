print("----------1.1----------")
def unique_chars(s):
    char_dict = {}
    for char in s:
        if char in char_dict.keys():
            return False
        else:
            char_dict[char] = 1
    return True
print(unique_chars("happybirthday"))
print(unique_chars("thequickbrwnfox"))

print("----------1.2----------")
def is_permutation(s1, s2):
    char_dict = {}
    for char in s1:
        if char in char_dict.keys():
            char_dict[char]['s1'] += 1
        else:
            char_dict[char] = {'s1': 1, 's2': 0}
    for char in s2:
        if char in char_dict.keys():
            char_dict[char]['s2'] += 1
        else:
            char_dict[char] = {'s2': 1, 's1': 0}
    for key in char_dict.keys():
        if char_dict[key]['s1'] != char_dict[key]['s2']:
            return False
    return True
print(is_permutation('jogger', 'gojger'))
print(is_permutation('abcd', 'efgh'))

print("----------1.3----------")
def replace_spaces(s):
    l = list(s)
    while l[-1] == " ":
        l.pop()
    while l[0] == " ":
        l.pop(0)
    for i in range(len(l)):
        if l[i] == " ":
            l[i] = '%20'
        else:
            continue
    return "".join(l)
print(replace_spaces("Mr John Smith"))
print(replace_spaces("Mr John Smith "))
print(replace_spaces(" Mr John Smith "))

print("----------1.4----------")
def palindrome_permutation(s):
    char_dict = {}
    for char in s:
        if char == " ":
            continue
        if char in char_dict.keys():
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    odd = False
    for key in char_dict.keys():
        if not odd and char_dict[key] % 2 != 0:
            odd = True
        elif odd and char_dict[key] % 2 != 0:
            return False
    return True
print(palindrome_permutation("CAT TRAC"))
print(palindrome_permutation("CAT TRACK"))

print("----------1.5----------")
def one_edit_away(s1, s2):

    diff = len(s1) - len(s2) if len(s1) >= len(s2) else len(s2) - len(s1)
    
    if diff > 1:
        return False
    elif diff == 0:
        edit = False
        for i in range(len(s1)):
            if not edit and s1[i] != s2[i]:
                edit = True
            elif edit and s1[i] != s2[i]:
                return False
    elif diff == 1:
        edit = False
        if len(s1) < len(s2):
            for i in range(len(s1)):
                if not edit and s1[i] != s2[i]:
                    edit = True
                elif edit and s1[i] != s2[i+1]:
                    return False
        else:
            for i in range(len(s2)):
                if not edit and s1[i] != s2[i]:
                    edit = True
                elif edit and s2[i] != s1[i+1]:
                    return False
    return True
print(one_edit_away('pale', 'ple'))
print(one_edit_away('pales', 'pale'))
print(one_edit_away('pale', 'bale'))
print(one_edit_away('pale', 'bake'))

print("----------1.6----------")
def string_compression(s):
    count = 1
    compressed_list = []
    for i in range(len(s)):
        if i == len(s) - 1:
            char = s[i] + str(count)
            compressed_list.append(char)
        elif s[i] == s[i+1]:
            count += 1
        else:
            char = s[i] + str(count)
            compressed_list.append(char)
            count = 1
    return_s =  "".join(compressed_list)
    if len(s) >= len(return_s):
        return return_s
    return s
print(string_compression("aabbbccccddddd"))
print(string_compression("aabbbccccddddde"))
print(string_compression("aabccddaabceAASs"))
print(string_compression("a"))

print("----------1.7----------")
def rotate_matrix(m):
    n = len(m)
    r = []
    for i in range(n):
        r.append([])
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            char = m[j][i]
            r[i].append(char)
    return r
test = [
    ['a', 'b', 'c', 'd', 'e'],
    ['f', 'g', 'h', 'i', 'j'],
    ['k', 'l', 'm', 'n', 'o'],
    ['p', 'q', 'r', 's', 't'],
    ['u', 'v', 'w', 'x', 'y']
]
result = [
    ['u', 'p', 'k', 'f', 'a'],
    ['v', 'q', 'l', 'g', 'b'],
    ['w', 'r', 'm', 'h', 'c'],
    ['x', 's', 'n', 'i', 'd'],
    ['y', 't', 'o', 'j', 'e']
]
print(rotate_matrix(test)==result)

print("----------1.8----------")
def reset_matrix(m):
    nrows = len(m)
    ncols = len(m[0])
    position = []
    for i in range(nrows):
        for j in range(ncols):
            if m[i][j] == 0:
                position.append((i, j))
    for item in position:
        i = item[0]
        j = item[1]
        for k in range(len(m[0])):
            m[i][k] = 0
        for k in range(len(m)):
            m[k][j] = 0
    return m
test = [
    [1, 2, 3, 4, 5],
    [1, 2, 0, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
]
result = [
    [1, 2, 0, 4, 5],
    [0, 0, 0, 0, 0],
    [1, 2, 0, 4, 5],
    [1, 2, 0, 4, 5]
]
test2 = [
    [1, 2, 3, 4, 5],
    [1, 2, 0, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 0, 5]
]
result2 = [
    [1, 2, 0, 0, 5],
    [0, 0, 0, 0, 0],
    [1, 2, 0, 0, 5],
    [0, 0, 0, 0, 0]
]
print(reset_matrix(test)==result)
print(reset_matrix(test2)==result2)

print("----------1.9----------")
def is_substring(s, sub):
    for i in range(len(s) - 1):
        if s[i] == sub[0]:
            for j in range(1, len(sub)):
                if s[i+j] != sub[j]:
                    return False
    return True
print(is_substring("abcdefgh", "def"))
print(is_substring("abcdabcdefg", "bcdefg"))