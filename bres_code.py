
import pandas as pd
import geopandas as gpd

income_df = pd.read_csv('/Users/breianaolguin/Desktop/GEOG4092/Final Project/Income/Income_ProcessedData.csv')
race_df = pd.read_csv('/Users/breianaolguin/Desktop/GEOG4092/Final Project/Race/RaceEthnicity_ProcessedData.csv')
census_gdf = gpd.read_file('/Users/breianaolguin/Desktop/GEOG4092/Final Project/census_block_groups_2010')
census_gdf.head()


   
        GEOID_BG     GEOID_NUM  POPULATION  HISPANIC_2  WHITE_2010  BLACK_2010  
0  080310006002  8.031001e+10      1556.0       984.0       494.0        19.0   
1  080310007011  8.031001e+10      1555.0       685.0       747.0        58.0   
2  080310007012  8.031001e+10      1156.0       625.0       458.0        27.0   
3  080310007013  8.031001e+10      1455.0       895.0       449.0        25.0   
4  080310007021  8.031001e+10       971.0       782.0       148.0        16.0   
    NATIVE_AM_  ASIAN_2010  HAW_PACIS_  OTHER_2010  ...  RENTED_A_2 
0        16.0        20.0         0.0         2.0  ...       100.0   
1        23.0        10.0         1.0         7.0  ...        63.0   
2        16.0        17.0         1.0         2.0  ...        43.0   
3        37.0        21.0         3.0         3.0  ...        80.0   
4         9.0         5.0         0.0         0.0  ...        72.0   

    RENTED_A_3  RENTED_A_4  RENTED_A_5  RENTED_A_6  RENTED_A_7  RENTED_A_8  
0        88.0        19.0        14.0        10.0         8.0         1.0  
1        63.0        22.0        42.0       177.0       128.0        57.0   
2        32.0        12.0        14.0        14.0         4.0         1.0   
3        77.0        29.0        23.0        23.0        13.0         2.0  
4        30.0        11.0        13.0        15.0         5.0         0.0   
    
          SHAPE_Leng  SHAPE_Area                                           geometry  
       0    0.028893    0.000041  POLYGON ((-105.01916 39.75483, -105.01916 39.7... 
       1    0.035016    0.000050  POLYGON ((-105.03931 39.74395, -105.03931 39.7...  
       2    0.026796    0.000039  POLYGON ((-105.03933 39.74034, -105.03932 39.7...  
       3    0.027680    0.000037  POLYGON ((-105.04634 39.74035, -105.04635 39.7...  
       4    0.019848    0.000023  POLYGON ((-105.02521 39.74636, -105.02521 39.7...  
    
       [5 rows x 133 columns]

                                            
                                            
merged_census = pd.merge(income_df,race_df,left_on='GEO_ID',right_on='GEO_ID')
merged_census.head()



                  GEO_ID  B19001_001E  B19001_002E  B19001_003E  B19001_004E  
0  1500000US080310032022          570           13           39            0   
1  1500000US080310032021          617            9           20           73  
2  1500000US080310034011          297            9            0            0  
3  1500000US080310034023          370            9            0            9   
4  1500000US080310034021          439           40            0            0   

   B19001_005E  B19001_006E  B19001_007E  B19001_008E  B19001_009E  ...  
0            8           15           37            0            0  ...   
1            7           85           64           73           56  ...   
2           22            0            0            0            0  ...   
3           18            0           10            8            0  ...   
4            8            0           18            0            0  ...   

   B03002_012E  B03002_013E  B03002_014E  B03002_015E  B03002_016E  
0           20            0            0            0            0   
1           99           89            0            0            0   
2           63           24            0            0            0  
3           54           54            0            0            0   
4            0            0            0            0            0   

   B03002_017E  B03002_018E  B03002_019E  B03002_020E  B03002_021E  
0            0           20            0            0            0  
1            0            5            5            5            0  
2            0           13           26           26            0  
3            0            0            0            0            0  
4            0            0            0            0            0  

[5 rows x 39 columns]



merged_census_gdf = gpd.GeoDataFrame(merged_census)

                           GEO_ID  B19001_001E  B19001_002E  B19001_003E  
       0    1500000US080310032022          570           13           39   
       1    1500000US080310032021          617            9           20   
       2    1500000US080310034011          297            9            0   
       3    1500000US080310034023          370            9            0   
       4    1500000US080310034021          439           40            0   
       ..                     ...          ...          ...          ...   
       476  1500000US080310068133          901          107           38   
       477  1500000US080310083861          612            0            0   
       478  1500000US080310083872          845           13            7   
       479  1500000US080310083882         1113           19           17   
       480  1500000US080310009023          443           13           26   
      
            B19001_004E  B19001_005E  B19001_006E  B19001_007E  B19001_008E  
       0              0            8           15           37            0   
       1             73            7           85           64           73  
       2              0           22            0            0            0   
       3              9           18            0           10            8  
       4              0            8            0           18            0   
       ..           ...          ...          ...          ...          ...   
       476           18           18           88           18            0   
       477           27           79           14           21           31   
       478            9           10            8           21           38   
       479            0            0           85           92           44   
       480           60           23           70           22           60  
       
            B19001_009E  ...  B03002_012E  B03002_013E  B03002_014E  B03002_015E  
       0              0  ...           20            0            0            0   
       1             56  ...           99           89            0            0   
       2              0  ...           63           24            0            0   
       3              0  ...           54           54            0            0   
       4              0  ...            0            0            0            0   
       ..           ...  ...          ...          ...          ...          ...   
       476           28  ...          154           28            0            0   
       477            0  ...         1850         1232            0            0   
       478           46  ...         2743         2223           58           25   
       479           46  ...          742          461           43           41   
       480            4  ...          665          548            0            0   
       
            B03002_016E  B03002_017E  B03002_018E  B03002_019E  B03002_020E 
       0              0            0           20            0            0   
       1              0            0            5            5            5   
       2              0            0           13           26           26   
       3              0            0            0            0            0   
       4              0            0            0            0            0   
       ..           ...          ...          ...          ...          ...   
       476            0            0          126            0            0   
       477            0            0          618            0            0   
       478            0            0          410           27           27   
       479            0            0          156           41           41   
       480           45            0           46           26           13   
            B03002_021E  
       0              0  
       1              0  
       2              0  
       3              0  
       4              0  
       ..           ...  
       476            0  
       477            0  
       478            0  
       479            0  
       480           13 
    
       [481 rows x 39 columns]

    #join = gpd.sjoin(merged_census_gdf, census_gdf, how="inner", op='intersects')
