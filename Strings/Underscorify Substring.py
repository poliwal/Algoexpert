# O(n + m) time | O(n) space      ; m is length of substring
def underscorifySubstring(string, subString):
	locations = collapse(getLocations(string, subString))
	return underscorify(string, locations)

def getLocations(string, subString):
	locations = []
	startIdx = 0
	while startIdx < len(string):
		nextIdx = string.find(subString, startIdx)
		if nextIdx != -1:
			locations.append([nextIdx, nextIdx + len(subString)])
			startIdx = nextIdx + 1
		else:
			break
	return locations

def collapse(locations):
	if not len(locations):
		return locations
	newLocation = [locations[0]]
	previous = locations[0]
	for i in range(1, len(locations)):

		current = locations[i]
		if current[0] <= previous[1]:
			previous[1] = current[1]
		else:
			newLocation.append(current)
			previous = current
	return newLocation

def underscorify(string, locations):
	locationIdx = 0
	stringIdx = 0
	inBetweenUnderscores = False
	finalString = []
	i = 0
	while stringIdx < len(string) and locationIdx < len(locations):
		if stringIdx == locations[locationIdx][i]:
			finalString.append('_')
			inBetweenUnderscores = not inBetweenUnderscores
			if not inBetweenUnderscores:
				locationIdx += 1
			i = 0 if i == 1 else 1
		finalString.append(string[stringIdx])
		stringIdx += 1
	if locationIdx < len(locations):
		finalString.append('_')
	elif stringIdx < len(string):
		finalString.append(string[stringIdx:])
	return "".join(finalString)


print(underscorifySubstring("testthis is a testtest to see if testestest it works","test"))