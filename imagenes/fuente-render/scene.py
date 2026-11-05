import bpy, math, sys, os
from mathutils import Vector
T=os.path.abspath("tex")+"/"
RES=float(sys.argv[-2]); SAMPLES=int(sys.argv[-1])
bpy.ops.wm.read_factory_settings(use_empty=True)
sc=bpy.context.scene
def mat(name,color=(0.8,0.8,0.8),rough=0.5,metal=0.0,img=None,emit=0.0,emit_img=False,noise=None):
    m=bpy.data.materials.new(name); m.use_nodes=True; nt=m.node_tree; b=nt.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value=(*color,1); b.inputs["Roughness"].default_value=rough; b.inputs["Metallic"].default_value=metal
    if img:
        t=nt.nodes.new("ShaderNodeTexImage"); t.image=bpy.data.images.load(T+img)
        nt.links.new(t.outputs["Color"],b.inputs["Base Color"])
        if emit_img:
            nt.links.new(t.outputs["Color"],b.inputs["Emission Color"]); b.inputs["Emission Strength"].default_value=emit
    elif emit>0:
        b.inputs["Emission Color"].default_value=(*color,1); b.inputs["Emission Strength"].default_value=emit
    if noise:
        n=nt.nodes.new("ShaderNodeTexNoise"); n.inputs["Scale"].default_value=noise[0]; n.inputs["Detail"].default_value=12
        mp=nt.nodes.new("ShaderNodeMapping"); mp.inputs["Scale"].default_value=noise[1]
        tc=nt.nodes.new("ShaderNodeTexCoord"); nt.links.new(tc.outputs["Object"],mp.inputs["Vector"]); nt.links.new(mp.outputs["Vector"],n.inputs["Vector"])
        cr=nt.nodes.new("ShaderNodeValToRGB"); cr.color_ramp.elements[0].color=(*noise[2],1); cr.color_ramp.elements[1].color=(*noise[3],1)
        nt.links.new(n.outputs["Fac"],cr.inputs["Fac"]); nt.links.new(cr.outputs["Color"],b.inputs["Base Color"])
    return m
def box(name,loc,size,m,bevel=0.004,rot=(0,0,0)):
    bpy.ops.mesh.primitive_cube_add(location=loc,rotation=rot); o=bpy.context.object; o.name=name
    o.scale=(size[0]/2,size[1]/2,size[2]/2); bpy.ops.object.transform_apply(scale=True)
    if bevel: md=o.modifiers.new("b","BEVEL"); md.width=bevel; md.segments=3
    o.data.materials.append(m); bpy.ops.object.shade_smooth(); return o
def cyl(name,loc,r,depth,m,rot=(0,0,0),verts=48):
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts,radius=r,depth=depth,location=loc,rotation=rot); o=bpy.context.object; o.name=name
    o.data.materials.append(m); bpy.ops.object.shade_smooth(); return o
def uvplane(name,loc,size,m,rot=(0,0,0)):
    bpy.ops.mesh.primitive_plane_add(location=loc,rotation=rot); o=bpy.context.object; o.name=name
    o.scale=(size[0]/2,size[1]/2,1); bpy.ops.object.transform_apply(scale=True); o.data.materials.append(m); return o
# materials
wood=mat("wood",rough=0.35,noise=(3.0,(1,14,1),(0.10,0.05,0.025),(0.22,0.12,0.06)))
floor=mat("floor",(0.05,0.05,0.06),0.6)
wall=mat("wall",(0.10,0.11,0.14),0.8)
alu=mat("alu",(0.55,0.56,0.58),0.3,0.9)
dark=mat("dark",(0.02,0.02,0.025),0.4)
screen=mat("screen",img="screen.png",emit=2.2,emit_img=True,rough=0.2)
paper=mat("paper",img="document.png",rough=0.7)
red=mat("red",(0.55,0.06,0.03),0.25)
card=mat("card",rough=0.85,noise=(40,(1,1,1),(0.42,0.29,0.17),(0.50,0.36,0.22)))
fabric=mat("fabric",(0.04,0.045,0.055),0.9)
city=mat("city",img="city.png",emit=2.5,emit_img=True)
H=0.75
uvplane("floor",(0,0,0),(10,10),floor)
uvplane("wall",(0,1.6,1.5),(10,3),wall,rot=(math.radians(90),0,0))
uvplane("window",(-0.4,1.58,1.55),(2.6,1.5),city,rot=(math.radians(90),0,0))
for x in (-1.72,-0.4,0.92):  # mullions
    box("mull",(x,1.57,1.55),(0.05,0.03,1.55),dark,0)
box("sill",(-0.4,1.57,0.79),(2.7,0.06,0.04),dark,0)
# desk
box("top",(0,0,H-0.02),(1.6,0.8,0.04),wood,0.006)
for x in (-0.76,0.76):
    for y in (-0.36,0.36): box("leg",(x,y,(H-0.04)/2),(0.04,0.04,H-0.04),dark,0.003)
# laptop
lx,ly=0.20,0.10; tilt=math.radians(14)
box("lbase",(lx,ly,H+0.008),(0.34,0.24,0.016),alu,0.004)
box("keys",(lx,ly+0.02,H+0.0165),(0.29,0.11,0.001),mat("keysm",(0.08,0.08,0.09),0.85),0)
hinge=Vector((lx,ly+0.12,H+0.016))
lid=box("lid",hinge+Vector((0,math.sin(tilt)*0.11,math.cos(tilt)*0.11)),(0.34,0.006,0.22),alu,0.003,rot=(-tilt,0,0))
bpy.ops.mesh.primitive_plane_add(); scr=bpy.context.object; scr.scale=(0.16,0.10,1); bpy.ops.object.transform_apply(scale=True)
scr.data.materials.append(screen); scr.rotation_euler=(math.radians(90)-tilt,0,0)
scr.location=hinge+Vector((0,math.sin(tilt)*0.11,math.cos(tilt)*0.11))+Vector((0,-0.0035*math.cos(tilt),0.0035*math.sin(tilt)))
# document and pen
doc=uvplane("doc",(-0.18,-0.12,H+0.0012),(0.21,0.297),paper,rot=(0,0,math.radians(8)))
pen=cyl("pen",(-0.04,-0.16,H+0.006),0.0055,0.14,red,rot=(math.radians(90),0,math.radians(70)))
cyl("pentip",(-0.04+0.07*math.cos(math.radians(160)),-0.16+0.07*math.sin(math.radians(160)),H+0.006),0.003,0.012,alu,rot=(math.radians(90),0,math.radians(70)))
# empty open box
bx,by,bs=-0.40,0.18,0.28; wt=0.004
bm=card
box("bbot",(bx,by,H+0.003),(bs,bs,wt),bm,0.001)
for dx,dy,sx,sy in ((bs/2,0,wt,bs),(-bs/2,0,wt,bs),(0,bs/2,bs,wt),(0,-bs/2,bs,wt)):
    box("bside",(bx+dx,by+dy,H+0.11),(sx,sy,0.22),bm,0.001)
for sign in (-1,1):
    a=math.radians(30); hy=by+sign*bs/2
    box("flap",(bx,hy+sign*0.07*math.cos(a),H+0.22+0.07*math.sin(a)),(bs,0.14,wt),bm,0.001,rot=(sign*a,0,0))
# lamp
lampm=mat("lamp",(0.03,0.03,0.035),0.35,0.6)
def rod(p1,p2,r,m):
    p1=Vector(p1);p2=Vector(p2);v=p2-p1
    bpy.ops.mesh.primitive_cylinder_add(vertices=32,radius=r,depth=v.length,location=(p1+p2)/2)
    o=bpy.context.object; o.rotation_euler=v.to_track_quat('Z','Y').to_euler(); o.data.materials.append(m); bpy.ops.object.shade_smooth(); return o
base_p=(0.50,0.34,H+0.02); elbow=(0.52,0.30,H+0.36); head=(0.36,0.14,H+0.45)
cyl("lbase",(0.50,0.34,H+0.01),0.075,0.02,lampm)
rod(base_p,elbow,0.008,lampm); rod(elbow,head,0.008,lampm)
target_l=Vector((-0.12,-0.10,H))
dl=(target_l-Vector(head)).normalized()
bpy.ops.mesh.primitive_cone_add(vertices=48,radius1=0.075,radius2=0.028,depth=0.12,end_fill_type='NOTHING',location=Vector(head)+dl*0.05)
sh=bpy.context.object; sh.rotation_euler=(-dl).to_track_quat('Z','Y').to_euler(); sh.data.materials.append(lampm)
sol=sh.modifiers.new("s","SOLIDIFY"); sol.thickness=0.002; bpy.ops.object.shade_smooth()
bulb=mat("bulb",(1.0,0.75,0.45),0.2,emit=30)
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.02,location=Vector(head)+dl*0.07); bpy.context.object.data.materials.append(bulb)
bpy.ops.object.light_add(type='SPOT',location=Vector(head)+dl*0.09); sp=bpy.context.object
sp.data.energy=70; sp.data.color=(1.0,0.76,0.5); sp.data.spot_size=math.radians(95); sp.data.spot_blend=0.7; sp.data.shadow_soft_size=0.03
sp.rotation_euler=dl.to_track_quat('-Z','Y').to_euler()
# chair pushed back, rotated
cx,cy=-0.62,-0.72
cyl("cpole",(cx,cy,0.25),0.025,0.4,alu)
for i in range(5):
    a=math.radians(i*72+10); box("cleg",(cx+0.17*math.cos(a),cy+0.17*math.sin(a),0.05),(0.34,0.04,0.03),dark,0.005,rot=(0,0,a))
seat=box("seat",(cx,cy,0.48),(0.48,0.46,0.08),fabric,0.025,rot=(0,0,math.radians(-35)))
back=box("back",(cx-0.13,cy-0.18,0.82),(0.46,0.06,0.55),fabric,0.025,rot=(math.radians(-8),0,math.radians(-35)))
# fill/ambient
bpy.ops.object.light_add(type='AREA',location=(-0.4,1.3,1.6)); a=bpy.context.object; a.data.energy=40; a.data.color=(0.6,0.7,1.0); a.data.size=2.5; a.rotation_euler=(math.radians(-90),0,0)
bpy.ops.object.light_add(type='AREA',location=(0.0,-2.2,2.2)); a=bpy.context.object; a.data.energy=15; a.data.color=(0.8,0.85,1.0); a.data.size=2; a.rotation_euler=(math.radians(55),0,0)
w=bpy.data.worlds.new("w"); sc.world=w; w.use_nodes=True; w.node_tree.nodes["Background"].inputs[0].default_value=(0.01,0.012,0.02,1); w.node_tree.nodes["Background"].inputs[1].default_value=0.5
# camera
bpy.ops.object.camera_add(location=(0.02,-1.12,1.22)); cam=bpy.context.object; sc.camera=cam
target=Vector((-0.05,0.02,H+0.10)); dirv=target-cam.location; cam.rotation_euler=dirv.to_track_quat('-Z','Y').to_euler()
cam.data.lens=40; cam.data.dof.use_dof=True; cam.data.dof.focus_distance=(Vector((-0.12,-0.08,H))-cam.location).length; cam.data.dof.aperture_fstop=2.2
cam.data.shift_y=0.10
r=sc.render; r.engine='CYCLES'; sc.cycles.device='CPU'; sc.cycles.samples=SAMPLES; sc.cycles.use_denoising=True
r.resolution_x=1080; r.resolution_y=1350; r.resolution_percentage=int(RES*100)
sc.view_settings.view_transform='AgX'; sc.view_settings.look='AgX - Medium High Contrast'
r.filepath=os.path.abspath("render.png"); bpy.ops.render.render(write_still=True)
