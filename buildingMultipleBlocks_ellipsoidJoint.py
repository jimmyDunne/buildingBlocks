



model  = modeling.Model()
ground = model.getBodySet().get(0)

groundVec3 = modeling.Vec3(0,0,0)
locInParent = modeling.Vec3(0,-0.07,0)
locInChild  = modeling.Vec3(0,0.07,0)



## Block 1
block = modeling.Body()
block.setName('block')
joint  = modeling.WeldJoint('grd_block',ground,groundVec3,groundVec3,block,locInChild,groundVec3,0)
block.addDisplayGeometry('block.vtp')
block.setJoint(joint)
model.addBody(block)

## Block 2
block1 = modeling.Body()
block1.setName('block1')
# Define the radii of the ellipsoid joint
ellipsRadii = modeling.Vec3(0.1,0.2, 0)
# 
joint1  = modeling.EllipsoidJoint ('ellipsoid',block,locInParent,groundVec3,block1,locInChild,groundVec3,ellipsRadii ,0)
block1.addDisplayGeometry('block.vtp')
block1.setJoint(joint1)
model.addBody(block1)


## edit the coordinates
jc = joint1().upd_CoordinateSet()
jc.setName('ellipsoidJoint')
k = -3.14/2

coordRange =  modeling.Vec2(k,k)


coD = modeling.ArrayDouble.populateFromVector(coordRange)





for i in range(2):
    jc.get(0).setRange(coordRange)
end

loadModel(model)






