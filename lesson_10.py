# def longestNiceSubstring(s: str) -> str:
#     c = set(s)
#     for i, v in enumerate(s):
#         if v.swapcase() not in c:
#             return max(map(longestNiceSubstring, [s[:i], s[i+1:]]), key=len)
#     return s
#
#
# s = "YBbazaAay"
#
# result = longestNiceSubstring(s)
# print(result)
s = "b"
t = "c"
# b = ''
# for i in s:
#     if i in t:
#         b += i
# if b == s:
#     print(True)
# else:
#     print(False)

# if len(s) > len(t): return False
# if len(s) == 0: return True
# subsequence = 0
# for i in range(0, len(t)):
#     if subsequence <= len(s) - 1:
#         if s[subsequence] == t[i]:
#             subsequence += 1
# # print(subsequence == len(s))
# s = "abc"
# t = "ahbgdc"
# o = 0
# for i in range(0, len(t)):
#     if o <= len(s) - 1:
#         if s[o] == t[i]:
#             o += 1
# print(o == len(s))
# order = "cba"
# s = "abcd"
# s = sorted(s, key=lambda i: (order.index(i) if i in order else ord(i)))
# print(''.join(s))
