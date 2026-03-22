class UnionFind:
    def __init__(self):
        self._next_id = 0
        self._parents = []
        self._ranks = []

    def make_set(self):
        val = self._next_id
        self._next_id += 1
        self._parents.append(val)
        self._ranks.append(0)
        return val

    def find(self, x):
        if self._parents[x] != x:
            self._parents[x] = self.find(self._parents[x])

        return self._parents[x]

    def merge(self, lhs, rhs):
        s1 = self.find(lhs)
        s2 = self.find(rhs)

        if s1 == s2:
            return s1

        r1 = self._ranks[s1]
        r2 = self._ranks[s2]
        if r1 == r2:
            self._parents[s2] = s1
            self._ranks[s1] += 1
            return s1
        elif r1 < r2:
            self._parents[s1] = s2
            return s2
        else:
            self._parents[s2] = s1
            return s1
