<div align ="center">
	<img src="https://github.com/anprita/images/blob/master/logo.jpg">
</div>

# Watershed Monitoring Tools
#### ArcGIS Python Toolbox version 1 for working with watershed related data in RIGIS and URI Watershed Watch.

The tools and its scripts are prepared by Prita Novita of University of Rhode Island for NRS568 - Final Project. The basic purposes of the toolbox is for watershed management and water quality monitoring program. All tools are released under the MIT License, and no warranty is implied.

The tools are grouped into the following:

* Watershed Tool is a tool for:
  * Counting number of public places (school, home)
  * Calculating length (miles), area (square miles) as well as perimeter (miles) of streams, soils, and wetlands
  * Integrating URI Watershed Watch data (enterococci.csv) into shape files

* Water Quality is a tool for:
  * Creating interpolation using Kriging from all enterococci sampling data
  * Converting vector based of watershed to raster
  * Extracting the interpolating result using raster based of watershed

* Elevation Tools is a tool for
  * Mosaicking tiles of elevation data 
  * Extracting the mosaick of elevation data raster based watershed as mask

#### Instructions

* Data preparation
  * Download this [example_data](https://bit.ly/2vsK8w2) and put it into folder *example_data/input* or you can download directly from RIGIS and URI Watershed Watch
    1. [Watershed boundary](http://www.rigis.org/datasets/watershed-boundary-dataset-huc-12)
    2. [Soils](http://www.rigis.org/datasets/soils)
    3. [Wetlands](http://www.rigis.org/datasets/wetlands-1993)
    4. [Streams](http://www.rigis.org/datasets/freshwater-rivers-and-streams-15000)
    5. [GNIS](http://www.rigis.org/datasets/geographic-names)
    6. [E911 Sites](http://www.rigis.org/datasets/e-911-sites) 
    7. [Elevation](http://www.rigis.org/pages/2011-statewide-lidar-ri-state-plane-feet-dem)
    8. [URI Watershed Monitoring Data](https://web.uri.edu/watershedwatch/uri-watershed-watch-monitoring-data) 

* Download the toolbox
  * Put the toolbox in *root* folder
  * Create new folder *example_data/output* and example_data/temp

* Running the toolbox
  * You can run these scripts in standalone mode, through PyCharm project or as an ArcGIS Toolbox with a GUI (add to ArcToolBox, and navigate to your required tool).
  * It's a sequential process, so you need to start from the first menu (watershed toolbox)
  ** Menu 1: Watershed toolbox
[Image of Toolbox 1](https://github.com/anprita/images/blob/master/menu01_flow.png)
  ** Menu 2: Water quality toolbox
[Image of Toolbox 1](https://github.com/anprita/images/blob/master/menu02_flow.png)
  ** Menu 3: Elevation toolbox
[Image of Toolbox 1](https://github.com/anprita/images/blob/master/menu03_flow.png)
 
 #### Detail Methodology of the toolbox

* Watershed Tools
  * Input : Watershed (HUC12), soils, wetlands, streams, GNI, E911 Sites, Enterococci.csv
  * Output: Map and statistics characteristics of the watershed
  * Method: Select, Clip, Dissolve, Summary Statistics, Add Geometry Attributes, Make XY Event Layer, Copy Features, ProjectManagement

![Image of Toolbox 1](https://github.com/anprita/images/blob/master/toolbox01_method.png)

* Water Quality Tools
  * Input: URI Watershed Watch monitoring data (enterococci), watershed 
  * Output: Kriging Interpolation
  * Method: Add Field, Calculate Field, Kriging, Extract by Mask, Feature to Raster

![Image of Toolbox 1](https://github.com/anprita/images/blob/master/toolbox02_method.png)

* Elevation Tools
  * Input : Elevation of several tiles
  * Output: Elevation of watershed only
  * Method: Mosaic to New Raster, Extract by Mask

![Image of Toolbox 1](https://github.com/anprita/images/blob/master/toolbox03_method.png)

#### Result
 
* Watershed Tools:

![Image of Toolbox 1](https://github.com/anprita/images/blob/master/toolbox01_map.png)

* Water Quality Tools

![Image of Toolbox 2](https://github.com/anprita/images/blob/master/toolbox02_map.png)

* Elevation Tools

![Image of Toolbox 3](https://github.com/anprita/images/blob/master/toolbox03_map.png)
