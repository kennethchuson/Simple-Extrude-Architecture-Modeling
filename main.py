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
            whatMesh = bpy.ops.mesh.primitive_torus_add
        if mesh == "cylinder": 
            whatMesh = bpy.ops.mesh.primitive_cylinder_add()
        if mesh == "plane": 
            whatMesh = bpy.ops.mesh.primitive_plane_add()
        else: 
            raise Exception("unknown mesh") 
        return whatMesh 



meshDesign = Mesh_Design() 

input_one = "plane"
