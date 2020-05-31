# O(nm*8^s + ws) time | O(nm + ws) space    ;n & m is board's height & width, w is no. of words, s is the length of the longest word
def boggleBoard(board, words):
	trie = Trie()
	for word in words:
		trie.add(word)
	finalWords = {}
	visited = [[False for _ in row] for row in board]
	for i in range(len(board)):
		for j in range(len(board[i])):
			explore(i, j, board, visited, trie.root, finalWords)
	return list(finalWords.keys())

def explore(i, j, board, visited, trieNode, finalWords):
	if visited[i][j]:
		return
	letter = board[i][j]
	if letter not in trieNode:
		return
	visited[i][j] = True
	trieNode = trieNode[letter]
	if '*' in trieNode:
		finalWords[trieNode['*']] = True
	neighbors = getNeighbors(i, j, board)
	for neighbor in neighbors:
		explore(neighbor[0], neighbor[1], board, visited, trieNode, finalWords)
	visited[i][j] = False


def getNeighbors(i, j, board):
	neighbors = []
	if i > 0 and j > 0:
		neighbors.append([i - 1, j - 1])
	if i > 0 and j < len(board[0]) - 1:
		neighbors.append([i - 1, j + 1])
	if i < len(board) - 1 and j < len(board[0]) - 1:
		neighbors.append([i + 1, j + 1])
	if i < len(board) - 1 and j > 0:
		neighbors.append([i + 1, j - 1])
	if i > 0:
		neighbors.append([i - 1, j])
	if i < len(board) - 1:
		neighbors.append([i + 1, j])
	if j < len(board[0]) - 1:
		neighbors.append([i, j + 1])
	if j > 0:
		neighbors.append([i, j - 1])
	return neighbors
	
# def getNeighbours(i, j, board):
#     neighbours = []
#     possibleDirections = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
#     for direction in possibleDirections:
#         di, dj = direction
#         newI, newJ = i + di, j + dj
#         if 0 <= newI < len(board) and 0 <= newJ < len(board[0]):
#             neighbours.append([newI, newJ])
#     return neighbours

class Trie:
	def __init__(self):
		self.root = {}
		self.endSymbol = '*'

	def add(self, word):
		node = self.root
		for letter in word:
			if letter not in node:
				node[letter] = {}
			node = node[letter]
		node[self.endSymbol] = word

print(boggleBoard([['t', 'h', 'i', 's', 'i', 's', 'a'], 
				   ['s', 'i', 'm', 'p', 'l', 'e', 'x'], 
				   ['b', 'x', 'x', 'x', 'x', 'e', 'b'], 
				   ['x', 'o', 'g', 'g', 'l', 'x', 'o'], 
				   ['x', 'x', 'x', 'D', 'T', 'r', 'a'], 
				   ['R', 'E', 'P', 'E', 'A', 'd', 'x'], 
				   ['x', 'x', 'x', 'x', 'x', 'x', 'x'], 
				   ['N', 'O', 'T', 'R', 'E', '-', 'P'], 
				   ['x', 'x', 'D', 'E', 'T', 'A', 'E']], 
				   ["this", "is", "not", "a", "simple", "boggle", "board", "test", "REPEATED", "NOTRE-PEATED"]))