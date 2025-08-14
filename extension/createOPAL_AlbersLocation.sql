# Create opal_albers_location table
CREATE TABLE opal_albers_location AS TABLE podm_location;

# Add ZCTA latitude and longitude values to opal_albers_location
UPDATE opal_albers_location l
SET (latitude, longitude) = (z.lat, z.lon)
FROM zcta_2020_centroids z
WHERE z.zcta = l.zipcode;

# Update opal_albers_location site_type
UPDATE opal_albers_location
SET site_type = 'Other'
WHERE site_type is null;

# Add geometry column to opal_albers_location table
ALTER TABLE opal_albers_location ADD COLUMN geom geometry(Point, 102008);

# Add geometry to opal_albers_location table
UPDATE opal_albers_location 
SET geom = ST_Transform(ST_SetSRID(ST_MakePoint(longitude::double precision, latitude::double precision) 4326), 102008);

CREATE INDEX IF NOT EXISTS opal_albers_location_id_index
ON opal_albers_location(location_id);

CREATE INDEX opal_albers_location_geom_index 
ON opal_albers_location USING GIST (geom);
