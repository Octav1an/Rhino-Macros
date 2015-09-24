import rhinoscriptsyntax as rs 

def lockPoints():
	points = rs.ObjectsByType(1)
	if not points: 
		print("0 Points were found")
		return False

	intCount = rs.LockObjects(points)
	print("Locked {} Points").format(intCount)

lockPoints()