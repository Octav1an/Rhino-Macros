import rhinoscriptsyntax as rs 

def unlockPoints():
	points = rs.ObjectsByType(1)
	if not points: 
		print("0 Points were found")
		return False

	intCount = rs.UnlockObjects(points)
	print("Unlocked {} Points").format(intCount)

unlockPoints()