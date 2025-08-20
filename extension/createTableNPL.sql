CREATE TABLE superfund_national_priorities_list AS TABLE superfund_albers_national_priorities_list;

ALTER TABLE superfund_national_priorities_list DROP COLUMN wkb_geometry;

ALTER TABLE superfund_national_priorities_list RENAME COLUMN notice_of_ TO notice_of;

CREATE INDEX IF NOT EXISTS superfund_npl_ids_index
ON superfund_national_priorities_list(ogc_fid, objectid);
