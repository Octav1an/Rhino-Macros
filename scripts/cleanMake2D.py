import rhinoscriptsyntax as rs


def cleanMake2D():
    ###Save default absolute tolerance
    fAbsTolDef = rs.UnitAbsoluteTolerance()
    ###Get a new user defined tolerance
    fNewAbsTol = rs.GetReal("Absolute Tolerance: ", fAbsTolDef, 0.0000001, 1)
    ###Change the default absolute tolerance
    rs.UnitAbsoluteTolerance(fNewAbsTol)
    ###Call the Make2D command
    rs.Command("_Make2D")
    ###Asign to a variable the curves created from Make2D in array
    crvMake2DCurves = rs.LastCreatedObjects()
    ###Aborts the script if there is no curves
    if not crvMake2DCurves: return False
    
    ###Go through array of curves
    for i in range(0, len(crvMake2DCurves)):
        ###Find out the length of the curves
        crvLength = rs.CurveLength(crvMake2DCurves[i])
        ###If its smaller then absolute tolerance, remove it
        if(crvLength<fAbsTolDef):
            rs.DeleteObject(crvMake2DCurves[i])
        ###If its smaller the absolute tolerance *10 then select it
        elif(crvLength<(fAbsTolDef*10)):
            rs.SelectObject(crvMake2DCurves[i])
        ###Deselect all the others
        else:
            rs.UnselectObject(crvMake2DCurves[i])
        
    ###Restore the default absolute tolerance of the file
    rs.UnitAbsoluteTolerance(fAbsTolDef)

cleanMake2D()