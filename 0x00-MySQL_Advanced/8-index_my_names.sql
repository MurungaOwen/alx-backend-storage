-- indexing name
DROP INDEX IF EXISTS idx_name_first ON names;
CREATE INDEX idx_name_first ON names(left(name,1));
