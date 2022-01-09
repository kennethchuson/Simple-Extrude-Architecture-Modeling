import bpy 

class Mesh_Design(object): 
    
    whatMesh = None
    
    def getMesh(self, mesh): 
        if mesh == "cube": 
            whatMesh = bpy.ops.mesh.primitive_cube_add()
        if mesh == "sphere": 
            whatMesh = bpy.ops.mesh.primitive_uv_sphere_add()
        if mesh == "cone": 
            whatMesh = bpy.ops.mesh.primitive_cone_add()
        if mesh == "torus": 
            whatMesh = bpy.ops.mesh.primitive_torus_add()
        if mesh == "cylinder": 
            whatMesh = bpy.ops.mesh.primitive_cylinder_add()
        if mesh == "plane": 
            whatMesh = bpy.ops.mesh.primitive_plane_add() 
        return whatMesh 
    


#mesh input
input_one = "cone"

#location mesh input
input_location_x = 5
input_location_y = 10
input_location_z = 15


meshDesign = Mesh_Design()



meshDesign.getMesh(input_one) 

#location mesh
bpy.context.active_object.location[0] = input_location_x
bpy.context.active_object.location[1] = input_location_y
bpy.context.active_object.location[2] = input_location_z
