class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 0
            d[i] += 1
        freq = {}
        for i in d:
            if d[i] not in freq:
                freq[d[i]] = [i]
            else:
                freq[d[i]].append(i)
        print(freq)
        ans = ""
        cnt = 0
        for i in freq:
            if len(ans) < len(freq[i]):
                ans = ''.join(freq[i])
                cnt = i
            elif len(ans) == len(freq[i]) and cnt < i:
                ans = ''.join(freq[i])
                cnt = i
        return ans