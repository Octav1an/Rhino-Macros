import rhinoscriptsyntax as rs 

def lockBreps():
	breps = rs.ObjectsByType(16)
	if not breps: 
		print("0 Breps were found")
		return False

	intCount = rs.LockObjects(breps)
	print("Locked {} Breps").format(intCount)

lockBreps()