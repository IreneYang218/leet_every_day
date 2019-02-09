"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ""
"""
def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        len_strs = len(strs)
        if len_strs == 0:
            return ""
        min_len = min([len(x) for x in strs])
        c_prefix = ""
        flag = 1
        for i in range(min_len):
            for j in range(1, len_strs):
                if strs[0][i] == strs[j][i]:
                    flag = flag*1
                else:
                    flag = 0
            if flag == 1:
                c_prefix = c_prefix + strs[0][i]
        return c_prefix

def better_longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    prefix = ""
    #if len(strs) == 0:
       # return ""
    for c in zip(*strs):
        if len(set(c)) == 1:
            prefix += c[0]
        else:
            break # faster
    return prefix