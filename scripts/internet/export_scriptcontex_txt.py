import rhinoscriptsyntax as rs
import scriptcontext as sc

def ExportClassDirectory(direc):
    filter = "Text File (*.txt)|*.txt|All Files (*.*)|*.*||"
    filename = rs.SaveFileName("Save directory as", filter)
    if not filename: return
    namext=filename.split("\\")
    name=namext[-1].split(".")

    file=open(filename,"w")
    file.write(name[0]+"\n\n")
    for item in direc:
        file.write(item+"\n")
    file.close()

direc=dir(sc.doc)
ExportClassDirectory(direc)