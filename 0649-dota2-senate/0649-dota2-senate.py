class Solution(object):
    def predictPartyVictory(self, senate):
        r = []
        d = []

        for i, j in enumerate(senate):
            if j == "R":
                r.append(i)
            else:
                d.append(i)
        
        idx_r = 0
        idx_d = 0
        while idx_r < len(r) and idx_d < len(d):
            if r[idx_r] < d[idx_d]:
                r.append(r[idx_r] + len(senate))
            else:
                d.append(d[idx_d] + len(senate))
            idx_r += 1
            idx_d += 1
        
        return "Radiant" if len(r) > len(d) else "Dire"
            