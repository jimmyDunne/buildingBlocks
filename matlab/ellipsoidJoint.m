



import org.opensim.modeling.*


model  = Model()
ground = model.getBodySet().get(0)

groundVec3 = Vec3(0,0,0)
locInParent = Vec3(0,-0.07,0)
locInChild  = Vec3(0,0.07,0)



%% Block 1
block = Body()
block.setName('block')
joint  = WeldJoint('grd_block',ground,groundVec3,groundVec3,block,locInChild,groundVec3,0)
block.addDisplayGeometry('block.vtp')
block.setJoint(joint)
model.addBody(block)

%% Block 2
block1 = Body()
block1.setName('block1')
% Define the radii of the ellipsoid joint
ellipsRadii = Vec3(0.1,0.2, 0)
% 
joint1  = EllipsoidJoint ('ellipsoid',block,locInParent,groundVec3,block1,locInChild,groundVec3,ellipsRadii ,0)
block1.addDisplayGeometry('block.vtp')
block1.setJoint(joint1)
model.addBody(block1)


jc = joint1().upd_CoordinateSet();


jc.setName('ellipsoidJoint');

coordRange = [-pi/2.0 pi/2.0];

for i = 0 : 2
    jc.get(0).setRange(coordRange);
end


loadModel(model)


















