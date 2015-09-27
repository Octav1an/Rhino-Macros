import rhinoscriptsyntax as rs


def scaleUntill():
    crvSel = rs.GetObject("Select Curve", 4, True)
    if crvSel is None: return
    ptCenter = rs.CurveAreaCentroid(crvSel)
    if ptCenter is None: return
    
    crvLength = rs.CurveLength(crvSel)
    crvLengthLimit = rs.GetReal("Curve length limit: ", crvLength*0.5, crvLength*0.1, crvLength)
    if crvLengthLimit is None: return
    
    while True:
        if rs.CurveLength(crvSel) <= crvLengthLimit: break
        crvSel = rs.ScaleObject(crvSel, ptCenter[0], (0.9, 0.9, 0.9), True)
        if crvSel is None:
            print("Something went wrong")
            return
    print("New Curve length: ", str(rs.CurveLength(crvSel)))


if __name__ == "__main__":
    scaleUntill()