import rhinoscriptsyntax as rs 

def lockMesh():
	mesh = rs.ObjectsByType(32)
	if not mesh: 
		print("0 Mesh was found")
		return False

	intCount = rs.LockObjects(mesh)
	print("Locked {} Mesh").format(intCount)

lockMesh()