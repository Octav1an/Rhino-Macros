import rhinoscriptsyntax as rs

###Toggle Osnap Near On/Off
def OsnapNear():
    ###Scring with the opstion to toggle(near osnap)
    strNear = "n"
    ###Rhino command of Osnap
    rs.Command("_-Osnap" + ' ' + strNear + ' ' + " Enter")
    print("Near_On/Off")


OsnapNear()