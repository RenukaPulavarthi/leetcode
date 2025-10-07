class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        res = [-1 for i in rains]
        n = len(rains)
        d = {}
        zeros = []
        for i in range(n):
            if rains[i] > 0:
                if rains[i] not in d:
                    d[rains[i]] = i
                else:
                    if len(zeros) == 0:
                        return []
                    k = zeros.pop()
                    if k < d[rains[i]]:
                        return []
                    res[k] = rains[i]
                    d[rains[i]] = i
            else:
                zeros.append(i)
        for i in d:
            x = i
            break
        while zeros:
            k = zeros.pop()
            res[k] = x
        return res

