# Plugin Features

The list below is a working list of features that could be provided.


1. **uArm USB Detection**

   uArms are connected via USB. Provide code which identifies the USB ports which have a uArm connected to them. The plugin will provide a selection of USB interfaces "/dev/tty..." on which it found a uArm. Be as generic as possible. Try to identify the uArm model if possible. Return a list of: device names, uArm Model  
   This information will be used in the plugin uArm tab
 
1. **uArm Serial Comms Parameters**

   The plugin uArm tab will also let you specify connection parameters for the serial interface
 
1. **Safe Area Definition**

   uArm movements are restricted to a specific area. This is partly because of the coordinate model which is built into the firmware, but also to mechanical reasons. The mechanics of the uArm cannot provide the same accuracy to all areas the uArm is technically able to reach. In order to support the user, the plugin should create a new layer in Inkscape which indicates the safe area with a sufficient level of accuracy. The plugin should also generate a graph which indicates the areas, the arm is technically capable of reaching. 
   
1. **Custom Safe Areas**

   Allow the user to define and load external SVG files which define the safe area (optional).

1. **GCode Output**

   Optionally write GCode to a file.
  
1. **Verify Printability**

   Using the Safe Area, the arm will not move outside this area, if this option is selected.
 
 
