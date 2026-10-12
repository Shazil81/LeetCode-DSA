class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def Union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pv == pu:
            return False

        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pv] < self.rank[pu]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return True
from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        n = len(accounts)
        ds = DisjointSet(n)

        # Step 1: Email mapping
        email_idx = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:          # account[0] naam hai, skip
                if email not in email_idx:
                    email_idx[email] = i
                else:
                    ds.Union(i, email_idx[email])
        
        # root k hisab se emails group kro
        merged = defaultdict(list)
        for email, idx in email_idx.items():
            root = ds.find(idx)
            merged[root].append(email)

        # Step 4: final answer 
        res = []
        for root, emails in merged.items():
            res.append([accounts[root][0]] + sorted(emails))

        return res