"""
Test the Python bindings.
"""
import PyOpenColorIO as OCIO

print ""
print "PyOCIO:", OCIO.__file__
print "OCIO:",dir(OCIO)
print "version:",OCIO.version
print ""

#import pydoc
#print pydoc.render_doc(OCIO)

#print dir(OCIO.Config)
#c = OCIO.Config.CreateFromEnv()
#print 'c',c
#print 'isEditable', c.isEditable()
#print "resourcePath: '%s' " % (c.getResourcePath(),)
#c = OCIO.GetCurrentConfig()
#print 'isEditable', c.isEditable()
#print "resourcePath: '%s' " % (c.getResourcePath(),)
#
#OCIO.SetCurrentConfig(c)
#c = OCIO.GetCurrentConfig()
#print ''
#print "ColorSpaces"
#for cs in c.getColorSpaces():
#    print "%s %s %s" % (cs.getName(), cs.getFamily(), cs.getBitDepth())


# Create a new config
"""
config = OCIO.Config()

print 'isEditable', config.isEditable()
print "resourcePath: '%s' " % (config.getResourcePath(),)

# Add a colorspace
cs = OCIO.ColorSpace()
cs.setName("lnh")
cs.setFamily("ln")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F16)
cs.setIsData(False)
cs.setAllocation(OCIO.Constants.ALLOCATION_LG2)
cs.setAllocationVars((-16.0,6.0))

config.addColorSpace(cs)
config.setRole(OCIO.Constants.ROLE_SCENE_LINEAR, cs.getName())

print config.getDefaultLumaCoefs()
#config.setDefaultLumaCoefs((1/3.0,1/3.0,1/3.0))
#print config.getDefaultLumaCoefs()

text = config.serialize()
#print text
"""

"""
config = OCIO.Config.CreateFromEnv()
print 'default display device',config.getDefaultDisplayDeviceName()
for device in config.getDisplayDeviceNames():
    print 'device',device
    print '    default',config.getDefaultDisplayTransformName(device)
    
    for transform in config.getDisplayTransformNames(device):
        print '    transform',transform
"""

"""

    OCIO::ConstColorSpaceRcPtr csSrc = config->getColorSpace("dt8");
    OCIO::ConstColorSpaceRcPtr csDst = config->getColorSpace("lnh");
    
    imageVec[0] = 445.0f/1023.0f;
    imageVec[1] = 1023.0/1023.0f;
    imageVec[2] = 0.0/1023.0f;
    std::cout << csSrc->getName() << " ";
    PrintColor(std::cout, &imageVec[0], "input");
    std::cout << std::endl;
    
    """

"""
config = OCIO.Config.CreateFromEnv()
c1 = config.getColorSpace("lnh")
c2 = config.getColorSpace("dt8")
print c1.getName(), c2.getName()
processor = config.getProcessor("dt8","lnh")
print "processor",processor
print "processor isNoOp",processor.isNoOp()

c = ( 445/1023.0, 1.0, 0.0 )
print processor.applyRGB(c)
"""

"""
#print OCIO.Constants.CombineTransformDirections(OCIO.Constants.TRANSFORM_DIR_INVERSE, OCIO.Constants.TRANSFORM_DIR_INVERSE)

#print dir(OCIO.MatrixTransform)
#print OCIO.MatrixTransform.View((False, False, False, True), (1.0, 1.0, 1.0))
#print OCIO.MatrixTransform.Identity()

"""

"""
config = OCIO.Config()

cs = OCIO.ColorSpace()
cs.setName("lgf")
cs.setFamily("lg")
cs.setBitDepth(OCIO.Constants.BIT_DEPTH_F16)
cs.setIsData(False)
cs.setAllocation(OCIO.Constants.ALLOCATION_LG2)
cs.setAllocationVars((-0.5,1.5))

g = OCIO.GroupTransform()

#t = OCIO.AllocationTransform()
#t.setAllocation(OCIO.Constants.ALLOCATION_LG2)
#t.setVars((-8.0, 8.0))
#g.push_back(t)

t = OCIO.LogTransform()
t.setBase(10.0)
g.push_back(t)

cs.setTransform(g, OCIO.Constants.COLORSPACE_DIR_TO_REFERENCE)


config.addColorSpace(cs)
config.setRole(OCIO.Constants.ROLE_COMPOSITING_LOG, cs.getName())

"""

# config = OCIO.Config.CreateFromEnv()

config = OCIO.Config()
"""

text = config.serialize()
print '\n\n'
print text

fname = '/tmp/a.ocio'
f = file(fname,'w')
f.write(text)
f.close()

newconfig = OCIO.Config.CreateFromFile(fname)

print '\n\n'
print newconfig.serialize()

#print '\n\n'
#print newconfig.serialize()


print newconfig.getDefaultDisplayDevice()
print newconfig.getDisplayDevices()
"""


t = OCIO.CDLTransform()
t.setSOP((1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0))
t.setSat(-0.123454)
t.setID("Taco")
t.setDescription("SDA SKJD ASK")

#print t.getXML()
#
#print dir(t)


t = OCIO.FileTransform()
#t.setSrc("/shots/grn/cc/data/vnp_folders/looks/dc0150_asc/v1/look_dc0150_asc_v1.cc")
t.setSrc("/net/homedirs/jeremys/cdl/./ASC-CDL_dist_v1.2/asc-cdl_test_images/SOP/sop_test_corrections.ccc")
t.setCCCId("$CCID")

p = config.getProcessor(t)
#print dir(p)
