class Solution(object):
    def predictPartyVictory(self, senate):
        r = []
        d = []

        for i, j in enumerate(senate):
            if j == "R":
                r.append(i)
            else:
                d.append(i)

        while r and d:
            idx_r = r.pop(0)
            idx_d = d.pop(0)

            if idx_r < idx_d:
                r.append(idx_r + len(senate))
            else:
                d.append(idx_d + len(senate))

        return "Radiant" if r else "Dire"