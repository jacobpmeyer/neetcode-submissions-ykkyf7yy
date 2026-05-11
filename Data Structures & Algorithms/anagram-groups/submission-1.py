class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        output = []
        for s in strs:
            t = "".join(sorted(s))
            if t not in hm:
                hm[t] = []
            hm[t].append(s)
        for v in hm.values():
            output.append(v)
        return output
        