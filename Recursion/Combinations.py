def Combinations(n, k):
        def helper(comb,idx, arr):
            if len(comb) == k:
                l = []
                l.extend(comb)
                arr.append(l)
                return
            else:        
                for elem in range(idx, n + 1):
                    comb.append(elem)
                    helper(comb,elem + 1, arr)
                    comb.pop()

        arr = []
        helper([], 1, arr)
        return arr

print(Combinations(4, 2)) 