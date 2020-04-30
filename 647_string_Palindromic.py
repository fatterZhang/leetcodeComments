# -*- coding: utf-8 -*-#
# Name:         647_string_Palindromic
# Author:       ARCHI
# Date:         2020/3/20
# Description:  字符串相关的回文串
# -------------------------------------------------------------------------------


# Manacher's Algorithm 马拉车算法 求回文串
# 参考链接： https://www.cnblogs.com/grandyang/p/4475985.html   https://www.jianshu.com/p/392172762e55
from typing import List


def manacher_detail(s: str):
    if not s:
        return None

    s = "$#" + '#'.join(list(s)) + "#"
    p = [0] * len(s)
    print(s)

    mx, idx, resLen, resCenter = 0, 0, 0, 0
    for i in range(1, len(s)):
        print(idx, mx, i)
        print(s)
        print(p)

        if i >= mx:
            print('   以s[%d]=%s为中心的回文串，超出了MX=%d'%(i, s[i], mx))
            p[i] = 1
        else:
            print('   以s[%d]=%s为中心的回文串, 中心在 MX=%d内' % (i, s[i], mx))

            j = 2*idx - i
            print("   以idx=%d为中心， i=%d 的对称位置为j=%d"%(idx, i, j))

            if p[j] < mx - i:
                print("   p[j] = %d, 小于当前中心i=%d到MX=%d的长度"%(p[j], i, mx))
                p[i] = p[j]
            else:
                print("   以s[%d]=%s为中心的回文串长度%d, 不小于mx-i=%d"%(j, s[j], p[j], mx-i))
                p[i] = mx - i

        while i+p[i] < len(s) and s[i+p[i]] == s[i-p[i]]:

            p[i] += 1
            print("       边界向两侧延申。。。。%d"%(i + p[i]))

        print("   最终确定，以s[%d]=%s为中心的回文串半径为%d"%(i, s[i], p[i]))

        # 如果有边界超过了
        if mx < i + p[i]:
            print("   调整当前可达的最右边界 %d ---> %d， 和其中心 %d ---> %d"%(mx, i+p[i], idx, i))
            mx, idx = i + p[i], i

        # 记录最长回文串中的中心索引和长度
        if resLen < p[i]:
            resLen, resCenter = p[i], i

        i += 1

def manacher(s: str) -> List[int]:
    if not s:
        return None

    s = "@#" + '#'.join(s) + "#"
    print(s)
    p = [0] * len(s)

    mx, idx = 0, 0
    for i in range(1, len(s)):
        p[i] = min(p[2*idx-i], mx-i) if i < mx else 1

        while (i+p[i] < len(s)) and (i-p[i] >= 0) and (s[i+p[i]] == s[i-p[i]]):
            p[i] += 1
        print(idx, p[i])
        if i+p[i] > mx:
            mx, idx = i+p[i], i

    return p


def longestPalindrome(s: str) -> str:
    if not s:
        return ""

    s = "@#" + "#".join(list(s)) + "#"
    print(s)
    p = [0] * len(s)
    mx, idx, maxCenter = 0, 0, 0
    for i in range(len(s)):
        p[i] = min(p[2*idx-i], mx-i) if i < mx else 1
        while (i + p[i] < len(s)) and (i - p[i] >= 0) and (s[i+p[i]] == s[i-p[i]]):
            p[i] += 1

        if i + p[i] > mx:
            mx, idx = i + p[i], i

        print(i, p[i], maxCenter)
        if p[i] > p[maxCenter]:
            print("***", i, p[i])
            maxCenter = i
    print(maxCenter, p[maxCenter])
    return s[maxCenter - p[maxCenter] + 1: maxCenter + p[maxCenter]].replace("#", '')

if __name__ == "__main__":
    s = "bananas"
    print(longestPalindrome(s))
    # print(manacher_detail(s))