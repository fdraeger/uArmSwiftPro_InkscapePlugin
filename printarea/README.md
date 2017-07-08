# Print Area

The uArm Swift Pro activity area is limited due to mechanical constraints.

The SVG file in this directory marks the area the uArm can reach. This drawing will be used by the plugin 
and will be loaded into a separate Inkscape layer. This will help users to align their drawings and make sure
they fit within the acitiviy area of the robotic arm.

<img src="https://github.com/fdraeger/uArmSwiftPro_InkscapePlugin/blob/master/printarea/uArmSwiftPro_Max.svg" 
alt="uArmSwiftPro_Max.svg" width="240" height="600" border="10" />

Users can also manually load the uArmSwiftPro_Max.svg file into Inkscape as a reference. 

## Issues with the Activity Area

As of the current version of the arm, there is an inconsistent behaviour iwht regard to how GCode commands are executed.

Moving the arm using polar coordinates allow to reach a larger range than usind cartesian coordinates.

Example:

Using polar coordinates :

`G2201 S350 R1 H50` moves to the rightmost location

`G0 X0.2 Y-350 Z50` moves to Y=300 and **not** beyond

The green line in the activity area drawing indicates the maximum reach when using cartesian coordinates: a radius of 300.

