import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino


### Duplicate a selected face of a Brep
def dupFace():
    ### String of the messege in command line
    msg = "Select a Brep Face"
    ### Filter to select only face/surface
    face_filter = Rhino.DocObjects.ObjectType.Surface
    ### Asign 'objref' the picked face, rc is ressult of this operation(look into
    ### it later)
    ##rc, objref = Rhino.Input.RhinoGet.GetOneObject(msg, False, face_filter)
    rc, obj_coll = Rhino.Input.RhinoGet.GetMultipleObjects(msg, True, face_filter)
    ### If the result of asigning the geo failed return
    if rc!=Rhino.Commands.Result.Success: return
    ### Unselect the referenced faces, later to remain only with dublicated faces
    rs.UnselectObject(obj_coll)
    
    ### Loop through all obj_collection
    for obj_ref in obj_coll:
        ### Get the faces from the selected brep surface
        face = obj_ref.Face()
        ### Duplicate the faces, as output this method is giving the trimmed nurb srf
        face_dup = Rhino.Geometry.BrepFace.DuplicateFace(face, False)
        ### Bake the surface
        bakedSrf = sc.doc.Objects.AddBrep(face_dup)
        ### Select it after baking
        rs.SelectObject(bakedSrf)
        ### Refresh the view(not sure if needed)(look into it later)
        sc.doc.Views.Redraw()


dupFace()