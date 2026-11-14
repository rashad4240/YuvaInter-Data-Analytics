-- q1_by_bmi_class
SELECT bmi_class,
       COUNT(*)                     AS patients,
       ROUND(AVG(progression), 1)   AS avg_progression,
       ROUND(AVG(glucose), 1)       AS avg_glucose
FROM patients
GROUP BY bmi_class
ORDER BY avg_progression DESC;

-- q2_case_bands
SELECT CASE WHEN bp >= 100 THEN 'High BP' ELSE 'Normal BP' END AS bp_band,
       age_group,
       COUNT(*) AS patients,
       ROUND(AVG(progression), 1) AS avg_progression
FROM patients
GROUP BY bp_band, age_group
HAVING COUNT(*) >= 10
ORDER BY bp_band, age_group;

-- q3_window_rank
SELECT * FROM (
    SELECT age_group, age, bmi, progression,
           RANK() OVER (PARTITION BY age_group ORDER BY progression DESC) AS rank_in_group
    FROM patients
)
WHERE rank_in_group <= 2
ORDER BY age_group, rank_in_group;

-- q4_subquery
SELECT COUNT(*) AS patients_above_avg,
       ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM patients), 1) AS pct_of_all,
       ROUND(AVG(bmi), 1) AS their_avg_bmi
FROM patients
WHERE progression > (SELECT AVG(progression) FROM patients);

