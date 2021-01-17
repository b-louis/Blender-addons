import bpy

def main(context):
    asko_value = 0.0
    objects = context.selected_objects
    print("-- Shape keys set to "+str(asko_value)+" for :")
    for object in objects :
        print(object.data.name)
        if object.type == "MESH" :
            shape_keys = object.data.shape_keys
            if shape_keys != None:
                for shape_key in shape_keys.key_blocks :
                    print(shape_key)
                    shape_key.value = asko_value
    print("--")

class Asko(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.asko"
    bl_label = "All Shape Keys at Once"

    @classmethod
    def poll(cls, context):
        return context.selected_objects is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}
    
class AskoPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Shape Keys Utils"
    bl_idname = "OBJECT_PT_skut"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        obj = context.object
        objs = context.selected_objects
        row = layout.row()
        row.label(text="WIP", icon='SHAPEKEY_DATA')

        row = layout.row()
        row.label(text="Active object is: " + obj.name)
        
        shape_keys = obj.data.shape_keys
        if shape_keys != None:
            for shape_key in shape_keys.key_blocks :
                print(shape_key)
                row = layout.row()
                row.label(text="Shape : " +shape_key.name)
                row.prop(shape_key, "value")

        row = layout.row()
        print(Asko)
        row.operator("object.asko")
        row = layout.row()
        row.label(text="Will be set to 0 ", icon='SHAPEKEY_DATA')
        for i in objs :
            row = layout.row()
            row.label(text="-> " + i.name) 
            
        

def test():
    return 0

def register():
    bpy.utils.register_class(Asko)
    bpy.utils.register_class(AskoPanel)


def unregister():
    bpy.utils.unregister_class(Asko)
    bpy.utils.unregister_class(AskoPanel)


if __name__ == "__main__":
    register()
