-- procedure to compute mean of weighted values
DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN `user_id` INT)
BEGIN
    UPDATE users
    SET average_score = (SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight)
        FROM corrections
        INNER JOIN projects
        ON projects.id = corrections.project_id
        WHERE corrections.user_id = user_id)
    WHERE users.id = user_id;
END $$
DELIMITER ;