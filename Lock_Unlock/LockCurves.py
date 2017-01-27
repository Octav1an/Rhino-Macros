import rhinoscriptsyntax as  rs

def lockCurves():
	curves = rs.ObjectsByType(4)
	if not curves: 
		print("0 Curves were found")
		return False
	intCount = rs.LockObjects(curves)
	print("Locked {} Curves").format(intCount)

lockCurves()
