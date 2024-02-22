SELECT C.CAR_ID, C.CAR_TYPE, ROUND(DAILY_FEE * 30 * (100 - P.DISCOUNT_RATE) / 100) AS FEE
FROM CAR_RENTAL_COMPANY_CAR C JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H ON C.CAR_ID = H.CAR_ID
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P ON C.CAR_TYPE = P.CAR_TYPE
WHERE C.CAR_ID NOT IN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE < '2022-12-01' AND END_DATE > '2022-11-01'
)
AND P.DURATION_TYPE = '30일 이상'
AND (C.CAR_TYPE = '세단' OR C.CAR_TYPE = 'SUV') 
GROUP BY CAR_ID
HAVING FEE >= 500000 AND FEE < 2000000
ORDER BY FEE DESC, CAR_TYPE ASC, CAR_ID DESC;