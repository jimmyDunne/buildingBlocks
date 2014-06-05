## Building a block body that is attached to the ground



model = modeling.Model()
ground = model.getBodySet().get(0)
block = modeling.Body()
block.setName('block')

groundVec3 = modeling.Vec3(0,0,0)

joint  = modeling.FreeJoint('ground_block',ground,groundVec3,groundVec3,block,groundVec3,groundVec3,0)
nCoord = joint.numCoordinates()

block.addDisplayGeometry('block.vtp')


model.addBody(block)

loadModel(model)












