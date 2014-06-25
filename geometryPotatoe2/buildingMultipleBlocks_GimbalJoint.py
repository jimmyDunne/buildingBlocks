## Building a block body that is attached to the ground



model = modeling.Model()
ground = model.getBodySet().get(0)
scalingFactor = modeling.Vec3(0.0333,0.0333,0.0333)

groundVec3 = modeling.Vec3(0,0,0)
locInParent = modeling.Vec3(0,0,0)
locInChild  = modeling.Vec3(0,0.07,0)

block = modeling.Body()
block.setName('block')
joint  = modeling.WeldJoint('WeldJoint',ground,groundVec3,groundVec3,block,locInChild,groundVec3,0)
block.addDisplayGeometry('scaphoid_largeSmoothed.vtp')
block.setJoint(joint)
block.scale(scalingFactor,1)
model.addBody(block)

## Create a body, set name, add geomtry, join with ground and add to model 

groundVec3 = modeling.Vec3(0,0,0)
locInParent = modeling.Vec3(-0.05, -0.35, -0)
oriInParent = modeling.Vec3(0,0,0)
locInChild  = modeling.Vec3(-0.2,0.4,-0.2)
oriInChild = modeling.Vec3(0,1.5,0)

block1 = modeling.Body()
block1.setName('block1')
joint1  = modeling.GimbalJoint('gimbalJoint',block,locInParent,oriInParent,block1,locInChild,oriInChild,0)
block1.addDisplayGeometry('capitate_largeSmoothed.vtp')
block1.setJoint(joint1)
block1.scale(scalingFactor,1)
model.addBody(block1)

## Edit the min and max range of the Coordinate 
jc = joint1.upd_CoordinateSet()
jc.setName('gimbalJoint')
nCoordinates = joint1.getCoordinateSet().getSize()
k = 3.14

nCoordinates = model.getCoordinateSet().getSize()

for i in range(nCoordinates):
    jc.get(i).setRangeMax(k)
    jc.get(i).setRangeMin(-k)

# get bodySet
bs = model.getBodySet()
nBodies = bs.getSize()

for i in range(1,nBodies):
    # get body 
    body = bs.get(i)
    # update the displayer 
    displayer = body.updDisplayer()
    displayer.setShowAxes(1)

# Print the model
model.print('gimbalJoint.osim')
# Load the model in the GUI
loadModel(model)