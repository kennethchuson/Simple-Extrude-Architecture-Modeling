

import bpy 



class Mesh_Transformation(object): 
    
    def __init__(self, mesh = None): 
        self.mesh = mesh 
    
    def getLocation_X(self, x): 
        return bpy.context.active_object.location[0] = x
    
    def getLocation_Y(self, y): 
        return bpy.context.active_object.location[1] = y
    
    def getLocation_Z(self, z): 
        return bpy.context.active_object.location[2] = z



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
        else: 
            raise Exception("unknown mesh") 
        return whatMesh 
    



meshDesign = Mesh_Design() 
#meshTransformation = Mesh_Transformation() 

#mesh input
input_one = "sphere"

#location mesh input
input_location_x = 5
input_location_y = 10
input_location_z = 15


meshDesign.getMesh(input_one) 


meshTransformation.getLocation_X(input_location_x) 
meshTransformation.getLocation_Y(input_location_y) 
meshTransformation.getLocation_Z(input_location_z)
