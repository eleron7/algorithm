-- 조건에 부합하는 중고거래 댓글 조회하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/164673

SELECT  A.TITLE, A.BOARD_ID, B.REPLY_ID, B.WRITER_ID, B.CONTENTS, DATE_FORMAT(B.CREATED_DATE, "%Y-%m-%d") AS CREATED_DATE
FROM USED_GOODS_BOARD AS A, USED_GOODS_REPLY AS B 
WHERE A.BOARD_ID = B.BOARD_ID and A.CREATED_DATE BETWEEN '2022-10-01' and '2022-10-31'
ORDER BY B.CREATED_DATE ASC, A.TITLE ASC;