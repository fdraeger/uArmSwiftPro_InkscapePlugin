# uArmSwiftPro_InkscapePlugin
Plugin development for uArmSwiftPro robotic arm to allow drawing SVG with pen and laser directly from Inkscape.

This project **just started**. Comments, suggestions and contribution is welcomed! 
Printing is not yet implemented. Help with coding, testing and documentation is highly welcomed!


The uArm Swift Pro robotic arm has a limited area of activity. Accuracy on the outer regions of this
area may also be reduced. The idea behind this plugin is to place the uArm 
towards the Inkscape drawing and use the activity area with the optimum precision and accuracy.

The plugin creates an additional layer to your Inkscape drawing. In this layer you can define how the uArm 
should be positioned towards your drawing. The data fo your drawing will be transformed during printing and the 
the result should be exactly as shown on the layer of this plugin.

The following should provide an idea of how it works:
![Area Tab Example][AreaTabExample]

This example is a quick and easy way to place the uArm on the edges of a document.

If a more exact placement is required, the Position Tab can be used:

![Position Tab Example][PositionTabExample]



This project is based on the following projects:

| Project                    | Description                                                                                                                                                                                                                                                                                                                                      | Link                                                      |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| uARM                       | robotic arm from uFactory. Reads G-code similar commands on serial interface.comes with laser, pen holder, openMV, suction cup, etc.  [uArm Swift Pro Quickstart Guide](http://download.ufactory.cc/docs/en/uArm-Swift-Pro-Quick-Start-Guide-1.0.pdf)                                                                                              | [uFactory](http://ufactory.cc/#/en/support/)              |
| Fellow uArm user  | Richard Garsthagen, a fellow uArm user from the facbook forum started a github repository for uArm code. Here, in issue #2, a SVG printing code sample was posted.  | [uArmProPython github](https://github.com/AnykeyNL/uArmProPython)              |
| pyuarm                     | Python library for the uArm robotic arm.                                                                                                                                                                                                                                                                                                         | [pyuarm](https://pyuarm.readthedocs.io/en/dev/index.html) |
| Inkscape                   | The major SVG editor. We choose this to control the uArm Swift Pro to draw and laser.Wiki with documentation can be found at: [Inkscape Wiki](http://wiki.inkscape.org/wiki/index.php/Inkscape). Information on writing Inkscape extensions: [Inkscape Extensions](https://inkscape.org/en/develop/extensions/) and [Inkscape Wiki](http://wiki.inkscape.org/wiki/index.php/Script_extensions). Also check the plugin development tutorial at [Inkscape Wiki PythonEffect Tutorial](http://wiki.inkscape.org/wiki/index.php/PythonEffectTutorial) | [Inkscape](https://inkscape.org/en/)                      |
| gcodetools                 | A generic plugic which creates G-Code for CNC routers.                                                                                                                                                                                                                                                                                           | [Gcodetools](http://www.cnc-club.ru/gcodetools)           |
| G Code                 | Reference Specification for G Code                                                                                                                                                                                                                                                                                           | [G Codes](http://linuxcnc.org/docs/html/gcode.html)           |
| G Code Simulation      | There is a web-based simulator which is quite useful for debugging                                                                                                                                                                                                                                                                                           | [G Code Simultor](https://nraynaud.github.io/webgcode/)           |
| EggBot Plugin for Inkscape | A valuable source for an initial version of the uArm Swift Pro Inkscape plugin. Python code is well written and stable. This code adresses a completely different device (actually it is painting on eggs), but it is a good start to see how Inkscape plugins work.                                                                             |  [EggBot](http://egg-bot.com/)                            |
| Inkscape Extension Template | The inkscape doc refers to this project which has been designed to be used as a template for Inkscape extensions. It demonstrates all features. | [Inkscpae Extension Template](https://github.com/Neon22/inkscape_extension_template) |



[AreaTabExample]: https://github.com/fdraeger/uArmSwiftPro_InkscapePlugin/blob/master/design/AreaTab_Example.png "Area Tab Example"

[PositionTabExample]: https://github.com/fdraeger/uArmSwiftPro_InkscapePlugin/blob/master/design/PositionTab_Example.png "Position Tab Example"

