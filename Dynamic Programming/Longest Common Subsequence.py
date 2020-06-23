# # O(nm * min(n, m)) time | O(nm * min(n, m)) space
# def longestCommonSubsequence(str1, str2):
# 	lcs = [[[] for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
# 	for i in range(1, len(str2) + 1):
# 		for j in range(1, len(str1) + 1):
# 			if str1[j - 1] == str2[i - 1]:
# 				lcs[i][j] = lcs[i - 1][j - 1] + [str1[j - 1]]
# 			else:
# 				lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1], key = len)
# 	return lcs[-1][-1]

# O(nm) time | O(nm) space
def longestCommonSubsequence(str1, str2):
	lcs = [[[None, 0, None, None] for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
	for i in range(1, len(str2) + 1):
		for j in range(1, len(str1) + 1):
			if str1[j - 1] == str2[i - 1]:
				lcs[i][j] = [str1[j - 1], lcs[i - 1][j - 1][1] + 1, i - 1, j - 1]
			else:
				if lcs[i - 1][j][1] > lcs[i][j - 1][1]:
					lcs[i][j] = [None, lcs[i - 1][j][1], i - 1, j]
				else:
					lcs[i][j] = [None, lcs[i][j - 1][1], i, j - 1]
	return buildSequence(lcs)

def buildSequence(lcs):
	sequence = []
	i = len(lcs) - 1
	j = len(lcs[0]) - 1
	while i != 0 and j != 0:
		current = lcs[i][j]
		if current[0] is not None:
			sequence.append(current[0])
		i = current[2]
		j = current[3]
	return sequence[::-1]

print(longestCommonSubsequence("ZXVVYZW","XKYKZPW"))