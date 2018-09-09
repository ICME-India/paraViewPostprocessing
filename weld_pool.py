#!/usr/bin/env python

#
# Copyright (c) 2018, Vishal_S
# All rights reserved. Please read the "license.txt" for license terms.
#
# Project Title: paraViewPostprocessing
#
# Developer: Vishal S
#
# Contact Info: vishalsubbu97@gmail.com
#

# Code to calculate the weldpool dimensions
# It writes to boundary.out
# please change the melting point of the alloy
# usgae : vtkpython weld_pool.py <vtk filename>


import vtk
import sys
from vtk import *
from vtk.util.misc import vtkGetDataRoot

output_file = "boundary.out"
file_object = open(output_file,"a")
melting_point = 1355.97
reader =  vtkRectilinearGridReader()
reader.SetFileName(sys.argv[1])
reader.Update()
iso = vtk.vtkContourFilter()
iso.SetNumberOfContours(1) 
iso.SetInputConnection(reader.GetOutputPort())
iso.SetValue(1, melting_point)
iso.Update()
polyData = vtkPolyData()
polyData = iso.GetOutput()
bounds = polyData.GetBounds()
scalarRange = reader.GetOutput().GetPointData().GetScalars().GetRange();
print scalarRange[1]
max_temp = scalarRange[1]
xdist = (bounds[1] - bounds[0] )*1000000
ydist = (bounds[3] - bounds[2] )*1000000
zdist = (bounds[5] - bounds[4] )*1000000

string = sys.argv[1] + "   max_temp  : " 
string = string + str(max_temp)
string = string + "   xdist : "
string = string + str(xdist)
string = string + "   ydist : "
string = string + str(ydist)
string = string + "   zdist : "
string = string + str(zdist)
file_object.write(string + "\n")
file_object.close()
