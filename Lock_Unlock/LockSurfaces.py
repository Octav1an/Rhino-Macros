import rhinoscriptsyntax as rs 

def lockSurfaces():
	surfaces = rs.ObjectsByType(8)
	if not surfaces: 
		print("0 Surfaces were found")
		return False

	intCount = rs.LockObjects(surfaces)
	print("Locked {} Surfaces").format(intCount)

lockSurfaces()