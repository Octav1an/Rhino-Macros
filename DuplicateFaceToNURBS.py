import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino


###Duplicate a selected face of a Brep
def dupFace():
    ###String of the messege in command line
    msg = "Select a Brep Face"
    ###Filter to select only face/surface
    face_filter = Rhino.DocObjects.ObjectType.Surface
    ###Asign 'objref' the picked face, rc is ressult of this operation(look into
    ###it later)
    rc, objref = Rhino.Input.RhinoGet.GetOneObject(msg, False, face_filter)
    ###if the result of asigning the geo failed return
    if rc!=Rhino.Commands.Result.Success: return
    
    ###Get the face from the selected brep surface
    face = objref.Face()
    ###Duplicate the face, as output this method is giving the trimmed nurb srf
    face_dup = Rhino.Geometry.BrepFace.DuplicateFace(face, False)
    ###Bake the surface
    bakedSrf = sc.doc.Objects.AddBrep(face_dup)
    ###Select it after baking
    rs.SelectObject(bakedSrf)
    ###Refresh the view(not sure if needed)(look into it later)
    sc.doc.Views.Redraw()


dupFace()