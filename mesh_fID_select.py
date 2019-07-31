import bmesh
import bpy
from bpy.props import BoolProperty, IntProperty, StringProperty
from bpy.types import Panel, Operator, PropertyGroup

bl_info = {
    "name": "Face ID Selector",
    "author": "Trevor Poirier",
    "description": "By face id, select a single face and(or) ranges of faces.",
    "location": "View 3D > Toolbar > Tools tab",
    "category": "Mesh"}

def userSelectionInput(self, context):
    self.ob = bpy.context.active_object
    self.mesh = self.ob.data

    current_scene = bpy.context.scene.name
    bm = bmesh.from_edit_mesh(self.mesh)
    flist = [f for f in bm.faces]
    face_count = len(bm.faces)

    # Visibility of indices choice
    bpy.data.scenes[bpy.context.scene.name].fid_view

    # First Face Selection
    faceEntries = []
    temp_str1 = bpy.data.scenes[current_scene].single1
    single1 = temp_str1.translate({ord(i): None for i in ' .:#\'\"'})
    if single1 != "":
        single1 = int(single1)
        print(single1)
        if single1 in range(face_count):
            faceEntries.append(single1)
        else:
            pass

    # Second Face Selection
    temp_str2 = bpy.data.scenes[current_scene].single2
    single2 = temp_str2.translate({ord(i): None for i in ' .:#\'\"'})
    if single2 != "":
        single2 = int(single2)
        if single2 in range(face_count):
            faceEntries.append(single2)
        else:
            pass

    # Third Face Selection
    temp_str3 = bpy.data.scenes[current_scene].single3
    single3 = temp_str3.translate({ord(i): None for i in ' .:#\'\"'})
    if single3 != "":
        single3 = int(single3)
        if single3 in range(face_count):
            faceEntries.append(single3)
        else:
            pass

    # Fourth Face Selection
    temp_str4 = bpy.data.scenes[current_scene].single4
    single4 = temp_str4.translate({ord(i): None for i in ' .:#\'\"'})
    if single4 != "":
        single4 = int(single4)
        if single4 in range(face_count):
            faceEntries.append(single4)
        else:
            pass

    # Fifth Face Selection
    temp_str5 = bpy.data.scenes[current_scene].single5
    single5 = temp_str5.translate({ord(i): None for i in ' .:#\'\"'})
    if single5 != "":
        single5 = int(single5)
        if single5 in range(face_count):
            faceEntries.append(single5)
        else:
            pass

    # Sixth Face Selection
    temp_str6 = bpy.data.scenes[current_scene].single6
    single6 = temp_str6.translate({ord(i): None for i in ' .:#\'\"'})
    if single6 != "":
        single6 = int(single6)
        if single6 in range(face_count):
            faceEntries.append(single6)
        else:
            pass

    # Seventh Face Selection
    temp_str7 = bpy.data.scenes[current_scene].single7
    single7 = temp_str7.translate({ord(i): None for i in ' .:#\'\"'})
    if single7 != "":
        single7 = int(single7)
        if single7 in range(face_count):
            faceEntries.append(single7)
        else:
            pass

    # Eighth Face Selection
    temp_str8 = bpy.data.scenes[current_scene].single8
    single8 = temp_str8.translate({ord(i): None for i in ' .:#\'\"'})
    if single8 != "":
        single8 = int(single8)
        if single8 in range(face_count):
            faceEntries.append(single8)
        else:
            pass

    # Ninth Face Selection
    temp_str9 = bpy.data.scenes[current_scene].single9
    single9 = temp_str9.translate({ord(i): None for i in ' .:#\'\"'})
    if single9 != "":
        single9 = int(single9)
        if single9 in range(face_count):
            faceEntries.append(single9)
        else:
            pass

    # Ninth Face Selection
    temp_str10 = bpy.data.scenes[current_scene].single10
    single10 = temp_str10.translate({ord(i): None for i in ' .:#\'\"'})
    if single10 != "":
        single10 = int(single10)
        if single10 in range(face_count):
            faceEntries.append(single10)
        else:
            pass

    # Ninth Face Selection
    temp_str11 = bpy.data.scenes[current_scene].single11
    single11 = temp_str11.translate({ord(i): None for i in ' .:#\'\"'})
    if single11 != "":
        single11 = int(single11)
        if single11 in range(face_count):
            faceEntries.append(single11)
        else:
            pass

    # Twelth Face Selection
    temp_str12 = bpy.data.scenes[current_scene].single12
    single12 = temp_str12.translate({ord(i): None for i in ' .:#\'\"'})
    if single12 != "":
        single12 = int(single12)
        if single12 in range(face_count):
            faceEntries.append(single12)
        else:
            pass

    # First selection range
    rs1 = bpy.data.scenes[current_scene].rs1
    re1 = bpy.data.scenes[current_scene].re1
    entryA = range(rs1, re1)

    # Second selection range
    rs2 = bpy.data.scenes[current_scene].rs2
    re2 = bpy.data.scenes[current_scene].re2
    entryB = range(rs2, re2)

    # Third selection range
    rs3 = bpy.data.scenes[current_scene].rs3
    re3 = bpy.data.scenes[current_scene].re3
    entryC = range(rs3, re3)

    # Fourth selection range
    rs4 = bpy.data.scenes[current_scene].rs4
    re4 = bpy.data.scenes[current_scene].re4
    entryD = range(rs4, re4)

    # Fifth selection range
    rs5 = bpy.data.scenes[current_scene].rs5
    re5 = bpy.data.scenes[current_scene].re5
    entryE = range(rs5, re5)

    # Sixth selection range
    rs6 = bpy.data.scenes[current_scene].rs6
    re6 = bpy.data.scenes[current_scene].re6
    entryF = range(rs6, re6)

    ##Press Alt-R to reload the script and start over
      ##with no selections

    bpy.ops.mesh.select_mode(type='FACE')

    for face in flist:
        if face.index in faceEntries:
            face.select = True
        elif face.index in entryA:
            face.select = True
        elif face.index in entryB:
            face.select = True
        elif face.index in entryC:
            face.select = True
        elif face.index in entryD:
            face.select = True
        elif face.index in entryE:
            face.select = True
        elif face.index in entryF:
            face.select = True
        elif face.index not in range(face_count):
            pass
        else:
            face.select = False

    bmesh.update_edit_mesh(self.mesh, True)

    return face_count


class addonProps(PropertyGroup):

    bpy.types.Scene.fid_view = BoolProperty \
      (
        name = "Display in 3D viewport",
        description = "Toggle on or off, then click 'OK'",
        default=False
      )

    bpy.types.Scene.single1 = bpy.props.StringProperty \
      (
      name = "",
      description = "Enter a Face ID integer",
      default = ""
      )

    bpy.types.Scene.single2 = bpy.props.StringProperty \
      (
        name = "",
        description = "Enter a Face ID integer",
        default = ""
      )

    bpy.types.Scene.single3 = bpy.props.StringProperty \
      (
        name = "",
        description = "Enter a Face ID integer",
        default = ""
      )

    bpy.types.Scene.single4 = bpy.props.StringProperty \
      (
        name = "",
        description = "Enter a Face ID integer",
        default = ""
      )

    bpy.types.Scene.single5 = bpy.props.StringProperty \
      (
        name = "",
        description = "Enter a Face ID integer",
        default = ""
      )

    bpy.types.Scene.single6 = bpy.props.StringProperty \
      (
        name = "",
        description = "Enter a Face ID integer",
        default = ""
      )

    bpy.types.Scene.single7 = bpy.props.StringProperty \
      (
        name = "",
        description = "Enter a Face ID integer",
        default = ""
      )

    bpy.types.Scene.single8 = bpy.props.StringProperty \
      (
        name = "",
        description = "Enter a Face ID integer",
        default = ""
      )

    bpy.types.Scene.single9 = bpy.props.StringProperty \
      (
        name = "",
        description = "Enter a Face ID integer",
        default = ""
      )

    bpy.types.Scene.single10 = bpy.props.StringProperty \
      (
        name = "",
        description = "Enter a Face ID integer",
        default = ""
      )

    bpy.types.Scene.single11 = bpy.props.StringProperty \
      (
        name = "",
        description = "Enter a Face ID integer",
        default = ""
      )

    bpy.types.Scene.single12 = bpy.props.StringProperty \
      (
        name = "",
        description = "Enter a Face ID integer",
        default = ""
      )

    bpy.types.Scene.rs1 = bpy.props.IntProperty \
      (
        name = "Start",
        description = "Enter a Face ID integer",
        default = 0,
        min = 0,
        max = 50352
      )
    bpy.types.Scene.re1 = bpy.props.IntProperty \
      (
        name = "Stop",
        description = "Enter a Face ID integer",
        default = 0,
        min = 0,
        max = 50352
      )

    bpy.types.Scene.rs2 = bpy.props.IntProperty \
      (
        name = "Start",
        description = "Enter a Face ID integer",
        default = 0,
        min = 0,
        max = 50352
      )

    bpy.types.Scene.re2 = bpy.props.IntProperty \
      (
        name = "Stop",
        description = "Enter a Face ID integer",
        default = 0,
        min = 0,
        max = 50352
      )
    bpy.types.Scene.rs3 = bpy.props.IntProperty \
      (
        name = "Start",
        description = "Enter a Face ID integer",
        default = 0,
        min = 0,
        max = 50352
      )

    bpy.types.Scene.re3 = bpy.props.IntProperty \
      (
        name = "Stop",
        description = "Enter a Face ID integer",
        default = 0,
        min = 0,
        max = 50352
      )
    bpy.types.Scene.rs4 = bpy.props.IntProperty \
      (
        name = "Start",
        description = "Enter a Face ID integer",
        default = 0,
        min = 0,
        max = 50352
      )

    bpy.types.Scene.re4 = bpy.props.IntProperty \
      (
        name = "Stop",
        description = "Enter a Face ID integer",
        default = 0,
        min = 0,
        max = 50352
      )

    bpy.types.Scene.rs5 = bpy.props.IntProperty \
      (
        name = "Start",
        description = "Enter a Face ID integer",
        default = 0,
        min = 0,
        max = 50352
      )

    bpy.types.Scene.re5 = bpy.props.IntProperty \
      (
        name = "Stop",
        description = "Enter a Face ID integer",
        default = 0,
        min = 0,
        max = 50352
      )

    bpy.types.Scene.rs6 = bpy.props.IntProperty \
      (
        name = "Start",
        description = "Enter a Face ID integer",
        default = 0,
        min = 0,
        max = 50352
      )

    bpy.types.Scene.re6 = bpy.props.IntProperty \
      (
        name = "Stop",
        description = "Enter a Face ID integer",
        default = 0,
        min = 0,
        max = 50352
      )


class fidSelectPanel(Panel):
    bl_label = "Face ID Selector"
    bl_idname = "fidSelectUI"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Tools"

    def draw(self, context):
        self.obj = bpy.context.active_object
        if self.obj.mode == 'EDIT':

            layout = self.layout
            split = layout.split()

            row = layout.row()
            row.scale_y = 1.250
            row.prop(context.scene, "fid_view")
            sub = row.row()

            row = layout.row(align=True)
            row = row.split(percentage=0.175)
            row.operator(
                toggleIndices.bl_idname)

            row = layout.row()
            row.label()

            row = layout.row()
            row = row.split(percentage=0.330)
            row.label()

            row.label("Individual ID #")

            row = layout.row()
            row.prop(context.scene, "single1")
            row.prop(context.scene, "single2")
            row.prop(context.scene, "single3")

            row = layout.row()
            row.prop(context.scene, "single4")
            row.prop(context.scene, "single5")
            row.prop(context.scene, "single6")

            row = layout.row()
            row.prop(context.scene, "single7")
            row.prop(context.scene, "single8")
            row.prop(context.scene, "single9")

            row = layout.row()
            row.prop(context.scene, "single10")
            row.prop(context.scene, "single11")
            row.prop(context.scene, "single12")

            row = layout.row()
            row = row.split(percentage=0.330)
            row.label()

            row.label("Ranges of IDs")

            row = layout.row(align=True)
            row.prop(context.scene, "rs1")
            row.prop(context.scene, "re1")

            row = layout.row(align=True)
            row.prop(context.scene, "rs2")
            row.prop(context.scene, "re2")

            row = layout.row(align=True)
            row.prop(context.scene, "rs3")
            row.prop(context.scene, "re3")

            row = layout.row(align=True)
            row.prop(context.scene, "rs4")
            row.prop(context.scene, "re4")

            row = layout.row(align=True)
            row.prop(context.scene, "rs5")
            row.prop(context.scene, "re5")

            row = layout.row(align=True)
            row.prop(context.scene, "rs6")
            row.prop(context.scene, "re6")

            row = layout.row()
            row.label()

            row = layout.row()
            row.label()
            row.scale_y = 1.200
            row.operator(
                resetValues.bl_idname)
            row.label()

            row = layout.row(align=True)
            row.label()

            sub = row.row()
            sub.scale_x = 3.200
            sub.scale_y = 1.675
            sub.operator(
                selectFaceID.bl_idname)
            sub.operator(
                selectFaceID_add.bl_idname)
            row.label()

            row = layout.row()
            row.label()

            layout.label(text="*A single field value left blank = no selection")
            layout.label(text="*Ranges with 0 for start & stop = no selection")


class selectFaceID(Operator):
    bl_idname = "mesh.select_fid"
    bl_label = (" " * 4+ "Make Selection")
    bl_description = "Click to confirm the selection(s) you have specified"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.select_all(action = 'DESELECT')
        userSelectionInput(self, context)
        bpy.ops.mesh.select_mode(type='FACE')

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}


class selectFaceID_add(Operator):
    bl_idname = "mesh.select_fid_a"
    bl_label = (" " * 4 + "Add to Selection")
    bl_description = "Click to confirm and add the selection(s) you have specified"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        userSelectionInput(self, context)
        bpy.ops.mesh.select_mode(type='FACE')

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}


class toggleIndices(Operator):
    bl_idname = "mesh.view_indices"
    bl_label = (' ' * 4 + 'OK')
    bl_description = "Click to update the 3D View to show face ids"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scn_name = bpy.context.scene.name
        mesh_name = bpy.context.active_object.data.name
        boolOutput = bpy.data.scenes[scn_name].fid_view

        if boolOutput == True:
            bpy.app.debug = True
            bpy.data.meshes[mesh_name].show_extra_indices = True
        else:
            bpy.data.meshes[mesh_name].show_extra_indices = False

        return {'FINISHED'}


class resetValues(Operator):
   bl_idname = "mesh.reset_vals"
   bl_label = " " * 8 + "Reset All"
   bl_description = "Click to return all entries to default (no selections)"
   bl_options = {'REGISTER', 'UNDO'}

   def execute(self, context):

       listProps = ["single1", "single2", "single3", "single4", "single5",
                    "single6", "single7", "single8", "single9", "single10",
                    "single11", "single12", "rs1", "re1", "rs2", "re2",
                    "rs3", "re3", "rs4", "re4", "rs5", "re5", "rs6", "re6"]

       for p in listProps:
           bpy.context.scene.property_unset(p)

       return {'FINISHED'}


def register():
    bpy.utils.register_class(fidSelectPanel)
    bpy.utils.register_class(selectFaceID)
    bpy.utils.register_class(selectFaceID_add)
    bpy.utils.register_class(toggleIndices)
    bpy.utils.register_class(resetValues)
    bpy.utils.register_class(addonProps)


def unregister():
    bpy.utils.unregister_class(fidSelectPanel)
    bpy.utils.unregister_class(selectFaceID)
    bpy.utils.unregister_class(selectFaceID_add)
    bpy.utils.unregister_class(toggleIndices)
    bpy.utils.unregister_class(resetValues)
    bpy.utils.unregister_class(addonProps)


if __name__ == "__main__":
    register()
