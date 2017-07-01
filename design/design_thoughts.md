# Design Aspects

## uArm Specific

 - the area covered by the uArm Swift Pro is not a rectangular shape. This needs to be covered by the plugin in order to avoid movements outside this area.
 - the plugin may create an Inkscape layer which show demarkations of the drawable area. So the user can directly see if the SVG is within this area.
 - yet to be proved: the accuracy of movements of the arm depends on the location within the area. It is presumed that the accuracy is reduced the closer the arm reaches the limits of the area. It needs to be discussed how the plugin deals with this.
 
## Laser Specific

 - for laser engravings speed of arm movement is important. Slower movements lead to more intense "burnings" with the laser. In Inkscape the user should be able to tell the plugin for each line/path, what speed should be applied on this line/path - eg. by assigning different speeds to different colors.
 
## pen specific
 - ...
 
## Inkscape Specific

 - Discuss if the plugin should only use information from a specific Inkscape layer with a specific name.
 
