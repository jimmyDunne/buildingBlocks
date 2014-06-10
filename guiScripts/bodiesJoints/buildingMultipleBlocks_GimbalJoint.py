## Building a block body that is attached to the ground



model = modeling.Model()
ground = model.getBodySet().get(0)

groundVec3 = modeling.Vec3(0,0,0)
locInParent = modeling.Vec3(0,-0.07,0)
locInChild  = modeling.Vec3(0,0.07,0)

block = modeling.Body()
block.setName('block')
joint  = modeling.WeldJoint('gimbalJoint',ground,groundVec3,groundVec3,block,locInChild,groundVec3,0)
block.addDisplayGeometry('block.vtp')
block.setJoint(joint)
model.addBody(block)

## Create a body, set name, add geomtry, join with ground and add to model 
block1 = modeling.Body()
block1.setName('block1')
joint1  = modeling.GimbalJoint('gimbalJoint',block,locInParent,groundVec3,block1,locInChild,groundVec3,0)
block1.addDisplayGeometry('block.vtp')
block1.setJoint(joint1)
model.addBody(block1)

## Edit the min and max range of the Coordinate 
jc = joint1.upd_CoordinateSet()
jc.setName('gimbal')
nCoordinates = joint1.getCoordinateSet().getSize()
k = 3.14

nCoordinates = model.getCoordinateSet().getSize()

for i in range(nCoordinates):
    jc.get(i).setRangeMax(k)
    jc.get(i).setRangeMin(-k)

# get bodySet
bs = model.getBodySet()
nBodies = bs.getSize()

for i in range(1,nCoordinates):
    # get body 
    body = bs.get(i)
    # update the displayer 
    displayer = body.updDisplayer()
    displayer.setShowAxes(1)

# Print the model
model.print('gimbalJoint.osim')
# Load the model in the GUI
loadModel(model)



