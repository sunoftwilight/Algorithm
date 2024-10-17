-- 코드를 입력하세요
SELECT A.CATEGORY, B.MAX_PRICE, A.PRODUCT_NAME
FROM FOOD_PRODUCT A JOIN (
                            SELECT CATEGORY, MAX(PRICE) AS MAX_PRICE
                            FROM FOOD_PRODUCT
                            GROUP BY CATEGORY
                            HAVING CATEGORY IN ('과자', '국', '김치', '식용유')
                        ) B
ON A.CATEGORY = B.CATEGORY AND A.PRICE = B.MAX_PRICE
ORDER BY B.MAX_PRICE DESC;