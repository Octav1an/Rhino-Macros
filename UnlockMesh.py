import rhinoscriptsyntax as rs 

def unlockMesh():
	mesh = rs.ObjectsByType(32)
	if not mesh: 
		print("0 Mesh was found")
		return False

	intCount = rs.UnlockObjects(mesh)
	print("Unlocked {} Mesh").format(intCount)

unlockMesh()