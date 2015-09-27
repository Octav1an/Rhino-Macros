import rhinoscriptsyntax as rs
import datetime as dt



def viewportClock():
    now = dt.datetime.now()
    textObjectID = rs.AddText(str(now), (0,0,0), 20)
    if textObjectID is None: return False
    intCount = 0
    
    while intCount < 4:
        rs.Sleep(1000)
        now = dt.datetime.now()
        rs.TextObjectText(textObjectID, str(now))
        intCount += 1
    textDone = rs.ObjectsByType(512)
    print(textDone)
    rs.DeleteObjects(textDone)


if __name__ == "__main__":
    viewportClock()