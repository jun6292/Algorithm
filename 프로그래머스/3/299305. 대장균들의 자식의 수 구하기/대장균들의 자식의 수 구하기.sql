SELECT ID, (SELECT COUNT(*) FROM ECOLI_DATA WHERE PARENT_ID = E.ID) AS CHILD_COUNT
FROM ECOLI_DATA E
ORDER BY ID ASC;