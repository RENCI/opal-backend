CREATE TABLE IF NOT EXISTS opal_site_distance_to_closest_superfund_site(
  opal_site_sample_id VARCHAR(100),
  superfund_ogc_fid INT,
  miles_to_closest_superfund_site NUMERIC
);

INSERT INTO opal_site_distance_to_closest_superfund_site (opal_site_sample_id, superfund_ogc_fid, miles_to_closest_superfund_site )
SELECT
    opal.sample_id AS opal_site_sample_id,
    sf.ogc_fid AS superfund_ogc_fid,
    ST_Distance( opal.geom, sf.wkb_geometry) * 0.000621371  AS miles_to_closest_superfund_site
FROM
    opal_pfas_sample_data_albers AS opal
JOIN LATERAL (
    SELECT
        ogc_fid,
        wkb_geometry
    FROM
        superfund_albers_national_priorities_list
    ORDER BY
        opal.geom <-> wkb_geometry  -- Nearest-neighbor operator
    LIMIT 1
) AS sf
ON true
WHERE opal.geom IS NOT NULL;

