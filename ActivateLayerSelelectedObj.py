import rhinoscriptsyntax as rs


def activateLayerSelectedObj():
    ###Make the current layer the selected object layer
    ###Select object
    obj_ref = rs.GetObject("Select Object", 0, True)
    if(obj_ref == None):
        print("Nothing Selected. Upss")
        return None
    ###Get the object layer
    obj_layer = rs.ObjectLayer(obj_ref)
    ###Make current layer the object layer
    if obj_layer != None:
        rs.CurrentLayer(obj_layer)
    else:
        return
        ###Print the name of the current layer
    print("Layer ' {} ' activated.".format(obj_layer))
    


activateLayerSelectedObj()