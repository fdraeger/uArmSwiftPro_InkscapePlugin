# Design Aspects

## uArm Specific

 - the area covered by the uArm Swift Pro is not a rectangular shape. This needs to be covered by the plugin in order to avoid movements outside this area.
 - the plugin may create an Inkscape layer which show demarkations of the drawable area. So the user can directly see if the SVG is within this area.
 - yet to be proved: the accuracy of movements of the arm depends on the location within the area. It is presumed that the accuracy is reduced the closer the arm reaches the limits of the area. It needs to be discussed how the plugin deals with this.
 - differences between uArm models: relevant different behaviours w of this plugin with respect to the various uArm models need to be clearly communicated/documented (precision of the uArm Swift Pro is considerably higher than with the other models)
 - G Code: the gcode implemented for the uArm is quite limited. It only supports G0, G1 commands. When it comes to circles, the gcode standard refers to G02,G03 commands which create movement along an arc-segment of a circle. This is not available for uArm yet. Two Options: implement G02 and G03 commands in the uArm firmware or avoid the generation of G02 and G03 in the Inkscape plugin and generate a series of G0/G1 commands instead. Investigate the use of uArm's G2201 command.
 
## Laser Specific

 - for laser engravings speed of arm movement is important. Slower movements lead to more intense "burnings" with the laser. In Inkscape the user should be able to tell the plugin for each line/path, what speed should be applied on this line/path - eg. by assigning different speeds to different colors.
 
## pen specific
 - ...
 
## Inkscape Specific

 - Discuss if the plugin should only use information from a specific Inkscape layer with a specific name.
 - provide settings for uArm parking position. The uArm then moves to this position and allows the user to place the object in front of the arm. The plugin will be paused for this. Once the user continues, the plugin will start printing from the parking position.
 
# Plugin Features

The list below is a working list of features that could be provided.


1. **uArm USB Detection**

   uArms are connected via USB. Provide code which identifies the USB ports which have a uArm connected to them. The plugin will provide a selection of USB interfaces "/dev/tty..." on which it found a uArm. Be as generic as possible. Try to identify the uArm model if possible. Return a list of: device names, uArm Model  
   This information will be used in the plugin uArm tab
 
1. **uArm Serial Comms Parameters**

   The plugin uArm tab will also let you specify connection parameters for the serial interface
 
1. **Safe Area Definition**

   uArm movements are restricted to a specific area. This is partly because of the coordinate model which is built into the firmware, but also to mechanical reasons. The mechanics of the uArm cannot provide the same accuracy to all areas the uArm is technically able to reach. In order to support the user, the plugin should create a new layer in Inkscape which indicates the safe area with a sufficient level of accuracy. The plugin should also generate a graph which indicates the areas, the arm is technically capable of reaching. 


 
 
