import bpy
from random import randint , uniform
import math



for mesh in bpy.data.meshes: #supprime les cubes actuel pour ne pas garder les anciens
    if mesh is not bpy.data.meshes['Plan']:
        bpy.data.meshes.remove(mesh)

RND_VAL =1.5

for i in range (60):
    #genere cubes de tailles et positions aleatoires
    bpy.ops.mesh.primitive_cube_add(size=1,location=(uniform(-RND_VAL,RND_VAL),uniform(-RND_VAL,RND_VAL),uniform(-RND_VAL,RND_VAL)),scale=(uniform(0.5,1),uniform(0.5,1),uniform(0.5,1)))
    
    
    #arrondir les cubes
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='EDGE')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.bevel(offset =0.05 ,segments =4)
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.shade_smooth()

    
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')