import rhinoscriptsyntax as rs


obj_ref = rs.GetObjects("Objects to return to initial position", 0, True, True)


###Return objects from a iteration to the original position
def returnToInitPos(obj):
    ### Get the current layer
    cur_layer = rs.CurrentLayer()
    for i in obj:
        ###Extract the iteration count of the selected objects
        obj_layer = rs.ObjectLayer(i)
        iter_count = obj_layer[obj_layer.find('(')+1:obj_layer.find(')')]
        ###Extract the distance from parent layer
        parent_layer = rs.ParentLayer(obj_layer)
        dist = parent_layer[parent_layer.find('[')+1:parent_layer.find(']')]
        ###Move a copy of objects back
        objBack = rs.CopyObject(i, (float(dist)*(-1)*float(iter_count), 0, 0))
        ### Change the layer to current layer
        pasted_to_layer = rs.ObjectLayer(objBack, cur_layer)
    ### Print the number of object returned
    print('Retured {} objects.'.format(len(obj)))





returnToInitPos(obj_ref)