-- 1. Developer Activity Summary

SELECT
    developer_id,
    COUNT(*) AS total_events,

    SUM(
        CASE
            WHEN event_type = 'Coding' THEN 1
            ELSE 0
        END
    ) AS coding_events,

    SUM(
        CASE
            WHEN event_type = 'Coding'
            THEN duration_minutes
            ELSE 0
        END
    ) AS total_coding_minutes,

    SUM(
        CASE
            WHEN event_type IN ('Message', 'Task_Update')
            THEN 1
            ELSE 0
        END
    ) AS potential_interruptions

FROM developer_activity

GROUP BY developer_id

ORDER BY total_coding_minutes DESC;