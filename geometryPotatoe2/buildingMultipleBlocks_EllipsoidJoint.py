



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
locInParent = modeling.Vec3(-0.05,0.25,0)
oriInParent = modeling.Vec3(0,0,0)
locInChild  = modeling.Vec3(0, 0, 0)
oriInChild = modeling.Vec3(0,0,0)

block1 = modeling.Body()
block1.setName('block1')
# Define the radii of an ellipsoid joint
ellipsRadii = modeling.Vec3(-0.8, -1, -0.8)
# Define the joint type as ellipsoid
joint1  = modeling.EllipsoidJoint('ellipsoidJoint',block,locInParent,oriInParent,block1,locInChild,oriInChild,ellipsRadii,0)
block1.addDisplayGeometry('capitate_largeSmoothed.vtp')
block1.setJoint(joint1)
block1.scale(scalingFactor,1)
model.addBody(block1)

## Edit the min and max range of the Coordinate 
jc = joint1.upd_CoordinateSet()
jc.setName('ellipsoidJoint')
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


model.print('ellipsoid.osim')

loadModel(model)