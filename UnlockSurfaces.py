import rhinoscriptsyntax as rs 

def unlockSurfaces():
	surfaces = rs.ObjectsByType(8)
	if not surfaces: 
		print("0 Surfaces were found")
		return False

	intCount = rs.UnlockObjects(surfaces)
	print("Unlocked {} Surfaces").format(intCount)

unlockSurfaces()