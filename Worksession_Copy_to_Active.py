"""
## * Worksession copy all files to active maintaining the hierarchy.

## * @author Octavian Catlabuga<catlabooga@gmail.com>
 
## * Copyright (c) 2017 Octavian Catlabuga, Berlin, Germany.
"""

import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino


## 'general_parent' = The main layer everything will be copied to.
general_parent = 'To_Active_Copy'

def prepere_for_duplicating():
    """
    Method that prepares the objects for duplicating. (Copies objs to
    active file).
    Retunrs:
        List of freshly created objects later to be removed.
    """
    ## List to store the created objects.
    coll_dup_objects = []
    str_message = "Select the geometry to export to Copy."
    coll_obj = rs.GetObjects(str_message, 0, True, True)
    if not coll_obj: return
    for obj_item in coll_obj:
        layer_object = rs.ObjectLayer(obj_item)
        coll_split_layer_name = layer_object.split('::')
        ## If the object belongs to another rhino file, the first item 
        ## in the 'coll_split_layer' should be file_name.3dm.
        first_layer_name = coll_split_layer_name[0]
        if '.3dm' in first_layer_name:
            ## Remove the file_name.3dm
            layer_3dm = coll_split_layer_name.pop(0)
            dup_layer(coll_split_layer_name[:], rs.AddLayer(general_parent), 
                                                            obj_item)
            coll_new_path_layer = coll_split_layer_name[:]
            ## Insert the 'To_Active' to have the full layer address.
            coll_new_path_layer.insert(0, general_parent)
            str_new_path_layer = '::'.join(coll_new_path_layer)
            active_obj = copy_object_to_layer(obj_item, str_new_path_layer)
            coll_dup_objects.append(active_obj)
        else:
            ## All the objects from the active file will be copied too with
            ## the help of the folowing lines.
            dup_layer(coll_split_layer_name[:], rs.AddLayer(general_parent), 
                                                            obj_item)
            coll_new_path_layer = coll_split_layer_name[:]
            ## Insert the 'To_Active' to have the full layer address.
            coll_new_path_layer.insert(0, general_parent)
            str_new_path_layer = '::'.join(coll_new_path_layer)
            active_obj = copy_object_to_layer(obj_item, str_new_path_layer)
            coll_dup_objects.append(active_obj)
    ## Check if the layer exists and colapse the layer 'general_parent' which
    ## is the layer all worksession geo is copied ecxept the active fils's geo.
    if rs.IsLayer(general_parent): rs.ExpandLayer(general_parent, False)
    return coll_dup_objects


def copy_object_to_layer(objs,layer):
    """
    Copies the object onto a specified layer and modifies the display mode
    of this object to wireframe for faster performance.
    """
    copy =  rs.CopyObject(objs)
    obj = sc.doc.ActiveDoc.Objects.Find(copy)
    if obj is None:
        print("Sorry, Cannot convert GUID to Rhino Object")
        return
    
    viewportId = sc.doc.Views.ActiveView.ActiveViewportID
    obj_attr = obj.Attributes
    ## Remove the Display Mode Override of obj if it has got one.
    if obj_attr.HasDisplayModeOverride(viewportId):
        print "Removing display mode override from object"
        obj_attr.RemoveDisplayModeOverride(viewportId)
    ## Modify the Object Diplay Mode to Wireframe for faster performance.
    display_mode = Rhino.Display.DisplayModeDescription.FindByName('Wireframe')
    obj_attr.SetDisplayModeOverride(display_mode, viewportId)
    ## IMPORTANT: Update the obj's attributes in scriptcontext
    sc.doc.Objects.ModifyAttributes(obj, obj_attr, False)
    sc.doc.Views.Redraw()
    ## Change objects layer to the correct one.
    rs.ObjectLayer(copy,layer)
    return copy


def dup_layer(coll_layers_parent, layer_parent_copy, obj_to_dup):
    """
    Recursive fuction to create the layers tree.
    Parameters:
        coll_layers_parent = List with obj layer and sublayers (L1::L2::L3)
        layer_parent_copy = (String) Main layer everything will be copied to.
                            in this case "To_Active".
        obj_to_dup = (Rhino Object) Obj to copy.
    """
    new_parent = rs.AddLayer(coll_layers_parent[0], parent = layer_parent_copy)
    obj_layer_last = coll_layers_parent[-1]
    coll_layers_parent.pop(0)
    if len(coll_layers_parent) > 0:
        dup_layer(coll_layers_parent, new_parent, obj_to_dup)


def clean_up(bool_run, coll_objs):
    """
    Remove all the created layers and objects.
    Parameters:
        bool_run = (Boolean) Trigger the function
        coll_objs = (List) with created objects to be removed.
    Returns:
        True if it succesfull, False if fails.
    """
    purge_layer = general_parent
    if not bool_run: return False
    elif rs.IsLayer(purge_layer):
        rc = rs.DeleteObjects(coll_objs)
        print("Removing {} objects".format(rc))
        rc = rs.DeleteLayer(purge_layer)
        print("Removing \'{}\' layer".format(purge_layer))
    return True

def print_result_info(coll_objs):
    if coll_objs is not None:
        print("{} objects were copied".format(len(coll_objs)))
    else:
        print("No Worksession found!!!")
        return


if __name__ == "__main__":
    objs_created = prepere_for_duplicating()
    print_result_info(objs_created)
