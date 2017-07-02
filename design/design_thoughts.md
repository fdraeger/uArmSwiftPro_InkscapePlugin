# Design Aspects

## uArm Specific

 - the area covered by the uArm Swift Pro is not a rectangular shape. This needs to be covered by the plugin in order to avoid movements outside this area.
 - the plugin may create an Inkscape layer which show demarkations of the drawable area. So the user can directly see if the SVG is within this area.
 - yet to be proved: the accuracy of movements of the arm depends on the location within the area. It is presumed that the accuracy is reduced the closer the arm reaches the limits of the area. It needs to be discussed how the plugin deals with this.
 - differences between uArm models: relevant different behaviours w of this plugin with respect to the various uArm models need to be clearly communicated/documented (precision of the uArm Swift Pro is considerably higher than with the other models)
 - G Code: the gcode implemented for the uArm is quite limited. It only supports G0, G1 commands. When it comes to circles, the gcode standard refers to G02,G03 commands which create movement along an arc-segment of a circle. This is not available for uArm yet. Two Options: implement G02 and G03 commands in the uArm firmware or avoid the generation of G02 and G03 in the Inkscape plugin and generate a series of G0/G1 commands instead.
 
## Laser Specific

 - for laser engravings speed of arm movement is important. Slower movements lead to more intense "burnings" with the laser. In Inkscape the user should be able to tell the plugin for each line/path, what speed should be applied on this line/path - eg. by assigning different speeds to different colors.
 
## pen specific
 - ...
 
## Inkscape Specific

 - Discuss if the plugin should only use information from a specific Inkscape layer with a specific name.
 - provide settings for uArm parking position. The uArm then moves to this position and allows the user to place the object in front of the arm. The plugin will be paused for this. Once the user continues, the plugin will start printing from the parking position.
 
 
