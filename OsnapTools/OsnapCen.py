import rhinoscriptsyntax as rs

###Toggle Osnap Center On/Off
def OsnapCen():
    ###Scring with the opstion to toggle(center osnap)
    strNear = "c"
    ###Rhino command of Osnap
    rs.Command("_-Osnap" + ' ' + strNear + ' ' + " Enter")
    print("Cen_On/Off")


OsnapCen()