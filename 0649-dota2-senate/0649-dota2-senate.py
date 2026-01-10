class Solution(object):
    def predictPartyVictory(self, senate):
        r = []
        d = []

        for i, j in enumerate(senate):
            if j == "R":
                r.append(i)
            else:
                d.append(i)
        
        idx = 0
        while idx < len(r) and idx < len(d):
            if r[idx] < d[idx]:
                r.append(r[idx] + len(senate))
            else:
                d.append(d[idx] + len(senate))
            idx += 1
        
        return "Radiant" if len(r) > len(d) else "Dire"
            