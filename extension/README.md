Things that need to be done to enable searches required from Case Study One.

Develop an SQL statement that will be able to do the search.  
    1) Intially do this using a Python Notebook with a psycopg connection to the DB.  
       1.1) The Notebook will contain a Python function that will connect to the DB  
            and run a query.  
       1.2) The functionn will require input of:  
              a) pi: USGS and HUD from the podm_pfas_sample_data table  
              b) distance in miles, but the function will convert the miles to km for  
                 the query.  
              c) The dataset to search distance for, initially that will be the Superfund  
                 (NPL) sites.  
              d) The PFAS analyte(s) to return  
    2) The table(s) to search with view  
       2.1) opal_albers_location, which has been added to a new view called podm_pfas_sample_data_albers  
       2.2) superfund_albers_national_priorities_list   
    3) After getting this to work, figure out how to use the this function and its SQL statement in DRF  
   
Other:  
https://gis.stackexchange.com/questions/94640/geodjango-transform-not-working  
  
Specific Task That Need to be Completed:  
  
Ingest the NPL data:  
    Data:  
    /projects/pfas/data/superfund_albers_national_priorities_list.csv  
  
    Create Table:  
    opal-backend/extension/createAlbersNPL.sql 
  
    Copy data to table:  
    opal-backend/extension/data_copy_NPL.sql  
  
Ingest the ZCTA 2020 Centroids Data:  
    Data:  
    /projects/pfas/data/ZCTA_2020_Centroids.csv  
  
    Create table:  
    opal-backend/extension/createZCTA_2020_Centroids.sql  
  
    Copy data to table:  
    opal-backend/extension/data_copy_zcta_2020_centroids.sql  
  
Create opal_albers_location table:  
    Run commands in:  
    opal-backend/extension/createOPAL_AlbersLocation.sql   
    opal-backend/extension/createPfasPrimarySampleDataAlbers.sql  

Create pfas_sites_distance_from_npl dumy table:
    Run command in:
    opal-backend/extension/createDistanceFromNPL.sql

Create superfund_national_priorities_list table:
    Run commands in:
    createTableNPL.sql

Create opal_site_distance_to_closest_superfund_site dumy table:
    Run commands in:
    opal-backend/extension/createOPAL-distance2NPL.sql

Create opal_pfas_sample_data_npl View
    Run command:
    opdal-backend/extension/createPfasPrimarySampleDataNPL.sql
  
