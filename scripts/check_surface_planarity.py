import rhinoscriptsyntax as rs


def check_planarity():
    ref_srf = rs.GetObject("Select Surface to Check Planarity", 0, True)
    if (rs.IsSurface(ref_srf) and rs.IsSurfacePlanar(ref_srf)):
        print("Surface is Planar")
        return
    elif (not rs.IsSurface(ref_srf)):
        print("This is not a Surface")
        return
    else:
        print("Not Planar, Shit")
        return


check_planarity()