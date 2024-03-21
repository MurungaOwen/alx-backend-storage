-- create an index of name and score
create index idx_name_first_score on names((left(name,1)), score);