# O(n^2) time | O(n) space
def rectangleMania(coords):
	coordsSet = set([(coord[0], coord[1]) for coord in coords])
	rectangleCount = 0
	for x1,y1 in coords:
		for x2,y2 in coords:
			if x2 > x1 and y2 > y1:
				if (x1,y2) in coordsSet and (x2,y1) in coordsSet:
					rectangleCount += 1
	return rectangleCount


print(rectangleMania([[0, 0], [0, 1], [1, 1], [1, 0], [2, 1], [2, 0], [3, 1], [3, 0]]))
