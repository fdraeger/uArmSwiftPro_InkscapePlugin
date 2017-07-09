#! /usr/bin/python
"""

MIT License

Copyright (c) 2017 fdraeger

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



uArmSwiftProInkscapeExtensionVersion = "0.1"

inkex.localize()


def draw_SVG_circle(parent, r, cx, cy, name, style):
    " structre an SVG circle entity under parent "
    circ_attribs = {'style': simplestyle.formatStyle(style),
                    'cx': str(cx), 'cy': str(cy), 
                    'r': str(r),
                    inkex.addNS('label','inkscape'): name,
                    'id':name,
                    'clip-path':"url(#uA-cut-off-bottom)" }
    circle = inkex.etree.SubElement(parent, inkex.addNS('circle','svg'), circ_attribs )


 
		
class uArmSwiftPro(inkex.Effect):
	"""
	main class of this plugin
	"""

	def __init__(self):
		"""
		initialize and parse parameter received. Inkscape passes these from the GUI.
		"""
		inkex.Effect.__init__(self)
		self.OptionParser.add_option("",   "--active-tab", action="store", type="string", dest="active_tab", default="", help="Defines which tab is active")
		self.OptionParser.add_option("", "--area-ext-file",  action="store", type="string", dest="area_file", default="./uArmSwiftPro_Max.svg", help="Printable area SVG file")

		self.OptionParser.add_option("", "--pos-root-x",  action="store", type="float", dest="pos_root_x", default="0.0", help="X coordinate of robot base center")
		self.OptionParser.add_option("", "--pos-root-y",  action="store", type="float", dest="pos_root_y", default="0.0", help="Y coordinate of robot base center")
		self.OptionParser.add_option("", "--pos-root-z",  action="store", type="float", dest="pos_root_z", default="0.0", help="Z coordinate of robot base center")
		self.OptionParser.add_option("", "--rotate-root",  action="store", type="float", dest="rotate_root", default="0.0", help="Rotation of robot base center")


	def effect(self) :
		# the active_tab tells us, on which dialog the Apply button has been pressed.
		if self.options.active_tab == '"help"' :
			inkex.errormsg(str(sys.argv[1:]))		# show all arguments passed by Inkscape
			return
			
		elif self.options.active_tab == '"about"' :
			#inkex.errormsg("This is just displaying information. Nothing to apply here.\n")
			return
			
		elif self.options.active_tab in ['"area"','"position"'] :
			#
			if self.doc_ids.has_key('uA4711') :
				strMessage = "As of now, the uArm Print Area cannot be updated.\nFor now, you need to remove the 'uArmLayer' layer first, before creating a new one." 
				inkex.errormsg(strMessage)
				#return

			# Add layer and draw printable area
			#
			# now the real thing
			svg = self.document.getroot()

			width  = self.unittouu(svg.get('width'))
			height = self.unittouu(svg.attrib['height'])

			# We now create an SVG group element ( 'g' ) and "mark" it as a layer using Inkscape' SVG extensions:
			mylayer = inkex.etree.SubElement(svg, 'g')
			mylayer.set('id', 'uA4711' ) # same id overwrites
			mylayer.set(inkex.addNS('label', 'inkscape'), 'uArmLayer' )
			mylayer.set(inkex.addNS('groupmode', 'inkscape'), 'layer')
			
			# DEBUG Output ot other informatione
			strTransform = "translate(%.2f,%.2f) rotate(%.2f)" % (self.options.pos_root_x,self.options.pos_root_y,self.options.rotate_root) 
			strErrorMessage = strTransform
			#inkex.errormsg(strErrorMessage)
			
			# Make a nice useful name
			g_attribs = { inkex.addNS('label','inkscape'): 'useful name' + str( 24 ),
				inkex.addNS('transform-center-x','inkscape'): str(self.options.pos_root_x),
				inkex.addNS('transform-center-y','inkscape'): str(self.options.pos_root_y),
				'transform': strTransform ,
				'info':'N: '+str(24)+'; with:'+ str(1.0) }
			# add the group to the document's current layer
			layer = inkex.etree.SubElement(mylayer, 'g', g_attribs )
			
			defs_attribs = { 'id':'uA4712'}
			defs = inkex.etree.SubElement(layer, 'defs', defs_attribs )
			layer.append(defs)
			
			clip_attribs = { "id":"uA-cut-off-bottom" }
			clip = inkex.etree.SubElement(defs, 'clipPath', clip_attribs )
			defs.append(clip)
			
			cliprect_attribs = { 'x':'0mm', 'y':'-355mm', 'height':'710mm', 'width':'352mm' ,'id':'uA4713' }
			clipRect = inkex.etree.SubElement(clip, 'rect', cliprect_attribs )
			
			marker_attribs = { inkex.addNS('stockid','inkscape'): "Arrow2Lend", 'orient':'auto', 'refY':'0.0', 'refX':'0.0',
			'id':'Arrow2Lend', 'style':'overflow:visible;', inkex.addNS('isstock','inkscape'): 'true' }
			marker = inkex.etree.SubElement(defs, 'marker', marker_attribs )
			
			mpath_attribs = {'id':'uA4715', 
			'style':'fill-rule:evenodd;stroke-width:0.625;stroke-linejoin:round;stroke:#000000;stroke-opacity:1;fill:#000000;fill-opacity:1',
			'd':'M 8.7185878,4.0337352 L -2.2072895,0.016013256 L 8.7185884,-4.0017078 C 6.9730900,-1.6296469 6.9831476,1.6157441 8.7185878,4.0337352 z ',
			'transform':'scale(1.1) rotate(180) translate(1,0)'}
			mpath = inkex.etree.SubElement(marker, 'path', mpath_attribs )
			
			clip.append(clipRect)

			
			style1 = { 'stroke': '#000000', 'fill': 'none', 'stroke-width': '1' , 'stroke-paint': 'flat-color' }
			draw_SVG_circle(layer, '100mm', '0mm', '0mm', 'uAInner', style1)
			
			rect = inkex.etree.Element(inkex.addNS('rect', 'svg' ))
			rect.set('height', '110mm')
			rect.set('width', '110mm')
			rect.set('x', '-55mm')
			rect.set('y', '-55mm')
			rect.set('style', formatStyle(style1))
			layer.append(rect)
			
			style2 = { 'stroke': '#00FF00', 'fill': 'none', 'stroke-width': '1' , 'stroke-paint': 'flat-color' }
			draw_SVG_circle(layer, '300mm', '0mm', '0mm', 'uAMiddle', style2)
			
			style3 = { 'stroke': '#FF0000', 'fill': 'none', 'stroke-width': '1' , 'stroke-paint': 'flat-color' }
			draw_SVG_circle(layer, '350mm', '0mm', '0mm', 'uAOuter', style3)

			lstyle = { "fill":"none", "fill-rule":"evenodd", "stroke":"#000000", "stroke-width":"1.00", "stroke-linecap":"butt", 
			"stroke-linejoin":"miter", "stroke-opacity":"1", "stroke-miterlimit":"4", "stroke-dasharray":"8.00000072,2.00000018,1.00000009,2.00000018", 
			"stroke-dashoffset":"0" } 
			line = inkex.etree.Element(inkex.addNS('path', 'svg' ))
			line.set('id', 'uA4716')
			line.set('d', 'm 0,-1281.3421 0,2553.105')
			line.set( inkex.addNS('connector-curvature','inkscape'),'0')
			line.set('style', formatStyle(lstyle))
			layer.append(line)
			
			arrowstyle = { 'fill':'none','fill-rule':'evenodd','stroke':'#000000','stroke-width':'1.0','stroke-linecap':'butt',
			'stroke-linejoin':'miter','stroke-opacity':'1','stroke-miterlimit':'4','stroke-dasharray':'8.00000072,2.00000018,1.00000009,2.00000018',
			'stroke-dashoffset':'0' }
			arrow = inkex.etree.Element(inkex.addNS('path', 'svg' ))
			arrow.set('d','m 0.0,0.0 105.8205,0')
			arrow.set('id','uA4717')
			arrow.set( inkex.addNS('connector-curvature','inkscape'),'0')
			arrow.set('style', "fill:none;fill-rule:evenodd;stroke:#000000;stroke-width:1.0;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1;marker-end:url(#Arrow2Lend)" )
			layer.append(arrow)
   
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

