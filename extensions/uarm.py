#! /usr/bin/python
# -*- coding: utf-8 -*-
"""

MIT License

Copyright (c) 2017 Frank Dräger

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""


import os
import sys
sys.path.append('/usr/share/inkscape/extensions')

# local library
import inkex
import simplestyle
from simplestyle import *

DEBUG = False

uArmSwiftProInkscapeExtensionVersion = "0.1"

inkex.localize()


def draw_SVG_circle(parent, r, cx, cy, name, style):
    " structre an SVG circle entity under parent "
    circ_attribs = {'style': simplestyle.formatStyle(style),
                    'cx': str(cx), 'cy': str(cy), 
                    'r': str(r),
                    inkex.addNS('label','inkscape'): name,
                    'id':name,
                    'clip-path':"url(#uArm_CutOffBottom)" }
    circle = inkex.etree.SubElement(parent, inkex.addNS('circle','svg'), circ_attribs )


 
		
class uArmSwiftPro(inkex.Effect):
	"""
	main class of this plugin
	"""
	
	uuconv = {'in':90.0, 'pt':1.25, 'px':1.0, 'mm':3.5433070866, 'cm':35.433070866, 'm':3543.3070866,
		  'km':3543307.0866, 'pc':15.0, 'yd':3240.0 , 'ft':1080.0}



	def __init__(self):
		"""
		initialize and parse parameter received. Inkscape passes these from the GUI.
		"""
		inkex.Effect.__init__(self)
		self.OptionParser.add_option("", "--active-tab", action="store", type="string", dest="active_tab", default="", help="Defines which tab is active")
		self.OptionParser.add_option("", "--area-ext-file",  action="store", type="string", dest="area_file", default="./tmp.svg", help="Printable area SVG file")
		self.OptionParser.add_option("", "--unit",  action="store", type="string", dest="unit", default="mm", help="Unit of parameters")

		self.OptionParser.add_option("", "--pos-face",  action="store", type="string", dest="pos_face", default="right", help="X coordinate of robot base center")
		self.OptionParser.add_option("", "--pos-side",  action="store", type="string", dest="pos_side", default="left", help="X coordinate of robot base center")
		self.OptionParser.add_option("", "--side-offset",  action="store", type="float", dest="side_offset", default="120.0", help="Offset of robot origin from selected side")
		self.OptionParser.add_option("", "--pos-align",  action="store", type="string", dest="pos_align", default="center", help="X coordinate of robot base center")

		self.OptionParser.add_option("", "--pos-root-x",  action="store", type="float", dest="pos_root_x", default="0.0", help="X coordinate of robot base center")
		self.OptionParser.add_option("", "--pos-root-y",  action="store", type="float", dest="pos_root_y", default="0.0", help="Y coordinate of robot base center")
#		self.OptionParser.add_option("", "--pos-root-z",  action="store", type="float", dest="pos_root_z", default="0.0", help="Z coordinate of robot base center")
		self.OptionParser.add_option("", "--rotate-root",  action="store", type="float", dest="rotate_root", default="0.0", help="Rotation of robot base center")
		
		"""
		<param name="pen-offset" type="string" _gui-text="Offset of actuator (use either mm,cm,in)" >(0.0mm,0.0mm,0.0mm)</param>
		<param name="pen-defspeed" type="float" _gui-text="Default speed" 	min="0.0" max="5000.0">400</param>
		<param name="pen-z-level" type="float" _gui-text="z-Level for drawing" 	min="-10.0" max="3000.0">100.0</param>
		<param name="pen-start" type="string" _gui-text="Starting position (X,Y,Z) in mm,cm,in" >(120.0mm,0.0mm,50.0mm)</param>
		<param name="pen-end" type="string" _gui-text="End position (X,Y,Z) in mm,cm,in" >(120.0mm,0.0mm,50.0mm)</param>
		<param name="pen-use-polar" type="boolean" gui-text="Use extended arm reach (EXPERIMENTAL)">false</param>
		"""
		self.OptionParser.add_option("", "--pen-offset",  action="store", type="string", dest="pen_offset", default="(0.0mm,0.0mm,0.0mm)", help="Offset of actuator (use either mm,cm,in)")
		self.OptionParser.add_option("", "--pen-defspeed",  action="store", type="float", dest="pen_defspeed", default="400.0", help="Default speed")
		self.OptionParser.add_option("", "--pen-z-level",  action="store", type="float", dest="pen_z-level", default="100.0", help="z-Level for drawing")
		self.OptionParser.add_option("", "--pen-start",  action="store", type="string", dest="pen_start", default="(120.0mm,0.0mm,50.0mm)", help="Starting position (X,Y,Z) in mm,cm,in")
		self.OptionParser.add_option("", "--pen-end",  action="store", type="string", dest="pen_end", default="(120.0mm,0.0mm,50.0mm)", help="End position (X,Y,Z) in mm,cm,in")
		self.OptionParser.add_option("", "--pen-use-polar",  action="store", type="string", dest="pen_use_polar", default="False", help="Use extended arm reach (EXPERIMENTAL)")

		self.OptionParser.add_option("", "--laser-offset",  action="store", type="string", dest="laser_offset", default="(0.0mm,0.0mm,0.0mm)", help="Offset of actuator (use either mm,cm,in)")
		self.OptionParser.add_option("", "--laser-defspeed",  action="store", type="float", dest="laser_defspeed", default="400.0", help="Default speed")
		self.OptionParser.add_option("", "--laser-z-level",  action="store", type="float", dest="laser_z-level", default="100.0", help="z-Level for drawing")
		self.OptionParser.add_option("", "--laser-start",  action="store", type="string", dest="laser_start", default="(120.0mm,0.0mm,50.0mm)", help="Starting position (X,Y,Z) in mm,cm,in")
		self.OptionParser.add_option("", "--laser-end",  action="store", type="string", dest="laser_end", default="(120.0mm,0.0mm,50.0mm)", help="End position (X,Y,Z) in mm,cm,in")
		self.OptionParser.add_option("", "--laser-use-polar",  action="store", type="string", dest="laser_use_polar", default="False", help="Use extended arm reach (EXPERIMENTAL)")

		self.OptionParser.add_option("", "--prt-mode",  action="store", type="string", dest="print_mode", default="Pen", help="Which mode to use: Pen or Laser")

		
	def calcPosition( self, side="left", align="center", face="right" , offset=120.0,  docWidth = 210.0,  docHeight = 297.0 ):
		xPos = 0.0
		yPos = 0.0
		rotation = 0.0
		
				
		# y = 0
		if (side == "top") or \
		(side == "left" and align == "left") or \
		(side == "right" and align =="right") :
			y = 0.0
			
		# y = max
		if (side == "bottom") or \
		(side == "left" and align == "right") or \
		(side == "right" and align =="left") :
			y = float(docHeight)
			
		# y = middle
		if ((side == "left") and (align == "center")) or \
		((side == "right") and (align == "center")):
			y = float(docHeight)/2.0
			
		# x = 0
		if (side == "left") or \
		(side == "top" and align == "right") or \
		(side == "bottom" and align =="left") :
			x = 0.0
			
		# x = max
		if (side == "right") or \
		(side == "top" and align == "left") or \
		(side == "bottom" and align =="right") :
			x = float(docWidth)
			
		# x = middle
		if ((side == "top") and (align == "center")) or \
		((side == "bottom") and (align == "center")):
			x = float(docWidth)/2.0
			
		
		# rotation
		if face == "up":
			rotation = 270.0
		if face == "down":
			rotation = 90.0
		if face == "left":
			rotation = 180.0
		if face == "right":
			rotation = 0.0
			
		# offset gives the distance of the robots center off the document side
		if side == "top":
			y = y - offset
		elif side == "right":
			x = x + offset
		elif side == "bottom":
			y = y + offset
		elif side == "left":
			x = x - offset
		
		return (x,y,rotation)




	def effect(self) :

		# the active_tab tells us, on which dialog the Apply button has been pressed.
		if self.options.active_tab == '"help"' :
			#inkex.errormsg(str(sys.argv[1:]))		# show all arguments passed by Inkscape
			return
			
		elif self.options.active_tab == '"about"' :
			#inkex.errormsg("This is just displaying information. Nothing to apply here.\n")
			return

			
		elif self.options.active_tab in ['"area"','"position"'] :
			#
			if (1==2) and self.doc_ids.has_key('uArmLayer') :
				strMessage = "As of now, the uArm Print Area cannot be updated.\nFor now, you need to remove the 'uArmLayer' layer first, before creating a new one." 
				if DEBUG: inkex.errormsg(strMessage)
				#return

			# Add layer and draw printable area
			#
			# now the real thing
			svg = self.document.getroot()

			"""
			find out what unit are being used in the document and with the extensions parameters
			"""
			width  = self.unittouu(svg.get('width'))
			height = self.unittouu(svg.attrib['height'])
			namedview = svg.find(inkex.addNS("namedview","sodipodi"))
			docunit = namedview.get(inkex.addNS('document-units','inkscape'))

			# TODO: different behaviour between area and position !!!
			
			posX = self.options.pos_root_x * self.uuconv[self.options.unit]
			posY = self.options.pos_root_y * self.uuconv[self.options.unit]

			if self.options.active_tab == '"area"':
				posX,posY,posRot = self.calcPosition( self.options.pos_side, 
					self.options.pos_align, 
					self.options.pos_face, 
					self.uuconv[self.options.unit]*self.options.side_offset, 
					width, height )
			elif self.options.active_tab == '"position"':
				posX = self.options.pos_root_x * self.uuconv[self.options.unit]
				posY = self.options.pos_root_y * self.uuconv[self.options.unit]
				posRot = self.options.rotate_root
				
			self.options.pos_root_x = posX
			self.options.pos_root_y = posY
			self.options.rotate_root = posRot
			
			if DEBUG:
				strScaleInfo = "width: %s, unittouu(width): %.2f, document unit is: %s, parameters in: %s" % (svg.get('width'), width, docunit, self.options.unit)
				strScaleInfo = strScaleInfo + ("\nposx: %.2f, posy: %.2f\n" % ( posX, posY ))
				inkex.errormsg( "\n" + strScaleInfo + "\n" )

			# We now create an SVG group element ( 'g' ) and "mark" it as a layer using Inkscape' SVG extensions:
			mylayer = inkex.etree.SubElement(svg, 'g')
			mylayer.set('id', 'uArmLayer' ) # same id overwrites
			mylayer.set(inkex.addNS('label', 'inkscape'), 'uArmLayer' )
			mylayer.set(inkex.addNS('groupmode', 'inkscape'), 'layer')
			
			# this string is placed in the svg layer with the id 'uArmLayer' at the attribute transform
			# It will be parsed and used to identify the robot position and orientation
			# This information will be used to transform the coordinates to the uArm prints
			# exactly as indicated. 
			strTransform = "translate(%.2f,%.2f) rotate(%.2f)" % (posX,posY,posRot) 
			
			# Make a nice useful name
			g_attribs = { 'id':'uArm_Placement',
				inkex.addNS('label','inkscape'): 'uArmPlacement',
				inkex.addNS('transform-center-x','inkscape'): str(posX),
				inkex.addNS('transform-center-y','inkscape'): str(posY),
				'transform': strTransform ,
				'info':'uArm Robot placement information' }
			# add the group to the document's current layer
			layer = inkex.etree.SubElement(mylayer, 'g', g_attribs )
			
			defs_attribs = { 'id':'uArm_Defs'}
			defs = inkex.etree.SubElement(layer, 'defs', defs_attribs )
			layer.append(defs)
			
			clip_attribs = { "id":"uArm_CutOffBottom" }
			clip = inkex.etree.SubElement(defs, 'clipPath', clip_attribs )
			defs.append(clip)
			
			cliprect_attribs = { 'x':'0mm', 'y':'-355mm', 'height':'710mm', 'width':'352mm' ,'id':'uArm_4713' }
			clipRect = inkex.etree.SubElement(clip, 'rect', cliprect_attribs )
			
			marker_attribs = { inkex.addNS('stockid','inkscape'): "Arrow2Lend", 'orient':'auto', 'refY':'0.0', 'refX':'0.0',
			'id':'Arrow2Lend', 'style':'overflow:visible;', inkex.addNS('isstock','inkscape'): 'true' }
			marker = inkex.etree.SubElement(defs, 'marker', marker_attribs )
			
			mpath_attribs = {'id':'uArm_4715', 
			'style':'fill-rule:evenodd;stroke-width:0.625;stroke-linejoin:round;stroke:#000000;stroke-opacity:1;fill:#000000;fill-opacity:1',
			'd':'M 8.7185878,4.0337352 L -2.2072895,0.016013256 L 8.7185884,-4.0017078 C 6.9730900,-1.6296469 6.9831476,1.6157441 8.7185878,4.0337352 z ',
			'transform':'scale(1.1) rotate(180) translate(1,0)'}
			mpath = inkex.etree.SubElement(marker, 'path', mpath_attribs )
			
			clip.append(clipRect)

			
			style1 = { 'stroke': '#000000', 'fill': 'none', 'stroke-width': '1' , 'stroke-paint': 'flat-color' }
			draw_SVG_circle(layer, '100mm', '0mm', '0mm', 'uArm_Inner', style1)
			
			rect = inkex.etree.Element(inkex.addNS('rect', 'svg' ))
			rect.set('height', '110mm')
			rect.set('width', '110mm')
			rect.set('x', '-55mm')
			rect.set('y', '-55mm')
			rect.set('style', formatStyle(style1))
			layer.append(rect)
			
			style2 = { 'stroke': '#00FF00', 'fill': 'none', 'stroke-width': '1' , 'stroke-paint': 'flat-color' }
			draw_SVG_circle(layer, '300mm', '0mm', '0mm', 'uArm_Middle', style2)
			
			style3 = { 'stroke': '#FF0000', 'fill': 'none', 'stroke-width': '1' , 'stroke-paint': 'flat-color' }
			draw_SVG_circle(layer, '350mm', '0mm', '0mm', 'uArm_Outer', style3)

			lstyle = { "fill":"none", "fill-rule":"evenodd", "stroke":"#000000", "stroke-width":"1.00", "stroke-linecap":"butt", 
			"stroke-linejoin":"miter", "stroke-opacity":"1", "stroke-miterlimit":"4", "stroke-dasharray":"8.00000072,2.00000018,1.00000009,2.00000018", 
			"stroke-dashoffset":"0" } 
			line = inkex.etree.Element(inkex.addNS('path', 'svg' ))
			line.set('id', 'uArm_4716')
			line.set('d', 'm 0,-1281.3421 0,2553.105')
			line.set( inkex.addNS('connector-curvature','inkscape'),'0')
			line.set('style', formatStyle(lstyle))
			layer.append(line)
			
			arrowstyle = { 'fill':'none','fill-rule':'evenodd','stroke':'#000000','stroke-width':'1.0','stroke-linecap':'butt',
			'stroke-linejoin':'miter','stroke-opacity':'1','stroke-miterlimit':'4','stroke-dasharray':'8.00000072,2.00000018,1.00000009,2.00000018',
			'stroke-dashoffset':'0' }
			arrow = inkex.etree.Element(inkex.addNS('path', 'svg' ))
			arrow.set('d','m 0.0,0.0 105.8205,0')
			arrow.set('id','uArm_4717')
			arrow.set( inkex.addNS('connector-curvature','inkscape'),'0')
			arrow.set('style', "fill:none;fill-rule:evenodd;stroke:#000000;stroke-width:1.0;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1;marker-end:url(#Arrow2Lend)" )
			layer.append(arrow)
   
			if DEBUG: print inkex.etree.tostring(svg,pretty_print=True)
			return
			
			
		elif self.options.active_tab == '"params"' :
			tmpStr = str(sys.argv[1:]) + "\n\n"
			inkex.errormsg(tmpStr)		# show all arguments passed by Inkscape
			return
			
		elif self.options.active_tab == '"print"' :
			tmpStr = str(sys.argv[1:]) + "\n\n"
			inkex.errormsg(tmpStr)		# show all arguments passed by Inkscape
			
			return
			
		
#						
uArm = uArmSwiftPro()
uArm.affect()					

