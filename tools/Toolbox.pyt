# Import modules
import arcpy, shutil, os

# Activate the spatial analyst tool
arcpy.CheckOutExtension("spatial")
arcpy.env.overwriteOutput = True

class Toolbox(object):
    def __init__(self):
        self.label = "Watershed Monitoring Tool"
        self.alias = "Watershed Monitoring Tool"

        # List of tool classes associated with this toolbox
        self.tools = [Tool1, Tool2, Tool3]


class Tool1(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Menu 1: Watershed Tool"
        self.description = "Creating watershed tool for counting number of public places (school, home), calculating length, area, as well as perimeter of streams,Watershed soils, and wetlands, integrating uri watershed watch of enterococci.csv into shape file"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []

        # Create workspace
        workspace = arcpy.Parameter(name="workspace",
                                    displayName="Workspace",
                                    datatype="DEFolder",
                                    parameterType="Required",  # Required|Optional|Derived
                                    direction="Input",  # Input|Output
                                    )
        params.append(workspace)

        # Input watershed
        input_watershed = arcpy.Parameter(name="input_watershed",
                                        displayName="Input all watershed in Rhode Island",
                                        datatype="DEFeatureClass",
                                        parameterType="Required",  # Required|Optional|Derived
                                        direction="Input",  # Input|Output
                                        )
        params.append(input_watershed)

        # Input GNIS11
        input_gni = arcpy.Parameter(name="input_gni",
                                     displayName="Input all GNI Site in Rhode Island",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        params.append(input_gni)

        # Input E911
        input_e911 = arcpy.Parameter(name="input_e911",
                                        displayName="Input all E911 Site in Rhode Island",
                                        datatype="DEFeatureClass",
                                        parameterType="Required",  # Required|Optional|Derived
                                        direction="Input",  # Input|Output
                                        )
        params.append(input_e911)

        # Input Soil
        input_soil = arcpy.Parameter(name="input_soil",
                                     displayName="Input all soil in Rhode Island",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        params.append(input_soil)

        # Input Wetland
        input_wetland = arcpy.Parameter(name="input_wetland",
                                     displayName="Input all wetland in Rhode Island",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        params.append(input_wetland)

        # Input Stream
        input_stream = arcpy.Parameter(name="input_stream",
                                        displayName="Input all stream in Rhode Island",
                                        datatype="DEFeatureClass",
                                        parameterType="Required",  # Required|Optional|Derived
                                        direction="Input",  # Input|Output
                                        )
        params.append(input_stream)

        # Input Enterococci
        input_enterococci = arcpy.Parameter(name="input_enterococci",
                                       displayName="Input all enterococci sampling data in Rhode Island",
                                       datatype="DEFile",
                                       parameterType="Required",  # Required|Optional|Derived
                                       direction="Input",  # Input|Output
                                       )
        params.append(input_enterococci)

        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        # Get input value
        workspace = parameters[0].valueAsText
        input_watershed = parameters[1].valueAsText
        input_gni = parameters[2].valueAsText
        input_e911 = parameters[3].valueAsText
        input_soil = parameters[4].valueAsText
        input_wetland = parameters[5].valueAsText
        input_stream = parameters[6].valueAsText
        input_enterococci = parameters[7].valueAsText

        # Get temp and output value
        output_directory = str(workspace) + "\\output\\"
        temp_directory = str(workspace) + "\\temp\\"
        Watershed_shp = str(output_directory) + "Watershed.shp"
        GNI_shp = str(temp_directory) + "GNI.shp"
        School_shp = str(output_directory) + "School.shp"
        Stat_School = str(output_directory) + "Stat_School"
        E911_shp = str(temp_directory) + "E911.shp"
        Residential_shp = str(output_directory) + "Residential.shp"
        Stat_Residential = str(output_directory) + "Stat_Residential"
        Soil_shp = str(temp_directory) + "Soil.shp"
        Soils_shp = str(output_directory) + "Soils.shp"
        Wetland_shp = str(temp_directory) + "Wetland.shp"
        Wetlands_shp = str(output_directory) + "Wetlands.shp"
        Stream_shp = str(temp_directory) + "Stream.shp"
        Streams_shp = str(output_directory) + "Streams.shp"
        enteroLayer = "enteroLayer"
        EnteroWGS_shp = str(temp_directory) + "EnteroWGS.shp"
        Enterococci = str(output_directory) + "Enterococci.shp"

        # Create temporary directory if doesn't exists
        if not os.path.exists(temp_directory):
            os.mkdir(temp_directory)
            arcpy.AddMessage("------------- Temporary directory created [" + str(temp_directory) + "]------------- ")

        # Delete output directory
        if os.path.exists(output_directory):
            shutil.rmtree(output_directory)
            arcpy.AddMessage(
                "------------- Old output directory has been deleted [" + str(output_directory) + "]------------- ")

        # Create output directory if doesn't exists
        if not os.path.exists(output_directory):
            os.mkdir(output_directory)
            arcpy.AddMessage("------------- Output directory created [" + str(output_directory) + "]------------- ")

            arcpy.AddMessage("------------- Menu #1 : Watershed toolbox starts processing ------------- ")

        # Process: Select
        arcpy.Select_analysis(input_watershed, Watershed_shp, "\"HUC_12\" ='010900040903'")
        arcpy.AddMessage("Step 1 of 19: Watershed has been selected successfully")

        # Process: Clip (8)
        arcpy.Clip_analysis(input_gni, Watershed_shp, GNI_shp, "")
        arcpy.AddMessage("Step 2 of 19: GNI Sites has been clipped successfully")

        # Process: Select (2)
        arcpy.Select_analysis(GNI_shp, School_shp, "FEAT_CLASS = 'School'")
        arcpy.AddMessage("Step 3 of 19: School have been selected from GNI Sites successfully")

        # Process: Summary Statistics
        arcpy.Statistics_analysis(School_shp, Stat_School, "FID COUNT", "")
        arcpy.AddMessage("Step 4 of 19: Number of schools has been calculated successfully")

        # Process: Clip (3)
        arcpy.Clip_analysis(input_e911, Watershed_shp, E911_shp, "")
        arcpy.AddMessage("Step 5 of 19: E911 Sites have been clipped successfully")

        # Process: Select (3)
        arcpy.Select_analysis(E911_shp, Residential_shp,
                              "SiteType = 'R1' OR SiteType = 'R2' OR SiteType = 'R4' OR SiteType = 'R6' ")
        arcpy.AddMessage("Step 6 of 19: Homes have been selected from E911 Sites successfully")

        # Process: Summary Statistics (2)
        arcpy.Statistics_analysis(Residential_shp, Stat_Residential, "FID COUNT", "")
        arcpy.AddMessage("Step 7 of 19: Number of homes has been calculated successfully")

        # Process: Clip
        arcpy.Clip_analysis(input_soil, Watershed_shp, Soil_shp, "")
        arcpy.AddMessage("Step 8 of 19: Soils have been clipped successfully")

        # Process: Dissolve
        arcpy.Dissolve_management(Soil_shp, Soils_shp, "HYDRIC", "", "MULTI_PART", "DISSOLVE_LINES")
        arcpy.AddMessage("Step 9 of 19: Soils have been dissolved based on HYDRIC type successfully")

        # Process: Add Geometry Attributes
        arcpy.AddGeometryAttributes_management(Soils_shp, "AREA;PERIMETER_LENGTH", "MILES_US", "SQUARE_MILES_US", "")
        arcpy.AddMessage(
            "Step 10 of 19: The area (miles) and perimeter (square miles) of soils  have been calculated successfully")

        # Process: Clip (2)
        arcpy.Clip_analysis(input_wetland, Watershed_shp, Wetland_shp, "")
        arcpy.AddMessage("Step 11 of 19: Wetlands have been clipped successfully")

        # Process: Dissolve (2)
        arcpy.Dissolve_management(Wetland_shp, Wetlands_shp, "JURIS", "", "MULTI_PART", "DISSOLVE_LINES")
        arcpy.AddMessage("Step 12 of 19: Wetlands have been dissolve based on JURIS TYPE successfully")

        # Process: Add Geometry Attributes (2)
        arcpy.AddGeometryAttributes_management(Wetlands_shp, "AREA;PERIMETER_LENGTH", "MILES_US", "SQUARE_MILES_US", "")
        arcpy.AddMessage(
            "Step 13 of 19: The area (miles) and perimeter (square miles) of wetlands have been calculated successfully")

        # Process: Clip (7)
        arcpy.Clip_analysis(input_stream, Watershed_shp, Stream_shp, "")
        arcpy.AddMessage("Step 14 of 19: Streams have been clipped successfully")

        # Process: Dissolve (3)
        arcpy.Dissolve_management(Stream_shp, Streams_shp, "StrmOrder", "", "MULTI_PART", "DISSOLVE_LINES")
        arcpy.AddMessage("Step 15 of 19: Streams have been dissolved based on STREAM ORDER successfully")

        # Process: Add Geometry Attributes (3)
        arcpy.AddGeometryAttributes_management(Streams_shp, "LENGTH", "MILES_US", "", "")
        arcpy.AddMessage("Step 16 of 19: The length of streams has been calculated successfully")

        # Process: Make XY Event Layer
        arcpy.MakeXYEventLayer_management(input_enterococci, "Long", "lat", enteroLayer,
                                          "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;.001;.001;IsHighPrecision",
                                          "Depth")
        arcpy.AddMessage("Step 17 of 19: Enterococci monitoring data has been made to XY Event Layer successfully")

        # Process: Copy Features
        arcpy.CopyFeatures_management(enteroLayer, EnteroWGS_shp, "", "0", "0", "0")
        arcpy.AddMessage("Step 18 of 19: Feature class Enterococci monitoring data has been created successfully")

        # Process: Project
        arcpy.Project_management(EnteroWGS_shp, Enterococci,
                                 "PROJCS['NAD_1983_StatePlane_Rhode_Island_FIPS_3800_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',328083.3333333333],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-71.5],PARAMETER['Scale_Factor',0.99999375],PARAMETER['Latitude_Of_Origin',41.08333333333334],UNIT['Foot_US',0.3048006096012192]]",
                                 "WGS_1984_(ITRF00)_To_NAD_1983",
                                 "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]",
                                 "NO_PRESERVE_SHAPE", "", "NO_VERTICAL")
        arcpy.AddMessage(
            "Step 19 of 19: Feature class Enterococci monitoring data projected to NAD_1983_StatePlane_Rhode_Island_FIPS_3800_Feet successfully")

        arcpy.AddMessage("------------- Menu #1 : Watershed toolbox finishes processing ------------- ")

        # Delete temporary directory
        if os.path.exists(temp_directory):
            shutil.rmtree(temp_directory)
            arcpy.AddMessage(
                "------------- Temporary directory has been deleted [" + temp_directory + "]------------- ")
        return

class Tool2(object):
    def __init__(self):
        self.label = "Menu 2: Water quality tool"
        self.description = "Creating water quality tool for creating interpolation using Kriging from all sampling data, converting watershed (vector) to raster, extracting the interpolation result using raster of watershed as mask"
        self.canRunInBackground = False

    def getParameterInfo(self):
        params = []
        # Create workspace
        workspace = arcpy.Parameter(name="workspace",
                                    displayName="Workspace",
                                    datatype="DEFolder",
                                    parameterType="Required",  # Required|Optional|Derived
                                    direction="Input",  # Input|Output
                                    )
        params.append(workspace)
        input_enterococci = arcpy.Parameter(name="input_enterococci",
                                     displayName="Input Enterococci shapefile that has been generated from Menu 1: Watershed tool",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        params.append(input_enterococci)
        input_watershed = arcpy.Parameter(name="input_watershed",
                                        displayName="Input Watershed shapefile that has been generated from Menu 1: Watershed tool",
                                        datatype="DEFeatureClass",
                                        parameterType="Required",  # Required|Optional|Derived
                                        direction="Input",  # Input|Output
                                        )
        params.append(input_watershed)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):

        # Get input value
        workspace = parameters[0].valueAsText
        input_enterococci = parameters[1].valueAsText
        input_watershed = parameters[2].valueAsText

        # Get temp and output value
        output_directory = str(workspace) + "\\output\\"
        temp_directory = str(workspace) + "\\temp\\"
        enterococci_shp_1 = input_enterococci
        enterococci_shp_2 = enterococci_shp_1
        kriging_all = output_directory + "krigingAll.TIF"
        kriging = output_directory + "kriging.TIF"
        Output_variance_of_prediction_raster = ""
        raster_watershed = output_directory + "rasterWatershed.TIF"

        # Create temporary directory if doesn't exists
        if not os.path.exists(temp_directory):
            os.mkdir(temp_directory)
            arcpy.AddMessage("------------- Temporary directory created [" + str(temp_directory) + "]-------------")

        # Create output directory if doesn't exists
        if not os.path.exists(output_directory):
            os.mkdir(output_directory)
            arcpy.AddMessage("------------- Output directory created [" + str(output_directory) + "]-------------")

        arcpy.AddMessage("------------- Menu #2 : Water quality toolbox starts processing -------------")

        # Process: Add Field
        arcpy.AddField_management(input_enterococci, "NValue", "FLOAT", "12", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
        arcpy.AddMessage("Step 1 of 5: New field (NValue) has been added successfully")

        # Process: Calculate Field
        arcpy.CalculateField_management(enterococci_shp_1, "NValue", "[CVALUE]", "VB", "")
        arcpy.AddMessage("Step 2 of 5: NValue has been updated with the concentration value (CVALUE)  successfully")

        # Process: Kriging
        arcpy.gp.Kriging_sa(enterococci_shp_2, "NValue", kriging_all, "Spherical 882.922345", "30", "VARIABLE 12",
                            Output_variance_of_prediction_raster)
        arcpy.AddMessage("Step 3 of 5: Kriging has been executed successfully")

        # Process: Feature to Raster
        arcpy.FeatureToRaster_conversion(input_watershed, "FID", raster_watershed, "30")
        arcpy.AddMessage("Step 4 of 5: Watershed has been converted to raster successfully")

        # Process: Extract by Mask
        arcpy.gp.ExtractByMask_sa(kriging_all, raster_watershed, kriging)
        arcpy.AddMessage("Step 5 of 5: Kriging of all sampling site has been clipped to selected watershed successfully")

        arcpy.AddMessage("------------- Menu #2 : Water quality toolbox finishes processing -------------")

        # Delete temporary directory
        if os.path.exists(temp_directory):
            shutil.rmtree(temp_directory)
            arcpy.AddMessage("------------- Temporary directory has been deleted [" + str(temp_directory) + "]-------------")

        return

class Tool3(object):
    def __init__(self):
        self.label = "Menu 3: Elevation tool"
        self.description = "Creating elevation tool for mosaicking tiles of elevation data, extracting the mosaick using raster of watershed as mask"
        self.canRunInBackground = False

    def getParameterInfo(self):
        params = []
        # Create workspace
        workspace = arcpy.Parameter(name="workspace",
                                    displayName="Workspace",
                                    datatype="DEFolder",
                                    parameterType="Required",  # Required|Optional|Derived
                                    direction="Input",  # Input|Output
                                    )
        params.append(workspace)
        input_raster_watershed = arcpy.Parameter(name="input_raster_watershed",
                                     displayName="Input Raster of Watershed that has been generated in Output folder by Menu 2 : Water quality tool",
                                     datatype="DERasterDataset",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        params.append(input_raster_watershed)
        input_tiles = arcpy.Parameter(name="input_tiles",
                                        displayName="Input Tiles of Elevation",
                                        datatype="DERasterDataset",
                                        parameterType="Required",  # Required|Optional|Derived
                                        direction="Input",  # Input|Output
                                        multiValue="True",
                                        )
        params.append(input_tiles)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        # Get input value
        workspace = parameters[0].valueAsText
        input_raster_watershed = parameters[1].valueAsText
        input_tiles = parameters[2].valueAsText
        arcpy.AddMessage("Your input_raster_watershed is: " + str(input_raster_watershed))
        arcpy.AddMessage("Your input_tiles is: " + str(input_tiles))

        # Get temp and output value
        output_directory = str(workspace) + "\\output\\"
        temp_directory = str(workspace) + "\\temp\\"
        dem_all_name = "DEMAll.TIF"
        dem_all = output_directory + dem_all_name
        dem = output_directory + "DEM.TIF"

        # Create temporary directory if doesn't exists
        if not os.path.exists(temp_directory):
            os.mkdir(temp_directory)
            arcpy.AddMessage("------------- Temporary directory created [" + str(temp_directory) + "]-------------")

        # Create output directory if doesn't exists
        if not os.path.exists(output_directory):
            os.mkdir(output_directory)
            arcpy.AddMessage("------------- Output directory created [" + str(output_directory) + "]-------------")

        arcpy.AddMessage("------------- Menu #3 : Elevation toolbox starts processing -------------")

        # Process: Mosaic To New Raster
        arcpy.MosaicToNewRaster_management(
            input_tiles,
            output_directory, dem_all_name,
            "PROJCS['NAD_1983_StatePlane_Rhode_Island_FIPS_3800_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',328083.3333333333],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-71.5],PARAMETER['Scale_Factor',0.99999375],PARAMETER['Latitude_Of_Origin',41.08333333333334],UNIT['Foot_US',0.3048006096012192]]",
            "32_BIT_FLOAT", "30", "1", "LAST", "FIRST")
        arcpy.AddMessage("Step 1 of 2: Mosaick of tiles has been created successfully")

        # Process: Extract by Mask
        arcpy.gp.ExtractByMask_sa(dem_all, input_raster_watershed, dem)
        arcpy.AddMessage("Step 2 of 2: Mosaick of tiles has been clipped by the raster based of watershed successfully")

        arcpy.AddMessage("------------- Menu #3 : Elevation toolbox finishes processing -------------")

        # Delete temporary directory
        if os.path.exists(temp_directory):
            shutil.rmtree(temp_directory)
            arcpy.AddMessage("------------- Temporary directory has been deleted [" + str(temp_directory) + "]-------------")

        return