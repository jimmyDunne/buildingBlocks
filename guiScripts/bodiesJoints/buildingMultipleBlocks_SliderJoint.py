
model  = modeling.Model()
ground = model.getBodySet().get(0)

groundVec3 = modeling.Vec3(0,0,0)
locInParent = modeling.Vec3(0,-0.07,0)
locInChild  = modeling.Vec3(0,0.07,0)


## Create a body, set name, add geomtry, join with ground and add to model 
block = modeling.Body()
block.setName('block')
joint  = modeling.WeldJoint('grd_block',ground,groundVec3,groundVec3,block,locInChild,groundVec3,0)
block.addDisplayGeometry('block.vtp')
block.setJoint(joint)
model.addBody(block)

## Create a body, set name, add geomtry, join with ground and add to model 
block2 = modeling.Body()
block2.setName('block2')
block1.addDisplayGeometry('block.vtp')
# Define the radii of an slider joint
ellipsRadii = modeling.Vec3(0.8,0.8, 0.8)
# Define the joint type as slider
joint1  = modeling.SliderJoint('slider',block,locInParent,groundVec3,block1,locInChild,groundVec3,0)
block1.setJoint(joint1)
model.addBody(block1)

## Edit the min and max range of the Coordinate 
jc = joint1.upd_CoordinateSet()
jc.setName('sliderJoint')
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


model.print('sliderJoint.osim')

loadModel(model)