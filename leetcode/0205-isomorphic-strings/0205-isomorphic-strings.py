class Solution(object):
    def isIsomorphic(self, s, t):
        s_dict = {}
        s_set = set()
        for s_, t_ in zip(list(s), list(t)):
            if not s_dict.get(s_) and t_ not in s_set:
                s_set.add(t_)
                s_dict[s_] = t_
            else:
                if s_dict.get(s_) != t_:
                    return False
        return True