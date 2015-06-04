
import org.opensim.modeling.*


model = Model()
ground = model.getBodySet().get(0)

groundVec3 = Vec3(0,0,0)
locInParent = Vec3(0,-0.07,0)
locInChild  = Vec3(0,0.07,0)

block = Body()
block.setName('block')
joint  = FreeJoint('grd_block',ground,groundVec3,groundVec3,block,locInChild,groundVec3,0)
block.addDisplayGeometry('block.vtp')
block.setJoint(joint)
model.addBody(block)


block1 = Body()
block1.setName('block1')
joint1  = PinJoint('jnt1',block,locInParent,groundVec3,block1,locInChild,groundVec3,0)
block1.addDisplayGeometry('block.vtp')
block1.setJoint(joint1)
model.addBody(block1)

maxIso     = 1000

xValues = [-1 -0.5 -0.2 0 0.01 0.02 0.03 0.04 0.05 0.06 0.07 0.1 0.13 0.15 0.2 0.4 0.7 1];
yValues = [0 0 0 0 0.00083333 0.00333333 0.0075 0.0133333 0.0208333 0.03 0.04 0.07 0.1 0.12 0.17 0.37 0.67 0.97];
%scatter(xValues, yValues)
fLc = SimmSpline ;


for i = 1:length(xValues)
        
    fLc.addPoint( xValues(i), yValues(i));
    
end


ligament = Ligament()
ligament.setName('lateralLigament')
ligament.getGeometryPath.appendNewPathPoint('lateralLigament-P1',block, Vec3(0,0,0.05))
ligament.getGeometryPath.appendNewPathPoint('lateralLigament-P2',block1, Vec3(0,0,0.05))
ligament.setMaxIsometricForce(maxIso)
ligament.setRestingLength(0.1400)
ligament.setForceLengthCurve(fLc)
model.addForce(ligament)

ligament1 = Ligament()
ligament1.setName('MedialLigament')
ligament1.getGeometryPath.appendNewPathPoint('MedialLigament-P1',block, Vec3(0,0,-0.05))
ligament1.getGeometryPath.appendNewPathPoint('MedialLigament-P2',block1, Vec3(0,0,-0.05))
ligament1.setMaxIsometricForce(maxIso)
ligament1.setRestingLength(0.1400)
ligament1.setForceLengthCurve(fLc)
model.addForce(ligament1)

ligament2 = Ligament()
ligament2.setName('internalLigament')
ligament2.getGeometryPath.appendNewPathPoint('internalLigament-P1',block,  Vec3(0,-0.05,0))
ligament2.getGeometryPath.appendNewPathPoint('internalLigament-P2',block1, Vec3(0,0.05,0))
ligament2.setMaxIsometricForce(maxIso)
ligament2.setRestingLength(0.04)
ligament2.setForceLengthCurve(fLc)
model.addForce(ligament2)



ligament3 = Ligament()
ligament3.setName('crossLigament')
ligament3.getGeometryPath.appendNewPathPoint('crossLigament-P1',block,  Vec3(0.05,-0.05,0.05))
ligament3.getGeometryPath.appendNewPathPoint('crossLigament-P2',block1, Vec3(-0.05,0.05,-0.05))
ligament3.setMaxIsometricForce(maxIso)
ligament3.setRestingLength(0.147)
ligament3.setForceLengthCurve(fLc)
model.addForce(ligament3)



state = model.initSystem()


model.getForceSet.getSize


model.print('LigamentModel.osim')
































