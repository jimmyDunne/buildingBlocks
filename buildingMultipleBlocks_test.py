## Building a block body that is attached to the ground



model = modeling.Model()
ground = model.getBodySet().get(0)

groundVec3 = modeling.Vec3(0,0,0)
locInParent = modeling.Vec3(0,-0.07,0)
locInChild  = modeling.Vec3(0,0.07,0)
scaleFactor = modeling.Vec3(0,5,0)


block = modeling.Body()
block.setName('block')
joint  = modeling.FreeJoint('grd_block',ground,groundVec3,groundVec3,block,locInChild,groundVec3,0)
block.addDisplayGeometry('block.vtp')
block.setJoint(joint)
block.scale(scaleFactor, 1)


model.addBody(block)


block1 = modeling.Body()
block1.setName('block1')
joint1  = modeling.GimbalJoint('jnt1',block,locInParent,groundVec3,block1,locInChild,groundVec3,0)
block1.addDisplayGeometry('block.vtp')
block1.setJoint(joint1)
model.addBody(block1)

block2 = modeling.Body()
block2.setName('block2')
joint2  = modeling.GimbalJoint('jnt2',block1,locInParent,groundVec3,block2,locInChild,groundVec3,0)
block2.addDisplayGeometry('block.vtp')
block2.setJoint(joint2)
model.addBody(block2)

loadModel(model)












