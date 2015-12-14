import rhinoscriptsyntax as rs
import myFunctions as mf
import Rhino


def iterateCopy():
    obj_ref = rs.GetObjects("Select objects to create a iteration", 0, True, True)
    nrObjIteration = rs.GetInteger("Object iteration count", 1)
    if obj_ref is None: return
    ###Creating the bounding box of the objects
    boxCorners = rs.BoundingBox(obj_ref)
    in_ptbase = boxCorners[0]
    ###final_dist = translation distance for the iteration
    final_dist = 0
    if boxCorners:
        ###Cheking the distance x-y
        ###final_dist is the translation dist for iteration
        dist1 = rs.Distance(boxCorners[0], boxCorners[1])
        dist2 = rs.Distance(boxCorners[1], boxCorners[2])
        if dist1 > dist2:
            final_dist = dist1 * 2
        else:
            final_dist = dist2 * 2
    else: return
    
    allLayers = rs.LayerNames()
    print(allLayers[1])
    ###Boolean execute once and if False
    bll_once = False
    ###Making sure we dont repeat ITERATE parent layer 
    for index, layer in enumerate(allLayers):
        if layer.find("ITERATE {}".format(nrObjIteration)) >= 0 and not bll_once:
            bll_once = True
            strParentLayer = layer
    ###Create a new ITERATE layer if it doesnt exists
    if not bll_once:
        strParentLayer = rs.AddLayer("ITERATE {} [{:1.1f}] <{:1.1f}, {:1.1f}, {:1.1f}>"\
        .format(nrObjIteration, final_dist, in_ptbase[0], in_ptbase[1], in_ptbase[2]))

    ###Extract the distance between object from parent layer
    distParent = strParentLayer[strParentLayer.find("[")+1:strParentLayer.find("]")]
    ###Add 1 to have the first layer named 'I - (1)' not zero
    nrIterateChild = rs.LayerChildCount(strParentLayer) + 1
    ###Create sublayer for each iteration
    ###Easier to do the translation math later on
    strLayer = rs.AddLayer("I - ({})".format(nrIterateChild), color = \
    (110, 200, 70), parent = strParentLayer)
    ###Go through all the selected objects and check their layers,
    ###If a least one is form a Iterate child layer do the math for translation...
    I_count = 0
    for index, obj in enumerate(obj_ref):
        obj_l = rs.ObjectLayer(obj)
        if obj_l.find("I - (") >= 0:
            I_count = obj_l[obj_l.find("(")+1:obj_l.find(")")]
        else: I_count = 0
    ###Copy the objects with the necessary distance which is the double of the
    ###longest edge of the bounding box of First selected objects
    obj_iteration = rs.CopyObjects(obj_ref, ((float(distParent) * \
    (int(nrIterateChild) - int(I_count))), 0, 0))
    rs.ObjectLayer(obj_iteration, strLayer)



iterateCopy()