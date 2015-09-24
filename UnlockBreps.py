import rhinoscriptsyntax as rs 

def unlockBreps():
	breps = rs.ObjectsByType(16)
	if not breps: 
		print("0 Breps were found")
		return False

	intCount = rs.UnlockObjects(breps)
	print("Unlocked {} Breps").format(intCount)

unlockBreps()