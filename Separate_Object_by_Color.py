"""
## * Places each object with different collor on different layers, good
for Evermotion 3ds max models.

## * @author Octavian Catlabuga<catlabooga@gmail.com>
 
## * Copyright (c) 2017 Octavian Catlabuga, Berlin, Germany.
"""

import rhinoscriptsyntax as rs


def Separate_On_Layers():
    ## Dictionary to store the colors already used.
    dict_colors = {}
    ## Create a parent layer for the all the other layers.
    layer_parent = Add_Parent_Layer()
    str_select = "Select the objects to sort."
    ref_objs_GUID = rs.GetObjects(str_select, preselect = True)
    if ref_objs_GUID is None: return
    
    for obj_GUID in ref_objs_GUID:
        color_obj = rs.ObjectColor(obj_GUID)
        if len(dict_colors) == 0:
            dict_colors[color_obj] = "obj_0"
            layer_obj = rs.AddLayer(dict_colors[color_obj], color_obj, 
                                                parent=layer_parent)
            rs.ObjectLayer(obj_GUID, layer_obj)
        else:
            is_similar = Check_Color(dict_colors, color_obj)
            if (is_similar):
                layer_to_move = Layer_Color(dict_colors, color_obj)
                rs.ObjectLayer(obj_GUID, layer_to_move)
            else:
                dict_colors[color_obj] = "obj_{}".format(len(dict_colors))
                layer_to_move = rs.AddLayer(dict_colors[color_obj], color_obj, 
                                                        parent = layer_parent)
                rs.ObjectLayer(obj_GUID, layer_to_move)


def Check_Color(dict_colors, color_obj):
    for color, layer in dict_colors.items():
        if color == color_obj: return True

def Layer_Color(dict_colors, color_obj):
    for color, layer in dict_colors.items():
        if color_obj == color: return layer

def Add_Parent_Layer():
    str_msg = "Introduce the Parent Layer name."
    srt_layer_name = rs.GetString(str_msg)
    if not srt_layer_name: return
    layer_parent = rs.AddLayer(srt_layer_name)
    return layer_parent

if __name__ == "__main__":
    Separate_On_Layers()