import rhinoscriptsyntax as rs 

def unlockCurves():
	curves = rs.ObjectsByType(4)
	if not curves: 
		print("0 Curves were found")
		return False

	intCount = rs.UnlockObjects(curves)
	print("Unlocked {} Curves").format(intCount)

unlockCurves()