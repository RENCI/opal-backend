CREATE TABLE IF NOT EXISTS superfund_albers_national_priorities_list( 
 ogc_fid INT,
 objectid VARCHAR(7),
 site_name VARCHAR(100),
 site_score NUMERIC,
 site_epa_i VARCHAR(20),
 sems_id INT,
 sits_id INT,
 region_id INT,
 state VARCHAR(40),
 city VARCHAR(50),
 county VARCHAR(60),
 status VARCHAR(25),
 longitude NUMERIC,
 latitude NUMERIC,
 proposed_d VARCHAR(15),
 listing_da VARCHAR(15),
 constructi VARCHAR(15),
 construc_1 NUMERIC,
 noid_date VARCHAR(15),
 deletion_d VARCHAR(15),
 site_listi VARCHAR(120),
 site_progr VARCHAR(200),
 notice_of_ VARCHAR(140),
 proposed_f VARCHAR(120),
 deletion_f VARCHAR(120),
 final_fr_n VARCHAR(120),
 noid_fr_no VARCHAR(120),
 restoratio VARCHAR(200),
 site_has_h VARCHAR(140),
 creationda VARCHAR(10),
 creator VARCHAR(10),
 editdate VARCHAR(10),
 editor VARCHAR(10),
 objectid2 INT,
 wkb_geometry GEOMETRY(Point, 102008),
 pfas BOOLEAN NOT NULL DEFAULT FALSE
)

CREATE INDEX IF NOT EXISTS superfund_albers_npl_ids_index
ON superfund_albers_national_priorities_list(ogc_fid, objectid);

CREATE INDEX superfund_albers_npl_geom_index
ON superfund_albers_national_priorities_list USING GIST (wkb_geometry);
