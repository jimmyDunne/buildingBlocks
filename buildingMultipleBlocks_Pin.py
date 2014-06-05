## Building a block body that is attached to the ground



model = modeling.Model()
ground = model.getBodySet().get(0)

groundVec3 = modeling.Vec3(0,0,0)
locInParent = modeling.Vec3(0,-0.07,0)
locInChild  = modeling.Vec3(0,0.07,0)

block = modeling.Body()
block.setName('block')
joint  = modeling.FreeJoint('grd_block',ground,groundVec3,groundVec3,block,locInChild,groundVec3,0)
block.addDisplayGeometry('block.vtp')
block.setJoint(joint)
model.addBody(block)


block1 = modeling.Body()
block1.setName('block1')
joint1  = modeling.PinJoint('jnt1',block,locInParent,groundVec3,block1,locInChild,groundVec3,0)
block1.addDisplayGeometry('block.vtp')
block1.setJoint(joint1)
model.addBody(block1)

block2 = modeling.Body()
block2.setName('block2')
joint2  = modeling.PinJoint('jnt2',block1,locInParent,groundVec3,block2,locInChild,groundVec3,0)
block2.addDisplayGeometry('block.vtp')
block2.setJoint(joint2)
model.addBody(block2)

block3 = modeling.Body()
block3.setName('block3')
joint3  = modeling.PinJoint('jnt3',block2,locInParent,groundVec3,block3,locInChild,groundVec3,0)
block3.addDisplayGeometry('block.vtp')
block3.setJoint(joint3)
model.addBody(block3)


block4 = modeling.Body()
block4.setName('block4')
joint4  = modeling.PinJoint('jnt4',block3,locInParent,groundVec3,block4,locInChild,groundVec3,0)
block4.addDisplayGeometry('block.vtp')
block4.setJoint(joint4)
model.addBody(block4)


block5 = modeling.Body()
block5.setName('block5')
joint5  = modeling.PinJoint('jnt5',block4,locInParent,groundVec3,block5,locInChild,groundVec3,0)
block5.addDisplayGeometry('block.vtp')
block5.setJoint(joint5)
model.addBody(block5)


block6 = modeling.Body()
block6.setName('block6')
joint6  = modeling.PinJoint('jnt6',block5,locInParent,groundVec3,block6,locInChild,groundVec3,0)
block6.addDisplayGeometry('block.vtp')
block6.setJoint(joint6)
model.addBody(block6)


block7 = modeling.Body()
block7.setName('block7')
joint7  = modeling.PinJoint('jnt7',block6,locInParent,groundVec3,block7,locInChild,groundVec3,0)
block7.addDisplayGeometry('block.vtp')
block7.setJoint(joint7)
model.addBody(block7)


block8 = modeling.Body()
block8.setName('block8')
joint8  = modeling.PinJoint('jnt8',block7,locInParent,groundVec3,block8,locInChild,groundVec3,0)
block8.addDisplayGeometry('block.vtp')
block8.setJoint(joint8)
model.addBody(block8)
loadModel(model)












