CREATE MATERIALIZED VIEW podm_ntar_sample_data AS
SELECT sa.id AS id,
       sa.sample_id AS sample_id,
       st.study AS study,
       sa.date AS date,
       st.year AS year,
       st.pi as pi,
       m.medium AS medium,
       l.city AS city,
       l.state AS state,
       l.zipcode AS zipcode,
       l.site_id AS site_id,
       l.site_type AS site_type,
       l.latitude AS latitude,
       l.longitude AS longitude,
       l.detects AS sample_detects,
       l.sum AS sample_sum,
       d.pfas_short_name AS pfas_short_name,
       d.pfas_long_name AS pfas_long_name,
       d.flags AS flags,
       d.measurement AS measurement
FROM podm_sample sa
INNER JOIN podm_study st ON st.study_id=sa.study_id
INNER JOIN podm_technique t ON t.technique_id=sa.technique_id
INNER JOIN podm_medium m ON m.medium_id=sa.medium_id
INNER JOIN podm_location l ON l.location_id=sa.location_id
INNER JOIN podm_ntar_data d ON d.sample_id=sa.sample_id;

CREATE INDEX IF NOT EXISTS podm_ntar_sample_data_index ON podm_ntar_sample_data (id, sample_id);
