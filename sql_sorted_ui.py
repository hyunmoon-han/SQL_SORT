from original import *

# sql_query = """SELECT A.CUSTOMER_ID
#      , A.NAME
#      , B.CATEGORY
#      , SUM(B.AMOUNT) AS TOTAL_AMOUNT
#      , COUNT(C.PAYMENT_ID) AS PAYMENT_COUNT
#      , func1(a, b, c)
#      , SUM(CASE WHEN salary > 5000 THEN (CASE WHEN performance_rating = 'Excellent' THEN salary * 0.2 ELSE salary * 0.1 END) WHEN salary >= 3000 AND salary <= 5000 THEN salary * 0.05 WHEN Z.sum_cnt - Z.m_sum_cnt > 0 THEN (CASE WHEN Z.prom_send_cnt - (Z.sum_cnt - Z.m_sum_cnt) > 0 THEN (CASE WHEN Z.prom_send_cnt - (Z.sum_cnt - Z.m_sum_cnt) >= Z.m_sum_cnt THEN Z.m_sum_cnt ELSE Z.prom_send_cnt - (Z.sum_cnt - Z.m_sum_cnt) END) ELSE 0 END) ELSE 0 END) AS bonus_sum
#      , SUM (CASE WHEN salary > 5000 THEN (CASE WHEN performance_rating = 'Excellent' THEN salary * 0.2
# ELSE salary * 0.1  
#                                                             END)
# WHEN salary >= 3000
# AND salary <= 5000 THEN salary * 0.05
# ELSE 0  
#                     END) AS bonus_sum
#      , sum(CASE WHEN J.STOR_CD IS NULL THEN A.CHNL_SEND_CNT
#           								ELSE J.STOR_DSTRB_CUST_CNT 
#           								END) AS cnt
#      , CASE WHEN FREQUENCY > 0
# AND FREQUENCY <= 7 THEN DATE_ADD(LAST_SALE_DT, INTERVAL 1 DAY)
# WHEN FREQUENCY > 7
# AND FREQUENCY <= 30 THEN DATE_ADD(LAST_SALE_DT, INTERVAL 8 DAY)
# WHEN FREQUENCY > 30
# AND FREQUENCY <= 90 THEN DATE_ADD(LAST_SALE_DT, INTERVAL 31 DAY)
# WHEN FREQUENCY > 90
# AND FREQUENCY <= 180 THEN DATE_ADD(LAST_SALE_DT, INTERVAL 91 DAY)
# WHEN FREQUENCY > 180
# AND FREQUENCY <= 365 THEN DATE_ADD(LAST_SALE_DT, INTERVAL 181 DAY) 
# 			END AS PCH_PLAN_START             
#      , CASE WHEN FREQUENCY > 0
# AND FREQUENCY <= 7 THEN DATE_ADD(LAST_SALE_DT, INTERVAL 1 DAY)
# WHEN FREQUENCY > 7
# AND FREQUENCY <= 30 THEN (CASE WHEN LAST_SALE_DT IS NOT NULL THEN DATE_ADD(LAST_SALE_DT, INTERVAL 8 DAY)
# ELSE DATE_ADD(CURRENT_DATE(), INTERVAL 8 DAY)
#         																			 		END )
# WHEN FREQUENCY > 30
# AND FREQUENCY <= 90 THEN (CASE WHEN LAST_SALE_DT IS NOT NULL THEN DATE_ADD(LAST_SALE_DT, INTERVAL 31 DAY)
# WHEN LAST_SALE_DT == 0 THEN 0
# ELSE DATE_ADD(CURRENT_DATE(), INTERVAL 31 DAY)
# 																END )
# ELSE DATE_ADD(LAST_SALE_DT, INTERVAL 91 DAY)
# 	 		END AS PCH_PLAN_START
# FROM (CUSTOMERS) A
# INNER JOIN ( 
#     SELECT CUSTOMER_ID, PAYMENT_ID, PAYMENT_METHOD, PAYMENT_STATUS
# FROM PAYMENTS
# WHERE PAYMENT_METHOD = 'CARD'
# OR PAYMENT_STATUS = 'APPROVED'
# AND CUSTOMER_ID IN ( 
# 				        SELECT CUSTOMER_ID
# FROM ANOTHER_TABLE
# WHERE STATUS = 'ACTIVE'
#    						 )
# 			) B
#  ON
# A.CUSTOMER_ID = B.CUSTOMER_ID
# LEFT JOIN ( SELECT ORDER_ID, DELIVERY_STATUS, DELIVERY_DATE
# FROM DELIVERY
# WHERE DELIVERY_STATUS IN ('SHIPPED', 'IN TRANSIT')) C
#  ON
# A.CUSTOMER_ID = C.CUSTOMER_ID
# RIGHT JOIN ( SELECT CUSTOMER_ID, CATEGORY, AMOUNT, STATUS, ORDER_ID, CASE WHEN score >= 90 THEN (CASE WHEN score >= 95 THEN (CASE WHEN score >= 98 THEN 'A++'
# ELSE 'A+' 
# 								                                                                                  END)
# ELSE 'A' 
# 				                                                                      END)
# WHEN score >= 80 THEN (CASE WHEN score >= 85 THEN 'B+'
# ELSE 'B' 
# 				                          											   END)
# WHEN score >= 70 THEN 'C'
# ELSE 'F' 
# 				  					      END AS grade
# FROM ORDERS
# WHERE STATUS IN ('CONFIRMED', 'PENDING') 
# 				) D
#    ON
# B.ORDER_ID = D.ORDER_ID
# RIGHT JOIN DELIVERY D
#   ON
# B.ORDER_ID = D.ORDER_ID
# AND D.DELIVERY_STATUS = 'SHIPPED'
# OR D.DELIVERY_STATUS = 'IN TRANSIT'
# WHERE 1 = 1
# AND A.AGE > 25
# AND A.COUNTRY = 'USA'
# OR B.CATEGORY = 'ELECTRONICS'
# AND B.AMOUNT > 500
# AND (B.CATEGORY = 'ELECTRONICS'
# 	OR B.AMOUNT > 500)
# GROUP BY A.CUSTOMER_ID
#     , A.NAME
#     , B.CATEGORY
# HAVING 1 = 1
# AND SUM(B.AMOUNT) > 1000
# AND COUNT(C.PAYMENT_ID) >= 2
# ORDER BY A.NAME ASC, TOTAL_AMOUNT DESC
# """

# sql_query = """SELECT A.CUSTOMER_ID
#      , A.NAME
#      , B.CATEGORY
#      , SUM(B.AMOUNT) AS TOTAL_AMOUNT
#      , COUNT(C.PAYMENT_ID) AS PAYMENT_COUNT
#      , func1(a, b, c)
#      , SUM(CASE WHEN salary > 5000 THEN (CASE WHEN performance_rating = 'Excellent' THEN salary * 0.2 ELSE salary * 0.1 END) WHEN salary >= 3000 AND salary <= 5000 THEN salary * 0.05 WHEN Z.sum_cnt - Z.m_sum_cnt > 0 THEN (CASE WHEN Z.prom_send_cnt - (Z.sum_cnt - Z.m_sum_cnt) > 0 THEN (CASE WHEN Z.prom_send_cnt - (Z.sum_cnt - Z.m_sum_cnt) >= Z.m_sum_cnt THEN Z.m_sum_cnt ELSE Z.prom_send_cnt - (Z.sum_cnt - Z.m_sum_cnt) END) ELSE 0 END) ELSE 0 END) AS bonus_sum
#      , SUM (CASE WHEN salary > 5000 THEN (CASE WHEN performance_rating = 'Excellent' THEN salary * 0.2  
#                                                             ELSE salary * 0.1  
#                                                             END)
#                     WHEN salary >= 3000 AND salary <= 5000 THEN salary * 0.05 
#                     ELSE 0  
#                     END) AS bonus_sum
#      , sum(CASE WHEN J.STOR_CD IS NULL 
#             THEN A.CHNL_SEND_CNT
#           ELSE J.STOR_DSTRB_CUST_CNT END) AS cnt
#      , CASE WHEN FREQUENCY > 0
# AND FREQUENCY <= 7 THEN DATE_ADD(LAST_SALE_DT, INTERVAL 1 DAY)
# WHEN FREQUENCY > 7
# AND FREQUENCY <= 30 THEN DATE_ADD(LAST_SALE_DT, INTERVAL 8 DAY)
# WHEN FREQUENCY > 30
# AND FREQUENCY <= 90 THEN DATE_ADD(LAST_SALE_DT, INTERVAL 31 DAY)
# WHEN FREQUENCY > 90
# AND FREQUENCY <= 180 THEN DATE_ADD(LAST_SALE_DT, INTERVAL 91 DAY)
# WHEN FREQUENCY > 180
# AND FREQUENCY <= 365 THEN DATE_ADD(LAST_SALE_DT, INTERVAL 181 DAY) END AS PCH_PLAN_START             
#      , CASE WHEN FREQUENCY > 0
# AND FREQUENCY <= 7 THEN DATE_ADD(LAST_SALE_DT, INTERVAL 1 DAY)
# WHEN FREQUENCY > 7
# AND FREQUENCY <= 30 THEN (CASE WHEN LAST_SALE_DT IS NOT NULL THEN DATE_ADD(LAST_SALE_DT, INTERVAL 8 DAY)
# ELSE DATE_ADD(CURRENT_DATE(), INTERVAL 8 DAY)
#         																			 END )
# WHEN FREQUENCY > 30
# AND FREQUENCY <= 90 THEN (CASE WHEN LAST_SALE_DT IS NOT NULL THEN DATE_ADD(LAST_SALE_DT, INTERVAL 31 DAY)
# WHEN LAST_SALE_DT == 0 THEN 0
# ELSE DATE_ADD(CURRENT_DATE(), INTERVAL 31 DAY)
# 													    END )
# ELSE DATE_ADD(LAST_SALE_DT, INTERVAL 91 DAY)
# 	 END AS PCH_PLAN_START
# FROM (CUSTOMERS) A
# INNER JOIN ( SELECT CUSTOMER_ID, PAYMENT_ID, PAYMENT_METHOD, PAYMENT_STATUS
# FROM PAYMENTS
# WHERE PAYMENT_METHOD = 'CARD'
# OR PAYMENT_STATUS = 'APPROVED' ) B
#      ON
# A.CUSTOMER_ID = B.CUSTOMER_ID
# LEFT JOIN ( SELECT ORDER_ID, DELIVERY_STATUS, DELIVERY_DATE
# FROM DELIVERY
# WHERE DELIVERY_STATUS IN ('SHIPPED', 'IN TRANSIT')) C
#      ON
# A.CUSTOMER_ID = C.CUSTOMER_ID
# RIGHT JOIN ( SELECT CUSTOMER_ID, CATEGORY, AMOUNT, STATUS, ORDER_ID, CASE WHEN score >= 90 THEN (CASE WHEN score >= 95 THEN (CASE WHEN score >= 98 THEN 'A++'
# ELSE 'A+' 
# 				                                                                                  END)
# ELSE 'A' 
#                                                                       END)
# WHEN score >= 80 THEN (CASE WHEN score >= 85 THEN 'B+'
# ELSE 'B' 
#                           											   END)
# WHEN score >= 70 THEN 'C'
# ELSE 'F' 
#   					      END AS grade
# FROM ORDERS
# WHERE STATUS IN ('CONFIRMED', 'PENDING') ) D
#      ON
# B.ORDER_ID = D.ORDER_ID
# RIGHT JOIN DELIVERY D
#   ON
# B.ORDER_ID = D.ORDER_ID
# AND D.DELIVERY_STATUS = 'SHIPPED'
# OR D.DELIVERY_STATUS = 'IN TRANSIT'
# WHERE A.AGE > 25
# AND A.COUNTRY = 'USA'
# OR B.CATEGORY = 'ELECTRONICS'
# AND B.AMOUNT > 500
# AND (B.CATEGORY = 'ELECTRONICS'
# 	OR B.AMOUNT > 500)
# GROUP BY A.CUSTOMER_ID
# AND A.NAME
# OR B.CATEGORY
# HAVING SUM(B.AMOUNT) > 1000
# AND COUNT(C.PAYMENT_ID) >= 2
# ORDER BY A.NAME ASC, TOTAL_AMOUNT DESC;"""

sql_query = """WITH A AS (SELECT SALES.SALE_DT               AS SALE_DT             /*구매 일자*/
			    , SALES.CUS_CD                AS CUS_CD              /*구매 고객 코드*/
			    , SALES.SALE_AMT              AS SALE_AMT            /*구매 금액*/ 
			    , IFNULL(cd1.cd_name, '미정의') AS GENDER              /*구매 고객 성별*/
			    , IFNULL(cd2.cd_name, '미정의') AS AGE_GROUP           /*구매 고객 연령대*/ 
			    , IFNULL(cd3.cd_name, '미정의') AS GRADE               /*구매 고객 회원 등급*/ 
			    , IFNULL(cd1.cd, '미정의')      AS GENDER_CD           /*구매 고객 성별 코드*/
			    , IFNULL(cd2.cd, '미정의')      AS AGE_GROUP_CD        /*구매 고객 연령대 코드*/
			    , IFNULL(cd3.cd, '미정의')      AS GRADE_CD            /*구매 고객 회원 등급 코드*/
			 FROM CSDW_SALE_INFO SALES
			  	  LEFT OUTER JOIN CSDW_CUST_INFO CUST                
			   ON SALES.CUS_CD = CUST.CUS_CD
			  	  LEFT OUTER JOIN COMM_CD_INFO cd1                   /*성별 코드 join*/
			   ON (CUST.SEX % 2 = cd1.CD % 2) AND (CUST.SEX != '') 
			  AND cd1.grp_cd = 'CR003'      
			  	  LEFT OUTER JOIN COMM_CD_INFO cd2                   /*연령대 코드 join*/
			   ON CUST.CUR_AGRP_CD = cd2.cd
			  AND cd2.grp_cd = 'CS102'
			   	  LEFT OUTER JOIN COMM_CD_INFO cd3                   /*회원 등급 코드 join*/
			   ON CUST.CUS_GRADE1 = cd3.CD
			  AND cd3.grp_cd = 'CR007'
), 
PREV AS (SELECT GENDER
              , AGE_GROUP
              , GRADE
              , GENDER_CD
              , AGE_GROUP_CD
              , GRADE_CD
              , COUNT(DISTINCT CUS_CD) PREV_CUS_AMT                            /*과거 구매 고객 수*/
              , SUM(SALE_AMT) PREV_SALE_AMT                                    /*과거 구매 금액*/
              , ROUND(SUM(SALE_AMT) / COUNT(DISTINCT CUS_CD), 2) PREV_AOV      /*과거 객단가*/
           FROM A
          WHERE SALE_DT BETWEEN @prev_startdate AND @prev_enddate
          GROUP BY GENDER_CD
              , AGE_GROUP_CD
              , GRADE_CD
),
CURR AS (SELECT GENDER
              , AGE_GROUP
              , GRADE
              , GENDER_CD
              , AGE_GROUP_CD
              , GRADE_CD
              , COUNT(DISTINCT CUS_CD) CURR_CUS_AMT                            /*현재 구매 고객 수*/
              , SUM(SALE_AMT) CURR_SALE_AMT                                    /*현재 구매 금액*/
              , ROUND(SUM(SALE_AMT) / COUNT(DISTINCT CUS_CD), 2) CURR_AOV      /*현재 객단가*/
           FROM A
          WHERE SALE_DT BETWEEN @curr_startdate AND @curr_enddate
          GROUP BY GENDER_CD
              , AGE_GROUP_CD
              , GRADE_CD
)
SELECT GENDER
     , AGE_GROUP
     , GRADE
     , PREV_CUS_AMT AS '과거 구매 고객 수'
     , PREV_SALE_AMT AS '과거 구매 금액'
     , PREV_AOV AS '과거 객단가'
     , CURR_CUS_AMT AS '현재 구매 고객 수'
     , CURR_SALE_AMT AS '현재 구매 금액'
     , CURR_AOV AS '현재 객단가'
     , ROUND(((CURR_CUS_AMT - PREV_CUS_AMT) / PREV_CUS_AMT),2) * 100 AS '증감률(%)_구매고객수'
     , ROUND(((CURR_SALE_AMT - PREV_SALE_AMT) / PREV_SALE_AMT),2) * 100 AS '증감률(%)_구매금액'
     , ROUND(((CURR_AOV - PREV_AOV) / PREV_AOV),2) * 100 AS '증감률(%)_객단가'
  FROM (SELECT PREV.GENDER
             , PREV.AGE_GROUP
             , PREV.GRADE
             , PREV.GENDER_CD
             , PREV.AGE_GROUP_CD
             , PREV.GRADE_CD
             , PREV_CUS_AMT
             , PREV_SALE_AMT
             , PREV_AOV
             , IFNULL(CURR_CUS_AMT, 0) AS CURR_CUS_AMT
             , IFNULL(CURR_SALE_AMT, 0) AS CURR_SALE_AMT
             , IFNULL(CURR_AOV, 0) AS CURR_AOV
          FROM PREV 
               LEFT JOIN CURR
            ON 1=1

       
      
       ) B
"""


# sql_query = """SELECT Z.CHNL_SEND_YM, Z.chnl_id, Z.CHNL_NAME, Z.PROMOTION_ID, Z.promotion_nm, Z.PROM_APLY_RPLAN_NM, Z.PROM_TYPE, Z.aprv_date, Z.prom_desc, CASE WHEN Z.sum_cnt - Z.m_sum_cnt = 0 THEN (CASE WHEN Z.prom_send_cnt >= Z.m_sum_cnt THEN Z.m_sum_cnt ELSE Z.prom_send_cnt END)
# WHEN Z.sum_cnt - Z.m_sum_cnt > 0 THEN (CASE WHEN Z.prom_send_cnt - (Z.sum_cnt - Z.m_sum_cnt) > 0 THEN (CASE WHEN Z.prom_send_cnt - (Z.sum_cnt - Z.m_sum_cnt) >= Z.m_sum_cnt THEN Z.m_sum_cnt
# ELSE Z.prom_send_cnt - (Z.sum_cnt - Z.m_sum_cnt) END)
# ELSE 0 END)
# ELSE 0 END AS REAL_CNT
# FROM(SELECT T.CHNL_SEND_YM, T.CHNL_SEND_DATE, T.chnl_id, T.CHNL_NAME, T.cnt, T.PROMOTION_ID, T.promotion_nm, T.PROM_APLY_RPLAN_NM, T.PROM_TYPE, T.aprv_date, T.prom_desc, IFNULL(T.prom_send_cnt, 0) AS prom_send_cnt, sum(T.cnt) OVER(PARTITION BY T.chnl_id
# ORDER BY T.chnl_send_date) AS sum_cnt, sum(T.cnt) OVER(PARTITION BY T.chnl_send_YM, T.chnl_id
# ORDER BY T.chnl_send_date) AS m_sum_cnt, ROW_NUMBER() OVER(PARTITION BY T.CHNL_SEND_YM, T.chnl_id
# ORDER BY T.CHNL_SEND_DATE DESC) AS rn
# FROM(SELECT a.CHNL_SEND_YM, a.CHNL_SEND_DATE, e.chnl_id, e.CHNL_NAME, sum(CASE WHEN J.STOR_CD IS NULL THEN A.CHNL_SEND_CNT ELSE J.STOR_DSTRB_CUST_CNT END) AS cnt, f.PROMOTION_ID, f.promotion_nm, h.RPLAN_NM AS PROM_APLY_RPLAN_NM, I.LOOKUP_NAME AS PROM_TYPE, f.aprv_date, concat(f.prom_day_cnt, '일 ', f.prom_send_cnt, '건 무료') AS prom_desc, f.prom_send_cnt
# FROM ${jdbc.QuadMaxMart.SchemaName}i_ums_cms_chnl_send_sum a
# INNER JOIN ${jdbc.QuadMax.SchemaName}t_campaign b ON
# a.CAMP_ID = b.CAMP_ID
# INNER JOIN ${jdbc.QuadMax.SchemaName}t_camp_bill_shop b1 ON
# b.camp_ID = b1.camp_ID
# INNER JOIN ${jdbc.QuadMax.SchemaName}t_emp_dept b2 ON
# b1.shop_cd = b2.dept_id
# INNER JOIN ${jdbc.QuadMaxMart.SchemaName}i_cdw_cms_cdw_ria_smt100tm c ON
# b1.shop_cd = c.STORECD
# INNER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values d ON
# a.CHNL_CD = d.VAL10
# AND d.LOOKUP_TYPE = 'CHANNEL_TYPE'
# INNER JOIN ${jdbc.QuadMax.SchemaName}t_channel e ON
# d.LOOKUP_CODE = e.CHNL_TYPE_CD
# LEFT OUTER JOIN (SELECT a.PROMOTION_ID, b.promotion_nm, a.STORE_CD, b.RPLAN_ID, b.PROM_TYPE, a.APRV_DATE, b.PROM_DAY_CNT, date_format(date_add(str_to_date(a.aprv_date, '%Y%m%d'), INTERVAL b.PROM_DAY_CNT - 1 DAY), '%Y%m%d') AS END_DATE, c.CHNL_ID, c.PROM_SEND_CNT
# FROM ${jdbc.QuadMax.SchemaName}promotion_req a
# INNER JOIN ${jdbc.QuadMax.SchemaName}promotion_list b ON
# a.PROMOTION_ID = b.PROMOTION_ID
# INNER JOIN ${jdbc.QuadMax.SchemaName}promotion_chnnl_capacity c ON
# a.PROMOTION_ID = c.PROMOTION_ID
# WHERE 1 = 1
# AND b.prom_TYPE = 'CHNL_SEND_FREE'
# AND a.APRV_STAT_CD IN ('Y', 'CF', 'F')
# 	AND a.store_cd = storeCd) f ON
# a.CHNL_SEND_DATE >= f.APRV_DATE
# AND a.CHNL_SEND_DATE <![CDATA[<=]]> f.END_DATE
# AND e.CHNL_ID = f.chnl_id
# INNER JOIN ${jdbc.QuadMax.SchemaName}RPLAN_JOIN g ON
# b1.SHOP_CD = g.STORE_CD
# AND a.CHNL_SEND_DATE >= g.RPLAN_JOIN_DT
# AND a.CHNL_SEND_DATE <![CDATA[<=]]> g.RPLAN_END_DT
# AND f.RPLAN_ID = g.RPLAN_ID
# INNER JOIN ${jdbc.QuadMax.SchemaName}RPLAN_LIST h ON
# g.RPLAN_ID = h.RPLAN_ID
# LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values I ON
# I.LOOKUP_TYPE = 'PROM_TYPE'
# AND f.PROM_TYPE = I.LOOKUP_CODE
# LEFT OUTER JOIN cmsmart.I_CDW_CMS_TMP_CMP_STOR_CUST_DSTRB J ON
# A.CAMP_ID = J.CMP_ID
# AND b1.SHOP_CD = J.STOR_CD
# WHERE 1 = 1
# AND (a.CHNL_SEND_YM = yyyymm
# 	OR a.CHNL_SEND_YM = substring(date_format(date_sub(str_to_date(concat(#{yyyymm}, '01'), '%Y%m%d'), INTERVAL 1 MONTH), '%Y%m%d'), 1, 6)) AND b1.shop_cd = f.store_cd AND b.bill_chrg_cd = b2.dept_gp_cd GROUP BY a.CHNL_SEND_YM, a.CHNL_SEND_DATE, e.chnl_id, e.CHNL_NAME, f.prom_send_cnt, f.PROMOTION_ID, f.promotion_nm, I.LOOKUP_NAME, f.aprv_date, concat(f.prom_send_cnt, '건 무료')) T) Z WHERE 1 = 1 AND Z.rn = 1 AND Z.CHNL_SEND_YM = yyyymm
# """

sql_query ="""SELECT CONCAT(SUBSTRING(#{yyyymm}, 1, 4), '년 ', SUBSTRING(#{yyyymm}, 5, 2), '월') AS USE_MONTH
     , T1.STORECD AS STORE_CD
     , T3.DEPT_NAME AS STORE_NM
     , T6.LOOKUP_NAME AS DSFRC_NM
     , '' AS BUSINESS_NO
     , T5.EMP_NAME AS SV_EMPNAME
     , T1.CHNL_NAME AS CHNL_NAME
     , T1.SEND_CNT AS CHNL_SEND_CNT
     , CAST(ROUND(T1.CHNL_UNIT_PRICE, 1) AS DECIMAL(20, 1)) AS CHNL_UNIT_PRICE
     , CAST(ROUND(T1.CHNL_UNIT_FEE, 1) AS DECIMAL(20, 1)) AS CHNL_UNIT_FEE
     , CAST(ROUND(T1.CHNL_UNIT_PRICE_SH, 1) AS DECIMAL(20, 1)) AS CHNL_UNIT_PRICE_SH
     , CAST(T1.send_amt AS DECIMAL(20, 0)) AS CHNL_SEND_AMT
     , T2.aprv_date AS APRV_DATE
     , T2.PROMOTION_ID AS PROMOTION_ID
     , T2.promotion_nm AS PROMOTION_NM
     , T2.PROM_APLY_RPLAN_NM AS PROM_APLY_RPLAN_NM
     , T2.PROM_TYPE AS PROM_TYPE
     , T2.prom_desc AS PROM_DESC
     , T2.CHNL_NAME AS PROM_CHNL_NAME
     , ROUND(SUM(IFNULL(T2.REAL_CNT, 0)), 0) AS PROM_APLY_CHNL_SEND_CNT
     , CAST(ROUND(SUM(IFNULL(T2.REAL_CNT, 0) * T1.CHNL_UNIT_PRICE_SH), 0) AS DECIMAL(20, 0)) AS PROM_APLY_CHNL_SEND_AMT
     , CAST(ROUND(sum((T1.SEND_CNT - IFNULL(T2.REAL_CNT, 0)) * T1.CHNL_UNIT_PRICE_SH), 0) AS DECIMAL(20, 0)) AS CHNL_SEND_AMT_AFT_PROM
  FROM(SELECT a.CHNL_SEND_YM
             , c.STORECD
             , e.chnl_id
             , e.CHNL_NAME
             , e.CHNL_UNIT_PRICE
             , e.CHNL_UNIT_FEE
             , sum(CASE WHEN h.STOR_DSTRB_CUST_CNT IS NOT NULL THEN h.STOR_DSTRB_CUST_CNT
                        									   ELSE a.CHNL_SEND_CNT 
                        									   END) AS send_cnt
             , e.CHNL_UNIT_PRICE_SH
             , sum(CASE WHEN h.STOR_DSTRB_CUST_CNT IS NOT NULL THEN h.STOR_DSTRB_CUST_CNT
                        									   ELSE a.CHNL_SEND_CNT 
                        									   END) * e.CHNL_UNIT_PRICE_SH AS send_amt
          FROM ${jdbc.QuadMaxMart.SchemaName}i_ums_cms_chnl_send_sum a
			   INNER JOIN ${jdbc.QuadMax.SchemaName}t_campaign b
		    ON a.CAMP_ID = b.CAMP_ID
		       INNER JOIN ${jdbc.QuadMax.SchemaName}t_camp_bill_shop b1
		    ON b.camp_id = B1.camp_id
		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}Z_CAMPAIGN b2
		    ON a.CAMP_ID = b2.CAMP_ID
		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}z_camp_cell b3
		    ON b2.CAMP_ID = b3.CAMP_ID
	       AND b2.CAMP_EXEC_NO = b3.CAMP_EXEC_NO
		  	   INNER JOIN ${jdbc.QuadMaxMart.SchemaName}i_cdw_cms_cdw_ria_smt100tm c
		    ON b1.shop_cd = c.STORECD
		  	   INNER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values d
		    ON a.CHNL_CD = d.VAL10
		   AND d.LOOKUP_TYPE = 'CHANNEL_TYPE'
		  	   INNER JOIN ${jdbc.QuadMax.SchemaName}t_channel e
		    ON d.LOOKUP_CODE = e.CHNL_TYPE_CD
		       INNER JOIN ${jdbc.QuadMax.SchemaName}t_emp_dept f
		    ON b1.shop_cd = f.dept_id
		       LEFT OUTER JOIN ${jdbc.QuadMaxMart.SchemaName}I_CDW_CMS_TMP_CMP_STOR_CUST_DSTRB h
	        ON b.CAMP_ID = h.cmp_id
	       AND b2.CAMP_EXEC_NO = h.CMP_EXEC_NO
	       AND b3.CELL_NODE_ID = h.CMP_CUSTG_ID
	       AND b1.SHOP_CD = h.STOR_CD
         WHERE 1 = 1
	       AND a.CHNL_SEND_YM = #{yyyymm}
	       AND c.STORECD = #{storeCd}
	       AND b.bill_chrg_cd = f.dept_gp_cd
         GROUP BY a.CHNL_SEND_YM
             , e.chnl_id
             , e.chnl_name
             , e.CHNL_UNIT_PRICE
             , e.CHNL_UNIT_FEE
             , e.CHNL_UNIT_PRICE_SH
       ) T1
       LEFT OUTER JOIN
       (SELECT Z.CHNL_SEND_YM
             , Z.chnl_id
             , Z.CHNL_NAME
             , Z.PROMOTION_ID
             , Z.promotion_nm
             , Z.PROM_APLY_RPLAN_NM
             , Z.PROM_TYPE
             , Z.aprv_date
             , Z.prom_desc
             , CASE WHEN Z.sum_cnt - Z.m_sum_cnt = 0 THEN (CASE WHEN Z.prom_send_cnt >= Z.m_sum_cnt THEN Z.m_sum_cnt
                              																		ELSE Z.prom_send_cnt 
                              																		END)
			        WHEN Z.sum_cnt - Z.m_sum_cnt > 0 THEN (CASE WHEN Z.prom_send_cnt - (Z.sum_cnt - Z.m_sum_cnt) > 0 THEN (CASE WHEN Z.prom_send_cnt - (Z.sum_cnt - Z.m_sum_cnt) >= Z.m_sum_cnt THEN Z.m_sum_cnt
			                            																																						ELSE Z.prom_send_cnt - (Z.sum_cnt - Z.m_sum_cnt) 
			                            																																						END)
	              																									 ELSE 0 
	              																									 END)
			        ELSE 0 
			        END AS REAL_CNT
	     FROM(SELECT T.CHNL_SEND_YM
	                , T.CHNL_SEND_DATE
	                , T.chnl_id
	                , T.CHNL_NAME
	                , T.cnt
	                , T.PROMOTION_ID
	                , T.promotion_nm
	                , T.PROM_APLY_RPLAN_NM
	                , T.PROM_TYPE
	                , T.aprv_date
	                , T.prom_desc
	                , IFNULL(T.prom_send_cnt, 0) AS prom_send_cnt
	                , sum(T.cnt) OVER(PARTITION BY T.chnl_id ORDER BY T.chnl_send_date) AS sum_cnt
				    , sum(T.cnt) OVER(PARTITION BY T.chnl_send_YM, T.chnl_id ORDER BY T.chnl_send_date) AS m_sum_cnt
			        , ROW_NUMBER() OVER(PARTITION BY T.CHNL_SEND_YM, T.chnl_id ORDER BY T.CHNL_SEND_DATE DESC) AS rn
		         FROM(SELECT a.CHNL_SEND_YM
				            , a.CHNL_SEND_DATE
				            , e.chnl_id
				            , e.CHNL_NAME
							, sum(CASE WHEN J.STOR_CD IS NULL THEN A.CHNL_SEND_CNT
									   						  ELSE J.STOR_DSTRB_CUST_CNT 
									   						  END) AS cnt
						    , f.PROMOTION_ID
						    , f.promotion_nm
						    , h.RPLAN_NM AS PROM_APLY_RPLAN_NM
						    , I.LOOKUP_NAME AS PROM_TYPE
						    , f.aprv_date
						    , concat(f.prom_day_cnt, '일 ', f.prom_send_cnt, '건 무료') AS prom_desc
						    , f.prom_send_cnt
			             FROM ${jdbc.QuadMaxMart.SchemaName}i_ums_cms_chnl_send_sum a
						      INNER JOIN ${jdbc.QuadMax.SchemaName}t_campaign b
						   ON a.CAMP_ID = b.CAMP_ID
						      INNER JOIN ${jdbc.QuadMax.SchemaName}t_camp_bill_shop b1
						   ON b.camp_ID = b1.camp_ID
						 	  INNER JOIN ${jdbc.QuadMax.SchemaName}t_emp_dept b2
						   ON b1.shop_cd = b2.dept_id
							  INNER JOIN ${jdbc.QuadMaxMart.SchemaName}i_cdw_cms_cdw_ria_smt100tm c
					       ON b1.shop_cd = c.STORECD
						      INNER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values d
						   ON a.CHNL_CD = d.VAL10
						  AND d.LOOKUP_TYPE = 'CHANNEL_TYPE'
						      INNER JOIN ${jdbc.QuadMax.SchemaName}t_channel e
						   ON d.LOOKUP_CODE = e.CHNL_TYPE_CD
							  LEFT OUTER JOIN (SELECT a.PROMOTION_ID
										        , b.promotion_nm
										        , a.STORE_CD
										        , b.RPLAN_ID
										        , b.PROM_TYPE
										        , a.APRV_DATE
										        , b.PROM_DAY_CNT
										        , date_format(date_add(str_to_date(a.aprv_date, '%Y%m%d'), INTERVAL b.PROM_DAY_CNT - 1 DAY), '%Y%m%d') AS END_DATE
										        , c.CHNL_ID
										        , c.PROM_SEND_CNT
										     FROM ${jdbc.QuadMax.SchemaName}promotion_req a
												  INNER JOIN ${jdbc.QuadMax.SchemaName}promotion_list b
											   ON a.PROMOTION_ID = b.PROMOTION_ID
												  INNER JOIN ${jdbc.QuadMax.SchemaName}promotion_chnnl_capacity c
										       ON a.PROMOTION_ID = c.PROMOTION_ID
										    WHERE 1 = 1
											  AND b.prom_TYPE = 'CHNL_SEND_FREE'
											  AND a.APRV_STAT_CD IN ('Y', 'CF', 'F')
											  AND a.store_cd = #{storeCd}
										  ) f
					       ON a.CHNL_SEND_DATE >= f.APRV_DATE
						  AND a.CHNL_SEND_DATE <= f.END_DATE
						  AND e.CHNL_ID = f.chnl_id
						      INNER JOIN ${jdbc.QuadMax.SchemaName}RPLAN_JOIN g
						   ON b1.SHOP_CD = g.STORE_CD
						  AND a.CHNL_SEND_DATE >= g.RPLAN_JOIN_DT
						  AND a.CHNL_SEND_DATE <= g.RPLAN_END_DT
						  AND f.RPLAN_ID = g.RPLAN_ID
						      INNER JOIN ${jdbc.QuadMax.SchemaName}RPLAN_LIST h
						   ON g.RPLAN_ID = h.RPLAN_ID
						      LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values I
						   ON I.LOOKUP_TYPE = 'PROM_TYPE'
						  AND f.PROM_TYPE = I.LOOKUP_CODE
							  LEFT OUTER JOIN cmsmart.I_CDW_CMS_TMP_CMP_STOR_CUST_DSTRB J
						   ON A.CAMP_ID = J.CMP_ID
						  AND b1.SHOP_CD = J.STOR_CD
					    WHERE 1 = 1
						  AND (a.CHNL_SEND_YM = #{yyyymm}
						       OR a.CHNL_SEND_YM = substring(date_format(date_sub(str_to_date(concat(#{yyyymm}, '01'), '%Y%m%d'), INTERVAL 1 MONTH), '%Y%m%d'), 1, 6))
						  AND b1.shop_cd = f.store_cd
						  AND b.bill_chrg_cd = b2.dept_gp_cd
			            GROUP BY a.CHNL_SEND_YM
			                , a.CHNL_SEND_DATE
			                , e.chnl_id
			                , e.CHNL_NAME
						    , f.prom_send_cnt
						    , f.PROMOTION_ID
						    , f.promotion_nm
						    , I.LOOKUP_NAME
						    , f.aprv_date
						    , concat(f.prom_send_cnt, '건 무료')
				    ) T
	           ) Z
		 WHERE 1 = 1
		   AND Z.rn = 1
		   AND Z.CHNL_SEND_YM = #{yyyymm}
	   ) T2
    ON T1.CHNL_SEND_YM = T2.CHNL_SEND_YM
   AND t1.chnl_id = t2.chnl_id
       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}T_EMP_DEPT T3
    ON T1.STORECD = T3.DEPT_ID
       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_emp T5
    ON T4.SV_EMPNO = T5.ORG_USER_CODE
       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}T_LOOKUP_VALUES T6
    ON T6.LOOKUP_TYPE = 'GRS_DSFRC_CD'
   AND T3.DSFRC_CD = T6.LOOKUP_CODE
 WHERE 1 = 1
 GROUP BY T1.STORECD
     , T3.DEPT_NAME 
     , T6.LOOKUP_NAME
     , T5.EMP_NAME 
     , T1.CHNL_NAME 
     , T1.SEND_CNT 
     , T1.CHNL_NAME 
     , T1.SEND_CNT
     , T1.CHNL_UNIT_PRICE
     , T1.CHNL_UNIT_FEE
     , T1.CHNL_UNIT_PRICE_SH
     , T1.send_amt
     , T2.PROMOTION_ID
     , T2.promotion_nm
     , T2.PROM_APLY_RPLAN_NM
     , T2.PROM_TYPE
     , T2.aprv_date
     , T2.prom_desc
     , T2.CHNL_NAME
 """

# sql_query = """SELECT 
#     T1.STORECD, 
#     T1.CHNL_NAME, 
#     T1.SEND_CNT, 
#     (SELECT SUM(T2.REAL_CNT) 
#      FROM promotion_details T2
#      WHERE T2.PROMOTION_ID = T1.PROMOTION_ID
#      AND T2.CHNL_ID = T1.CHNL_ID) AS PROMO_APPLIED_COUNT
# FROM 
#     channel_send_data T1
# GROUP BY 
#     T1.STORECD, 
#     T1.CHNL_NAME, 
#     T1.SEND_CNT;
# """

sql_query ="""SELECT SALE_DT AS '구매년월'
     , GENDER AS '성별'
     , AGE_GROUP AS '연령대'
     , GRADE AS '회원 등급'
     , COUNT(DISTINCT CUS_CD) AS '구매 고객 수'
     , SUM(SALE_AMT) AS '구매 금액'
     , ROUND(SUM(SALE_AMT) / COUNT(DISTINCT CUS_CD), 2) AS '객단가'
     , COUNT(RECP_NO) AS '구매 건수'
     , ROUND(SUM(SALE_AMT) / COUNT(RECP_NO), 2) AS '건단가'
FROM(SELECT SUBSTRING(SALE_DT, 1, 6) AS SALE_DT
             , SALES.CUS_CD AS CUS_CD
             , RECP_NO
             , SALE_AMT
             , IFNULL(cd1.cd_name, '미정의') AS GENDER
             , IFNULL(cd2.cd_name, '미정의') AS AGE_GROUP
             , IFNULL(cd3.cd_name, '미정의') AS GRADE
             , IFNULL(cd1.cd, '미정의') AS GENDER_CD
             , IFNULL(cd2.cd, '미정의') AS AGE_GROUP_CD
             , IFNULL(cd3.cd, '미정의') AS GRADE_CD
FROM(SELECT SALE_DT
                     , CUS_CD
                     , SALE_AMT
                     , RECP_NO
FROM CSDW_SALE_INFO
WHERE SALE_DT BETWEEN @startdate AND @enddate
               ) SALES
LEFT OUTER JOIN CSDW_CUST_INFO CUST                
            ON
SALES.CUS_CD = CUST.CUS_CD
LEFT OUTER JOIN COMM_CD_INFO cd1
            ON
(CUST.SEX % 2 = cd1.CD % 2)
AND (CUST.SEX != '')
AND cd1.grp_cd = 'CR003'
LEFT OUTER JOIN COMM_CD_INFO cd2
            ON
CUST.CUR_AGRP_CD = cd2.cd
AND cd2.grp_cd = 'CS102'
LEFT OUTER JOIN COMM_CD_INFO cd3
            ON
CUST.CUS_GRADE1 = cd3.CD
AND cd3.grp_cd = 'CR007'
       ) A
GROUP BY SALE_DT
     , GENDER_CD
     , AGE_GROUP_CD
     , GRADE_CD"""



sql_query ="""SELECT 
    SALE_DT AS '구매년월',
    GENDER AS '성별',
    AGE_GROUP AS '연령대',
    GRADE AS '회원 등급',
    COUNT(DISTINCT CUS_CD) AS '구매 고객 수',
    SUM(SALE_AMT) AS '구매 금액',
    ROUND(SUM(SALE_AMT) / COUNT(DISTINCT CUS_CD), 2) AS '객단가',
    COUNT(RECP_NO) AS '구매 건수',
    CAST(ROUND(SUM(TOT.RPLAN_USE_AMT), 0) AS DECIMAL(20, 0)) AS RPLAN_USE_AMT ,
    CASE 
        WHEN (TABLEA != 3 OR TABLEB != 2) THEN '조건 만족'
        ELSE '조건 불만족'
    END AS '조건 만족 여부',
      CASE WHEN (TABLEA IN (3, 5) OR TABLEB IN (2, 4, 6)) AND (TABLEA = 3 OR TABLEB = 2) THEN '조건 만족'
            ELSE '조건 불만족'
            END AS '조건 만족 여부',
    CASE 
    WHEN TABLEA BETWEEN 1 AND 10 OR TABLEB BETWEEN 5 AND 20 THEN '조건 만족'
    ELSE '조건 불만족'
END AS '조건 만족 여부',
CASE 
    WHEN TABLEA IN (3, 5) OR TABLEB IN (2, 4, 6) THEN '조건 만족'
    ELSE '조건 불만족'
END AS '조건 만족 여부',
CASE 
    WHEN TABLEA LIKE 'prefix%' OR TABLEB LIKE '%suffix' THEN '조건 만족'
    ELSE '조건 불만족'
END AS '조건 만족 여부',
CASE 
    WHEN TABLEA IS NULL OR TABLEB IS NULL THEN '조건 만족'
    ELSE '조건 불만족'
END AS '조건 만족 여부',
CASE 
    WHEN TABLEA NOT IN (3, 5) OR TABLEB NOT IN (2, 4, 6) THEN '조건 만족'
    ELSE '조건 불만족'
END AS '조건 만족 여부',
    ROUND(SUM(SALE_AMT) / COUNT(RECP_NO), 2) AS '건단가',
CASE WHEN RIGHT ( A2.STORE_NM, 1) = '점' THEN (CASE WHEN A1.SHOP_COUNT > 1 THEN CONCAT (A2.STORE_NM, ' 외 ', A1.SHOP_COUNT - 1, '점') 
                                                                           ELSE A2.STORE_NM 
                                                                           END) 
     ELSE (CASE WHEN A1.SHOP_COUNT > 1 THEN CONCAT (A2.STORE_NM, '점 외 ', A1.SHOP_COUNT - 1, '점') 
                                        ELSE A2.STORE_NM 
                                        END ) 
     END AS BILL_SHOP_NAME
FROM (
    SELECT 
        SUBSTRING(SALE_DT, 1, 6) AS SALE_DT,
        SALES.CUS_CD AS CUS_CD,
        RECP_NO,
     CASE WHEN (TABLEA IN (3, 5) OR TABLEB IN (2, 4, 6)) AND (TABLEA = 3 OR TABLEB = 2) THEN '조건 만족'
            ELSE '조건 불만족'
            END AS '조건 만족 여부',
        SALE_AMT,
        IFNULL(cd1.cd_name, '미정의') AS GENDER,
        IFNULL(cd2.cd_name, '미정의') AS AGE_GROUP,
        IFNULL(cd3.cd_name, '미정의') AS GRADE,
        IFNULL(cd1.cd, '미정의') AS GENDER_CD,
        IFNULL(cd2.cd, '미정의') AS AGE_GROUP_CD,
        IFNULL(cd3.cd, '미정의') AS GRADE_CD,
        TABLEA,
        TABLEB
    FROM (
        SELECT 
            SALE_DT,
          CASE WHEN (TABLEA IN (3, 5) OR TABLEB IN (2, 4, 6)) AND (TABLEA = 3 OR TABLEB = 2) THEN '조건 만족'
            ELSE '조건 불만족'
            END as '조건 만족 여부',
            CUS_CD,
            SALE_AMT,
            RECP_NO
        FROM CSDW_SALE_INFO
        WHERE 1=1 
        and SALE_DT BETWEEN @startdate AND @enddate
        and (TABLEA = 3 OR TABLEB = 2)
        and (a = 1 AND b = 2) OR (a = 3 AND b = 4)
    ) SALES
    LEFT OUTER JOIN CSDW_CUST_INFO CUST 
        ON SALES.CUS_CD = CUST.CUS_CD
       AND (TABLEA = 3 OR TABLEB = 2)
    LEFT OUTER JOIN COMM_CD_INFO cd1 
        ON (CUST.SEX % 2 = cd1.CD % 2) 
        AND (CUST.SEX != '') 
        AND cd1.grp_cd = 'CR003'
        OR (TABLEA = 3 AND TABLEB = 2)
    LEFT OUTER JOIN COMM_CD_INFO cd2 
        ON CUST.CUR_AGRP_CD = cd2.cd 
        AND cd2.grp_cd = 'CS102'
    LEFT OUTER JOIN COMM_CD_INFO cd3 
        ON CUST.CUS_GRADE1 = cd3.CD 
        AND cd3.grp_cd = 'CR007'
        AND CURRENT_DATE BETWEEN c.start_date AND c.end_date
     left JOIN discount_rules d
  ON c.total_spent BETWEEN d.min_amount AND d.max_amount
  right JOIN time_slots s
  ON t.transaction_time BETWEEN s.start_time AND s.end_time
  cross JOIN locations l
  ON l.latitude BETWEEN e.min_lat AND e.max_lat
 AND l.longitude BETWEEN e.min_lng AND e.max_lng;
) A
WHERE 1 = 1
  AND (a.CHNL_SEND_YM = yyyymm 
       OR a.CHNL_SEND_YM = SUBSTRING(
           DATE_FORMAT(DATE_SUB(STR_TO_DATE(CONCAT(#{yyyymm}, '01'), '%Y%m%d'), INTERVAL 1 MONTH), '%Y%m%d'), 
           1, 6)
      )
  AND (TABLEA = 3 OR TABLEB = 2) 
     and (salary BETWEEN 3000 AND 5000 AND bonus BETWEEN 500 AND 1000)
    OR (hire_date BETWEEN '2020-01-01' AND '2021-01-01')
    AND department_id BETWEEN 10 AND 50;
GROUP BY 1=1 ,SALE_DT, 
         GENDER_CD, 
         AGE_GROUP_CD, 
         GRADE_CD,
         CASE 
        WHEN a = 1 AND b = 2 THEN '조건1'
        ELSE '조건2'
    END
HAVING (a = 1 AND b = 2) OR (a = 3 AND b = 4)AND SALE_DT BETWEEN @startdate AND @enddate and     (salary BETWEEN 3000 AND 5000 AND bonus BETWEEN 500 AND 1000)
    OR (hire_date BETWEEN '2020-01-01' AND '2021-01-01')
    AND department_id BETWEEN 10 AND 50
ORDER BY 1=1,
    CASE WHEN TABLEA = 3 OR TABLEB = 2 THEN 1 ELSE 0 END DESC,
    STR_TO_DATE(SALE_DT, '%Y%m') DESC, 
    ROUND(SUM(SALE_AMT) / COUNT(DISTINCT CUS_CD), 2) DESC,
    GENDER ASC,
    (a = 1 AND b = 2) DESC;
"""

sql_query ="""SELECT A.CAMP_ID,
       CASE
           WHEN LENGTH(A.CAMP_NAME) > 128 THEN CONCAT(SUBSTRING(A.CAMP_NAME, 1, 128), '...')
           ELSE A.CAMP_NAME
       END AS CAMP_NAME,
       CASE
           WHEN F.camp_id IS NOT NULL THEN F.bill_shop_cd
           ELSE C.SHOP_CD
       END AS SHOP_CD,
       CASE
           WHEN F.camp_id IS NOT NULL THEN IFNULL(F.bill_shop_name, '점포 불명')
           ELSE IFNULL(E.STORE_NM, '점포 불명')
       END AS BILL_SHOP_NAME,
       A.CAMP_SDATE,
       A.CAMP_EDATE,
       MIN(E.DIVCD) AS divCd
FROM cmsmeta.T_CAMPAIGN A
LEFT JOIN cmsmeta.T_EMP_DEPT B ON A.REG_DEPT_ID = B.DEPT_ID
INNER JOIN cmsmeta.T_CAMP_BILL_SHOP C ON A.CAMP_ID = C.CAMP_ID
LEFT JOIN cmsmart.cluster_stor_list D ON C.SHOP_CD = D.STORE_CD
LEFT JOIN cmsmart.I_CDW_CMS_CDW_RIA_SMT100TM E ON C.SHOP_CD = E.STORECD
LEFT JOIN (
    SELECT A1.CAMP_ID AS CAMP_ID,
           CASE
               WHEN A1.SHOP_COUNT > 1 THEN CONCAT(A1.SHOP_CD, ' 외 ', A1.SHOP_COUNT - 1, '점')
               ELSE A1.SHOP_CD
           END AS BILL_SHOP_CD,
           CASE
               WHEN RIGHT(A2.STORE_NM, 1) = '점' THEN
                    (CASE
                        WHEN A1.SHOP_COUNT > 1 THEN CONCAT(A2.STORE_NM, ' 외 ', A1.SHOP_COUNT - 1, '점')
                        ELSE A2.STORE_NM
                    END)
               ELSE
                    ( CASE
                        WHEN A1.SHOP_COUNT > 1 THEN CONCAT(A2.STORE_NM, '점 외 ', A1.SHOP_COUNT - 1, '점')
                        ELSE A2.STORE_NM
                    END)
           END AS BILL_SHOP_NAME
    FROM (
        SELECT BS.CAMP_ID,
               COUNT(BS.CAMP_ID) AS SHOP_COUNT,
               MIN(BS.SHOP_CD) AS SHOP_CD
        FROM cmsmeta.T_CAMP_BILL_SHOP BS
        GROUP BY BS.CAMP_ID
    ) A1
    INNER JOIN cmsmart.I_CDW_CMS_CDW_RIA_SMT100TM A2 ON A1.SHOP_CD = A2.STORECD
    WHERE A1.SHOP_COUNT > 1
) F ON A.CAMP_ID = F.CAMP_ID
WHERE A.DEL_F = 'N'
  AND A.BRAND_CD = '00'
  AND A.CSTS_ID IN ('006', '007', '008', '009', '100')
  AND A.CAMP_BASE_TYPE = 'TARGET'
  AND (
      'Y' = (
          SELECT MAX(AW.ALL_CAMP_SELECT_AUTH_YN)
          FROM cmsmeta.T_EMP_MENU_AUTH AW
          WHERE AW.MATH_ID IN (
              SELECT AWA.MATH_ID
              FROM cmsmeta.T_EMP_AUTH AWA
              WHERE AWA.EMP_ID = 'crmadm'
                AND AWA.DEPT_ID = '999999'
          )
      )
      OR 1 = 1
  )
GROUP BY A.CAMP_ID,
         CASE
             WHEN LENGTH(A.CAMP_NAME) > 128 THEN CONCAT(SUBSTRING(A.CAMP_NAME, 1, 128), '...')
             ELSE A.CAMP_NAME
         END,
         CASE
             WHEN F.camp_id IS NOT NULL THEN F.bill_shop_cd
             ELSE C.SHOP_CD
         END,
          CASE
               WHEN RIGHT(A2.STORE_NM, 1) = '점' THEN
                    (CASE
                        WHEN A1.SHOP_COUNT > 1 THEN CONCAT(A2.STORE_NM, ' 외 ', A1.SHOP_COUNT - 1, '점')
                        ELSE A2.STORE_NM
                    END)
               ELSE
                    (CASE
                        WHEN A1.SHOP_COUNT > 1 THEN CONCAT(A2.STORE_NM, '점 외 ', A1.SHOP_COUNT - 1, '점')
                        ELSE A2.STORE_NM
                    END)
           END AS BILL_SHOP_NAME,
         A.CAMP_SDATE,
         A.CAMP_EDATE
ORDER BY A.CAMP_SDATE DESC,
         A.CAMP_ID DESC,
                   CASE
               WHEN RIGHT(A2.STORE_NM, 1) = '점' THEN
                    (CASE
                        WHEN A1.SHOP_COUNT > 1 THEN CONCAT(A2.STORE_NM, ' 외 ', A1.SHOP_COUNT - 1, '점')
                        ELSE A2.STORE_NM
                    END)
               ELSE
                    (CASE
                        WHEN A1.SHOP_COUNT > 1 THEN CONCAT(A2.STORE_NM, '점 외 ', A1.SHOP_COUNT - 1, '점')
                        ELSE A2.STORE_NM
                    END)
           END AS BILL_SHOP_NAME,
           CASE WHEN A1.SHOP_COUNT > 1 THEN CONCAT (A1.SHOP_CD, ' 외 ', A1.SHOP_COUNT - 1, '점') 
                                                     ELSE A1.SHOP_CD 
                                                     END AS BILL_SHOP_CD
LIMIT 16;
"""
sql_query="""SELECT CONCAT(SUBSTRING(#{yyyymm} /* 변수 처리 조회월 */, 1, 4), '년 ', SUBSTRING(#{yyyymm} /* 변수 처리 조회월 */, 5, 2), '월') AS USE_MONTH /* 조회월 */
     , T1.STORECD														AS STORE_CD				/* 점포 코드 */
     , T3.DEPT_NAME 													AS STORE_NM				/* 점포명*/
     , T6.LOOKUP_NAME 													AS DSFRC_NM				/* 직,가구분 */
     , '' 																AS BUSINESS_NO			/* 사업,자번호 */
     , T5.EMP_NAME 														AS SV_EMPNAME			/* 담당 SV 이,름 */
     , T1.CHNL_NAME 													AS CHNL_NAME 			/* 발송 채널 (화면) */
	 , T1.SEND_CNT 														AS CHNL_SEND_CNT 		/* 발송(건수 (건) (화면) */
	 , CAST(ROUND(T1.CHNL_UNIT_PRICE, 1) AS DECIMAL(20, 1))				AS CHNL_UNIT_PRICE	 	/* 발송단가 기본료(원) */
	 , CAST(ROUND(T1.CHNL_UNIT_FEE, 1) AS DECIMAL(20, 1))				AS CHNL_UNIT_FEE 	 	/* 발송단가 수수료(원) */
	 , CAST(ROUND(T1.CHNL_UNIT_PRICE_SH, 1) AS DECIMAL(20, 1))			AS CHNL_UNIT_PRICE_SH 	/* 발송단가 (원) (화면) */
	 , CAST(T1.send_amt AS DECIMAL(20, 0))								AS CHNL_SEND_AMT 		/* (프로모션 적용 전) 발송금액 (원) (화면) */
	 , T2.aprv_date 													AS APRV_DATE 			/* 프로모션 적용일 (화면) */
	 , T2.PROMOTION_ID 													AS PROMOTION_ID 		/* 프로모션ID (화면) */
	 , T2.promotion_nm 													AS PROMOTION_NM 		/* 프로모션명 (화면) */
	 , T2.PROM_APLY_RPLAN_NM											AS PROM_APLY_RPLAN_NM	/* 프로모션 대상 요금제 (화면) */
	 , T2.PROM_TYPE 													AS PROM_TYPE 			/* 프로모션 종류 (화면) */
	 , T2.prom_desc 													AS PROM_DESC 			/* 프로모션 내용 (화면) */
	 , T2.CHNL_NAME														AS PROM_CHNL_NAME		/* 프로모션 적용 채널 (화면) */ 
	 , ROUND(SUM(IFNULL(T2.REAL_CNT, 0)), 0)							AS PROM_APLY_CHNL_SEND_CNT	/* (프로모션 무료) 발송건수 (건) (화면) */
	 , CAST(ROUND(SUM(IFNULL(T2.REAL_CNT, 0) * T1.CHNL_UNIT_PRICE_SH), 0) AS DECIMAL(20, 0))					AS PROM_APLY_CHNL_SEND_AMT	/* (프로모션 무료) 발송금액 (원) (화면) */
	 , CAST(ROUND(sum((T1.SEND_CNT - IFNULL(T2.REAL_CNT, 0)) * T1.CHNL_UNIT_PRICE_SH), 0) AS DECIMAL(20, 0))	AS CHNL_SEND_AMT_AFT_PROM /* (프로모션 적용 후) 발송금액 (원) (화면) */
  FROM (SELECT a.CHNL_SEND_YM
             , c.STORECD
             , e.chnl_id
             , e.CHNL_NAME
             , e.CHNL_UNIT_PRICE
             , e.CHNL_UNIT_FEE
             , sum(CASE WHEN h.STOR_DSTRB_CUST_CNT IS NOT NULL 
                        THEN h.STOR_DSTRB_CUST_CNT
                        ELSE a.CHNL_SEND_CNT END) AS send_cnt
             , e.CHNL_UNIT_PRICE_SH
             , sum(CASE WHEN h.STOR_DSTRB_CUST_CNT IS NOT NULL 
                        THEN h.STOR_DSTRB_CUST_CNT
                        ELSE a.CHNL_SEND_CNT END) * e.CHNL_UNIT_PRICE_SH AS send_amt
          FROM ${jdbc.QuadMaxMart.SchemaName}i_ums_cms_chnl_send_sum a /* UMS 채널발송정보 */
			   INNER JOIN ${jdbc.QuadMax.SchemaName}t_campaign b
		    ON a.CAMP_ID = b.CAMP_ID
		       INNER JOIN ${jdbc.QuadMax.SchemaName}t_camp_bill_shop b1
		    ON b.camp_id = B1.camp_id
		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}Z_CAMPAIGN b2
		    ON a.CAMP_ID = b2.CAMP_ID
		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}z_camp_cell b3
		    ON b2.CAMP_ID = b3.CAMP_ID
	       AND b2.CAMP_EXEC_NO = b3.CAMP_EXEC_NO
		  	   INNER JOIN ${jdbc.QuadMaxMart.SchemaName}i_cdw_cms_cdw_ria_smt100tm c
		    ON b1.shop_cd = c.STORECD
		  	   INNER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values d
		    ON a.CHNL_CD = d.VAL10
		   AND d.LOOKUP_TYPE = 'CHANNEL_TYPE'
		  	   INNER JOIN ${jdbc.QuadMax.SchemaName}t_channel e
		    ON d.LOOKUP_CODE = e.CHNL_TYPE_CD
		       INNER JOIN ${jdbc.QuadMax.SchemaName}t_emp_dept f
		    ON b1.shop_cd = f.dept_id
		       LEFT OUTER JOIN ${jdbc.QuadMaxMart.SchemaName}I_CDW_CMS_TMP_CMP_STOR_CUST_DSTRB h
	        ON b.CAMP_ID = h.cmp_id
	       AND b2.CAMP_EXEC_NO = h.CMP_EXEC_NO
	       AND b3.CELL_NODE_ID = h.CMP_CUSTG_ID
	       AND b1.SHOP_CD = h.STOR_CD
         WHERE 1 = 1
	       AND a.CHNL_SEND_YM = #{yyyymm} /* 화면 INPUT 조회월 */
	       AND c.STORECD = #{storeCd} /* 화면 INPUT 점포코드 */
	       AND b.bill_chrg_cd = f.dept_gp_cd
         GROUP BY a.CHNL_SEND_YM
             , e.chnl_id
             , e.chnl_name
             , e.CHNL_UNIT_PRICE
             , e.CHNL_UNIT_FEE
             , e.CHNL_UNIT_PRICE_SH
       ) T1
       LEFT OUTER JOIN
       (SELECT Z.CHNL_SEND_YM
        --   , Z.CHNL_SEND_DATE
             , Z.chnl_id
             , Z.CHNL_NAME
             , Z.PROMOTION_ID
             , Z.promotion_nm
             , Z.PROM_APLY_RPLAN_NM
             , Z.PROM_TYPE
             , Z.aprv_date
             , Z.prom_desc
             , CASE WHEN Z.sum_cnt - Z.m_sum_cnt = 0 THEN
                         (CASE WHEN Z.prom_send_cnt >= Z.m_sum_cnt THEN Z.m_sum_cnt
                              ELSE Z.prom_send_cnt END)
			        WHEN Z.sum_cnt - Z.m_sum_cnt > 0 THEN
			             (CASE WHEN Z.prom_send_cnt - (Z.sum_cnt - Z.m_sum_cnt) > 0 THEN
			                       (CASE WHEN Z.prom_send_cnt - (Z.sum_cnt - Z.m_sum_cnt) >= Z.m_sum_cnt THEN Z.m_sum_cnt
			                            ELSE Z.prom_send_cnt - (Z.sum_cnt - Z.m_sum_cnt) END)
				              ELSE 0 END)
			        ELSE 0 END AS REAL_CNT /* 발송기간 내 프로모션적용 건수 계싼 */
	     FROM (SELECT T.CHNL_SEND_YM
	                , T.CHNL_SEND_DATE
	                , T.chnl_id
	                , T.CHNL_NAME
	                , T.cnt
	                , T.PROMOTION_ID
	                , T.promotion_nm
	                , T.PROM_APLY_RPLAN_NM
	                , T.PROM_TYPE
	                , T.aprv_date
	                , T.prom_desc
	                , IFNULL(T.prom_send_cnt, 0) AS prom_send_cnt
	                , sum(T.cnt) OVER(PARTITION BY T.chnl_id ORDER BY T.chnl_send_date) AS sum_cnt /* 조회기간동안의 총 누적합 */
				    , sum(T.cnt) OVER(PARTITION BY T.chnl_send_YM, T.chnl_id ORDER BY T.chnl_send_date) AS m_sum_cnt /*조회기간내  월별 누적합 */
			 	    /* , sum(T.cnt) OVER(ORDER BY T.chnl_send_date) - T.prom_send_cnt) */
			        , row_number() OVER(PARTITION BY T.CHNL_SEND_YM, T.chnl_id ORDER BY T.CHNL_SEND_DATE DESC) AS rn /* 월별 최종값을 구하기위한 rn */
		         FROM (SELECT a.CHNL_SEND_YM
				            , a.CHNL_SEND_DATE
				            , e.chnl_id
				            , e.CHNL_NAME
							, sum(CASE WHEN J.STOR_CD IS NULL
										   THEN A.CHNL_SEND_CNT
									   ELSE J.STOR_DSTRB_CUST_CNT END) 		AS cnt
						    , f.PROMOTION_ID
						    , f.promotion_nm
						    , h.RPLAN_NM 				AS PROM_APLY_RPLAN_NM
						    , I.LOOKUP_NAME 			AS PROM_TYPE
						    , f.aprv_date
						    , concat(f.prom_day_cnt, '일 ', f.prom_send_cnt, '건 무료') AS prom_desc
						    , f.prom_send_cnt
			             FROM ${jdbc.QuadMaxMart.SchemaName}i_ums_cms_chnl_send_sum a
						      INNER JOIN ${jdbc.QuadMax.SchemaName}t_campaign b
						   ON a.CAMP_ID = b.CAMP_ID
						      INNER JOIN ${jdbc.QuadMax.SchemaName}t_camp_bill_shop b1
						   ON b.camp_ID = b1.camp_ID
						 	  INNER JOIN ${jdbc.QuadMax.SchemaName}t_emp_dept b2
						   ON b1.shop_cd = b2.dept_id
							  INNER JOIN ${jdbc.QuadMaxMart.SchemaName}i_cdw_cms_cdw_ria_smt100tm c
					       ON b1.shop_cd = c.STORECD
						      INNER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values d
						   ON a.CHNL_CD = d.VAL10
						  AND d.LOOKUP_TYPE = 'CHANNEL_TYPE'
						      INNER JOIN ${jdbc.QuadMax.SchemaName}t_channel e
						   ON d.LOOKUP_CODE = e.CHNL_TYPE_CD
							  LEFT OUTER JOIN
							  (SELECT a.PROMOTION_ID
							        , b.promotion_nm
							        , a.STORE_CD
							        , b.RPLAN_ID
							        , b.PROM_TYPE
							        , a.APRV_DATE
							        , b.PROM_DAY_CNT
							        , date_format(date_add(str_to_date(a.aprv_date, '%Y%m%d'), INTERVAL b.PROM_DAY_CNT - 1 DAY), '%Y%m%d') AS END_DATE
							        , c.CHNL_ID
							        , c.PROM_SEND_CNT
							     FROM ${jdbc.QuadMax.SchemaName}promotion_req a
									  INNER JOIN ${jdbc.QuadMax.SchemaName}promotion_list b
								   ON a.PROMOTION_ID = b.PROMOTION_ID
									  INNER JOIN ${jdbc.QuadMax.SchemaName}promotion_chnnl_capacity c
							       ON a.PROMOTION_ID = c.PROMOTION_ID
							    WHERE 1 = 1
								  AND b.prom_TYPE = 'CHNL_SEND_FREE' /* 발송비프로모션 */
								  AND a.APRV_STAT_CD IN ('Y', 'CF', 'F') /* 프로모션 승인 완료 */
								  AND a.store_cd = #{storeCd} /* 화면 INPUT 점포 코드*/
							  ) f
					       ON a.CHNL_SEND_DATE >= f.APRV_DATE /* 프로모션 기간 내 발송 건 */
						  AND a.CHNL_SEND_DATE <![CDATA[<=]]>  f.END_DATE /* 프로모션 기간 내 발송 건 */
						  AND e.CHNL_ID = f.chnl_id
						      INNER JOIN ${jdbc.QuadMax.SchemaName}RPLAN_JOIN g
						   ON b1.SHOP_CD = g.STORE_CD
						  AND a.CHNL_SEND_DATE >= g.RPLAN_JOIN_DT
						  AND a.CHNL_SEND_DATE <![CDATA[<=]]>  g.RPLAN_END_DT
						  AND f.RPLAN_ID = g.RPLAN_ID
						      INNER JOIN ${jdbc.QuadMax.SchemaName}RPLAN_LIST h
						   ON g.RPLAN_ID = h.RPLAN_ID
						      LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values I
						   ON I.LOOKUP_TYPE = 'PROM_TYPE'
						  AND f.PROM_TYPE = I.LOOKUP_CODE
							  LEFT OUTER JOIN cmsmart.I_CDW_CMS_TMP_CMP_STOR_CUST_DSTRB J
						   ON A.CAMP_ID = J.CMP_ID
						  AND b1.SHOP_CD = J.STOR_CD
					    WHERE 1 = 1
						  AND (a.CHNL_SEND_YM = #{yyyymm} /* 화면 INPUT 조회월 */
						       OR a.CHNL_SEND_YM = substring(date_format(date_sub(str_to_date(concat(#{yyyymm}, '01'), '%Y%m%d'), INTERVAL 1 MONTH) , '%Y%m%d'), 1, 6))/* 당월 또는 전월 */
						  AND b1.shop_cd = f.store_cd
						  AND b.bill_chrg_cd = b2.dept_gp_cd
			            GROUP BY a.CHNL_SEND_YM
			                , a.CHNL_SEND_DATE
			                , e.chnl_id
			                , e.CHNL_NAME
						    , f.prom_send_cnt
						    , f.PROMOTION_ID
						    , f.promotion_nm
						    , I.LOOKUP_NAME
						    , f.aprv_date
						    , concat(f.prom_send_cnt, '건 무료')
				    ) T
	           ) Z
		 WHERE 1 = 1
		   AND Z.rn = 1
		   AND Z.CHNL_SEND_YM = #{yyyymm} /* 화면 INPUT 조회월 */
	   ) T2
    ON T1.CHNL_SEND_YM = T2.CHNL_SEND_YM
   AND t1.chnl_id = t2.chnl_id
       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}T_EMP_DEPT T3
    ON T1.STORECD = T3.DEPT_ID
       LEFT OUTER JOIN
       (SELECT STORECD					
             , SUBSTRING(WORK_DE, 1, 6) AS WORK_DE
             , SV_EMPNO					AS SV_EMPNO
             , ROW_NUMBER() OVER(PARTITION BY STORECD, SUBSTRING(WORK_DE, 1, 6) ORDER BY WORK_DE DESC) AS RN
          FROM ${jdbc.QuadMaxMart.SchemaName}CDW_RIA_SMT100TM_SV 
       ) T4
    ON T4.WORK_DE = #{yyyymm} /* 변수 처리 조회월 */
   AND T1.STORECD = T4.STORECD
   AND T4.RN = 1
       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_emp T5
    ON T4.SV_EMPNO = T5.ORG_USER_CODE
       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}T_LOOKUP_VALUES T6
    ON T6.LOOKUP_TYPE = 'GRS_DSFRC_CD'
   AND T3.DSFRC_CD = T6.LOOKUP_CODE
 WHERE 1 = 1
 GROUP BY T1.STORECD														
     , T3.DEPT_NAME 												
     , T6.LOOKUP_NAME 																												
     , T5.EMP_NAME 												
     , T1.CHNL_NAME 												
	 , T1.SEND_CNT 												
     , T1.CHNL_NAME
     , T1.SEND_CNT
     , T1.CHNL_UNIT_PRICE
     , T1.CHNL_UNIT_FEE
     , T1.CHNL_UNIT_PRICE_SH
     , T1.send_amt
     , T2.PROMOTION_ID
     , T2.promotion_nm
     , T2.PROM_APLY_RPLAN_NM
     , T2.PROM_TYPE
     , T2.aprv_date
     , T2.prom_desc
     , T2.CHNL_NAME

"""

# sql_query="""SELECT a.CMP_ID AS CMP_ID /* 캠페인ID */
#      , a.STD_YM AS STD_YM /* 기준년월 */
#      , a.cmp_custg_id AS cmp_custg_id /* 고객군ID */
#      , c.CONT_ID AS CHNNL_CN_ID /* 채널컨텐츠ID */
#      , c.CHNL_ID AS CMP_CHNNL_ID /* 채널ID */
#      , d.CUST_ID AS GNO /* GRS통합회원번호 */
#      , a.CMP_EXEC_NO AS CMP_EXEC_NO /* 캠페인실행회차 */
#      , CASE WHEN e.CHNG_CHNL_YN = 'Y' THEN e.CHNL_ID_1 
#                                       ELSE c.CHNL_ID 
#                                       END AS fst_chnnl_Id /* 1차채널ID */
#      , CASE WHEN d.CHNG_CHNL_YN = 'Y' THEN 'N' 
#                                       ELSE d.SUCCESS_YN 
#                                       END AS fst_chnnl_send_succ_yn /* 1차채널발송성공여부 */
#      , CASE WHEN d.CHNG_CHNL_YN = 'Y' THEN 'N' 
#                                       ELSE d.OPEN_YN 
#                                       END AS fst_chnnl_open_yn /* 1차채널오픈여부 */
#      , CASE WHEN f.DSFRC_CODE = '20' THEN /* 가맹 */ ( CASE WHEN e.CHNG_CHNL_YN = 'Y' THEN /* 전환채널O */ ( CASE WHEN d.CHNG_CHNL_YN = 'Y' THEN 0 /* 전환채널 1차 실패 */ 
#                                                                                                                                          ELSE tc1.CHNL_UNIT_PRICE_SH 
#                                                                                                                                          END ) /* 전환채널 1차 성공 */ 
#                                                                                     ELSE ( CASE WHEN d.SUCCESS_YN = 'Y' THEN e.CHNL_UNIT_PRICE_SH /* 전환채널 X , 발송성공*/ 
#                                                                                                                        ELSE 0 
#                                                                                                                        END ) /* 전환채널 X , 발송실패 */ 
#                                                                                     END  ) 
#                                      ELSE ( CASE WHEN e.CHNG_CHNL_YN = 'Y' THEN /* 직영 */ /* 전환채널O */ ( CASE WHEN d.CHNG_CHNL_YN = 'Y' THEN 0 /* 전촨채널 1차 실패 */ 
#                                                                                                                                         ELSE tc1.CHNL_UNIT_PRICE 
#                                                                                                                                         END  ) /* 전환채널 1차 성공 */ 
#                                                                           ELSE ( CASE WHEN d.SUCCESS_YN = 'Y' THEN e.CHNL_UNIT_PRICE /* 전환채널 X , 발송성공*/ 
#                                                                                                              ELSE 0 
#                                                                                                              END ) /* 전환채널 X , 발송실패 */ 
#                                                                           END  ) 
#                                      END AS fst_chnnl_cost /* 1차채널비용 */
#      , CASE WHEN e.CHNG_CHNL_YN = 'Y' THEN e.CHNL_ID_2 
#                                       ELSE NULL 
#                                       END AS snd_chnnl_id /* 2차채널ID */
#      , CASE WHEN d.CHNG_CHNL_YN = 'Y' THEN d.SUCCESS_YN 
#                                       ELSE NULL 
#                                       END AS snd_chnnl_send_succ_yn /* 2차채널발송성공여부 */
#      , CASE WHEN d.CHNG_CHNL_YN = 'Y' THEN d.OPEN_YN 
#                                       ELSE NULL 
#                                       END AS snd_chnnl_open_yn /* 2차채널오픈여부 */
#      , CASE WHEN e.CHNG_CHNL_YN = 'Y' THEN ( CASE WHEN f.DSFRC_CODE = '20' THEN ( CASE WHEN d.SUCCESS_YN = 'Y' AND d.CHNG_CHNL_YN = 'Y' THEN tc2.CHNL_UNIT_PRICE_SH 
#                                                                                                                                            ELSE 0 
#                                                                                                                                            END ) 
#                                                                            ELSE ( CASE WHEN d.SUCCESS_YN = 'Y' AND d.CHNG_CHNL_YN = 'Y' THEN e.CHNL_UNIT_PRICE_SH 
#                                                                                                                                        ELSE 0 
#                                                                                                                                        END  ) 
#                                                                            END  ) 
#                                       ELSE 0 
#                                       END AS snd_chnnl_cost /* 2차채널비용 */
#      , now () AS ETL_LOAD_DTTM /* ETL적재일시 */
#   FROM grs_dm.cdm_f_cmp_exec_no a /* 캠페인실행회차 */
#        INNER JOIN grs_dw.cdw_cmp_z_campaign b /* 캠페인실행이력 */
#     ON a.CMP_ID = b.CAMP_ID
#    AND a.CMP_EXEC_NO = b.CAMP_EXEC_NO
#        INNER JOIN grs_dw.cdw_cmp_z_chnl_send_req c /* 캠페인채널발송요청실행이력 */
#     ON a.CMP_ID = c.CAMP_ID
#    AND a.CMP_EXEC_NO = c.CAMP_EXEC_NO
#    AND a.cmp_custg_id = c.CELL_NODE_ID
#        INNER JOIN grs_dm.cdm_f_cmp_cust_info g
#     ON a.cmp_id = g.cmp_id
#    AND a.std_ym = g.std_ym
#    AND a.cmp_custg_id = g.cmp_custg_id
#    AND a.cmp_exec_no = g.cmp_exec_no
#        INNER JOIN grs_dw.cdw_cmp_z_chnl_send_req_cust d /* 캠페인채널발송요청고객실행이력 */
#     ON c.CHNL_SEND_REQ = d.CHNL_SEND_REQ
#    AND g.gno = d.cust_id
#        LEFT OUTER JOIN grs_dw.cdw_cmp_t_channel e /* 캠페인채널정보 */
#     ON c.CHNL_ID = e.CHNL_ID
#        LEFT OUTER JOIN grs_dw.cdw_ria_smt100tm f /* 점포마스터 */
#     ON b.REG_DEPT_ID = f.STORECD
#        LEFT OUTER JOIN grs_dw.cdw_cmp_t_channel tc1 /* 1차채널비용 */
#     ON e.CHNL_ID_1 = tc1.CHNL_ID
#        LEFT OUTER JOIN grs_dw.cdw_cmp_t_channel tc2 /* 2차채널비용 */
#     ON e.CHNL_ID_2 = tc2.CHNL_ID"""

sql_query="""SELECT A.CHNL_SEND_DATE 																	AS CHNL_SEND_DATE  		/* 발송일 */
		     , B.CAMP_ID        																	AS CAMP_ID  			/* 캠페인 ID */
		     , B.CAMP_NAME      																	AS CAMP_NAME 			/* 캠페인 명 */
		     , B.BRAND_CD      												    					AS BRAND_CD 			/* 브랜드명 */
		     , B.REG_DEPT_ID 																		AS REG_DEPT_ID
		     , B.REG_EMP_ID     																	AS REG_EMP_ID 			/* 담당자 ID */
		     , CASE WHEN E.CHNG_CHNL_YN = 'Y' 
		            THEN (CASE WHEN F1.VAL10 IS NOT NULL 
		                       THEN E1.CHNL_NAME
		     				   ELSE (CASE WHEN F2.VAL10 IS NOT NULL 
		     				              THEN E2.CHNL_NAME END) END)
			 		ELSE E.CHNL_NAME END 															AS CHNL_NAME 			/* 발송채널 ID */
		     , H.DSFRC_CODE 																								/* 직가구분 */
		     , G.SHOP_CD        																	AS SHOP_CD 				/* 대상 점포 코드 */
		     , H.STORE_NM       																	AS STORE_NM 			/* 대상 점포 명 */
		     , B.BILL_CHRG_CD  										  														/* 비용 부담 부서 */
		     , B.BILL_DEPT_CD  													                  							/* 정산 부서 */
		     , CASE WHEN E.CHNG_CHNL_YN IS NULL AND A.CHNL_CD = F.VAL10 
		            THEN (CASE WHEN D1.DETECT_SEQ IS NOT NULL
		                      THEN (CASE WHEN D1.CUST_TYPE_CD = 'T' THEN 1 ELSE 0 END)
		                      WHEN I.STOR_CD IS NULL 
		                 	  THEN A.CHNL_SEND_CNT 
		                 	  ELSE I.STOR_DSTRB_CUST_CNT END)
					WHEN E.CHNG_CHNL_YN ='Y' AND (F1.VAL10 IS NOT NULL OR F2.VAL10 IS NOT NULL) 
					THEN (CASE WHEN D1.DETECT_SEQ IS NOT NULL
		                      THEN (CASE WHEN D1.CUST_TYPE_CD = 'T' THEN 1 ELSE 0 END)
						      WHEN I.STOR_CD IS NULL 
						      THEN A.CHNL_SEND_CNT 
						      ELSE I.STOR_DSTRB_CUST_CNT END)
					ELSE 0 END																		AS CHNL_SEND_CNT		/* 발송량 */
		     , SUM(CASE WHEN E.CHNG_CHNL_YN IS NULL AND A.CHNL_CD = F.VAL10 
		                THEN (CASE WHEN I.STOR_CD IS NULL 
		                          THEN A.CHNL_SEND_CNT 
		                          ELSE I.STOR_DSTRB_CUST_CNT END)
					    WHEN E.CHNG_CHNL_YN ='Y' AND (F1.VAL10 IS NOT NULL OR F2.VAL10 IS NOT NULL) 
					    THEN (CASE WHEN I.STOR_CD IS NULL 
						          THEN A.CHNL_SEND_CNT 
						          ELSE I.STOR_DSTRB_CUST_CNT END)
					    ELSE 0 END) 
		          OVER(PARTITION BY J.PROMOTION_ID, G.SHOP_CD, D.CHNL_ID ORDER BY CHNL_SEND_DATE) 	AS CHNL_SEND_CNT_OVER_SUM /* 발송 건수 누적합 */
		     , E.CHNL_UNIT_PRICE 																	AS CHNL_UNIT_PRICE  	/* 발송단가 기본료(원) */
		     , CASE WHEN H.DSFRC_CODE = '20' THEN E.CHNL_UNIT_FEE ELSE NULL END 					AS CHNL_UNIT_FEE		/* 발송단가 수수료(원) */
		     , CASE WHEN H.DSFRC_CODE = '20' THEN E.CHNL_UNIT_PRICE_SH ELSE E.CHNL_UNIT_PRICE END 	AS CHNL_UNIT_PRICE_SH 	/* 발송단가 */
		     , J.APRV_DATE
		     , J.PROMOTION_ID
		     , J.PROMOTION_NM
		     , J.RPLAN_GP
		     , J.PROM_TYPE
		     , J.PROM_DESC
		     , J.PROM_SEND_CNT
		  FROM ${jdbc.QuadMaxMart.SchemaName}i_ums_cms_chnl_send_sum A
		       INNER JOIN ${jdbc.QuadMax.SchemaName}z_campaign B
		    ON A.CAMP_ID = B.CAMP_ID
		       INNER JOIN ${jdbc.QuadMax.SchemaName}z_camp_cell C
		    ON A.CAMP_ID = C.CAMP_ID 
		   AND B.CAMP_EXEC_NO = C.CAMP_EXEC_NO
		       INNER JOIN ${jdbc.QuadMax.SchemaName}Z_CHNL_SEND_REQ D
		    ON A.CAMP_ID = D.CAMP_ID
		   AND B.CAMP_EXEC_NO = D.CAMP_EXEC_NO
		   AND A.CHNNL_TYPE_CD = F.LOOKUP_CODE
		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values F1
			ON F1.LOOKUP_TYPE ='CHANNEL_TYPE'
		   AND A.CHNL_CD = F1.VAL10  /*전환채널1*/
		   AND E.CHNG_CHNL_YN = 'Y'
		   AND E1.CHNL_TYPE_CD = F1.LOOKUP_CODE
			   LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values F2
			ON F2.LOOKUP_TYPE ='CHANNEL_TYPE'
		   AND A.CHNL_CD = F2.VAL10  /*전환채널2*/
		   AND E.CHNG_CHNL_YN = 'Y'
		   AND E2.CHNL_TYPE_CD = F2.LOOKUP_CODE
		       INNER JOIN ${jdbc.QuadMax.SchemaName}z_camp_bill_shop G
		    ON A.CAMP_ID = G.CAMP_ID
		       INNER JOIN ${jdbc.QuadMaxMart.SchemaName}i_cdw_cms_cdw_ria_smt100tm H
		    ON G.SHOP_CD = H.STORECD
		       LEFT OUTER JOIN ${jdbc.QuadMaxMart.SchemaName}I_CDW_CMS_TMP_CMP_STOR_CUST_DSTRB I
		    ON a.CAMP_ID = I.CMP_ID 
		   AND G.SHOP_CD = I.STOR_CD
		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}rplan_join K
		    ON G.SHOP_CD = K.STORE_CD
		   AND A.CHNL_SEND_DATE >= K.RPLAN_JOIN_DT
		   AND A.CHNL_SEND_DATE <![CDATA[<=]]> K.RPLAN_END_DT
		       LEFT OUTER JOIN 
		       (SELECT a.PROMOTION_ID
				      , b.promotion_nm
				      , a.STORE_CD
				      , b.RPLAN_ID
				      , e.LOOKUP_NAME AS RPLAN_GP
				      , F.LOOKUP_NAME AS PROM_TYPE
				      , CONCAT(H.PROM_DESC, ' (', b.PROM_DAY_CNT, '일)') AS PROM_DESC
				      , a.APRV_DATE
				      , b.PROM_DAY_CNT
				      , date_format(date_add(str_to_date(a.aprv_date, '%Y%m%d'), INTERVAL b.PROM_DAY_CNT - 1 DAY), '%Y%m%d') AS END_DATE
				      , c.CHNL_ID
				      , c.PROM_SEND_CNT
				   FROM ${jdbc.QuadMax.SchemaName}promotion_req a
						INNER JOIN ${jdbc.QuadMax.SchemaName}promotion_list b
					 ON a.PROMOTION_ID = b.PROMOTION_ID
						INNER JOIN ${jdbc.QuadMax.SchemaName}promotion_chnnl_capacity c
				     ON a.PROMOTION_ID = c.PROMOTION_ID
				        LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}RPLAN_LIST d
				     ON b.RPLAN_ID = d.RPLAN_ID
				        LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}T_LOOKUP_VALUES E
				     ON E.LOOKUP_TYPE = 'FEE_TYPE'
				    AND D.RPLAN_GP_CD = E.LOOKUP_CODE
				        LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}T_LOOKUP_VALUES F
				     ON F.LOOKUP_TYPE = 'PROM_TYPE'
				    AND B.PROM_TYPE = F.LOOKUP_CODE
				        LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}T_CHANNEL G
				     ON C.CHNL_ID = G.CHNL_ID
				        LEFT OUTER JOIN
				        (SELECT A.PROMOTION_ID
						      , GROUP_CONCAT(CONCAT(C.CHNL_NAME), ' ', B.PROM_SEND_CNT, '건' SEPARATOR ', ') AS PROM_DESC
						   FROM ${jdbc.QuadMax.SchemaName}PROMOTION_LIST A
						        INNER JOIN ${jdbc.QuadMax.SchemaName}PROMOTION_CHNNL_CAPACITY B
						     ON A.PROMOTION_ID = B.PROMOTION_ID 
						    AND A.PROM_TYPE = 'CHNL_SEND_FREE'
						        INNER JOIN ${jdbc.QuadMax.SchemaName}T_CHANNEL C
						     ON B.CHNL_ID = C.CHNL_ID 
						  GROUP BY PROMOTION_ID
				        ) H
				     ON A.PROMOTION_ID = H.PROMOTION_ID
				  WHERE 1 = 1
					AND b.prom_TYPE = 'CHNL_SEND_FREE' /* 발송비프로모션 */
					AND a.APRV_STAT_CD IN ('Y', 'CF', 'F') /* 프로모션 승인 완료 */
			   ) J
		    ON G.SHOP_CD = J.STORE_CD
		   AND D.CHNL_ID = J.CHNL_ID
		   AND A.CHNL_SEND_DATE >= J.APRV_DATE
		   AND A.CHNL_SEND_DATE <![CDATA[<=]]> J.END_DATE  
		   AND B.BILL_CHRG_CD = 'SH'
		   AND J.RPLAN_ID = K.RPLAN_ID
		 WHERE 1=1
		   AND A.CHNL_CD <![CDATA[<>]]> 'PUSH' 	/*고정조건 PUSH 제외 - 2023.01.27 추가*/
		   AND ((E.CHNG_CHNL_YN IS NULL AND A.CHNL_CD = F.VAL10) OR E.CHNG_CHNL_YN ='Y' AND (F1.VAL10 IS NOT NULL OR F2.VAL10 IS NOT NULL)) /*고정조건*/     
		       UNION ALL 
		/* 테스트 및 참조발송(이상치 제외) 프로모션 적용 안함 */	
		SELECT A.CHNL_SEND_DATE 												AS CHNL_SEND_DATE  		/* 발송일 */
		     , B.CAMP_ID        												AS CAMP_ID  			/* 캠페인 ID */
		     , B.CAMP_NAME      												AS CAMP_NAME 			/* 캠페인 명 */
		     , B.BRAND_CD      												    AS BRAND_CD 			/* 브랜드명 */
		     , B.REG_DEPT_ID 													AS REG_DEPT_ID
		     , B.REG_EMP_ID     												AS REG_EMP_ID 			/* 담당자 ID */
		     , CASE WHEN E.CHNG_CHNL_YN = 'Y' 
		            THEN (CASE WHEN F1.VAL10 IS NOT NULL 
		                       THEN E1.CHNL_NAME
		     				   ELSE (CASE WHEN F2.VAL10 IS NOT NULL 
		     				              THEN E2.CHNL_NAME END) END)
			 		ELSE E.CHNL_NAME END 										AS CHNL_NAME 			/* 발송채널 ID */
		     , H.DSFRC_CODE 																			/* 직가구분 */
		     , G.SHOP_CD        												AS SHOP_CD 				/* 대상 점포 코드 */
		     , H.STORE_NM       												AS STORE_NM 			/* 대상 점포 명 */
		     , B.BILL_CHRG_CD  										  									/* 비용 부담 부서 */
		     , B.BILL_DEPT_CD  													                  		/* 정산 부서 */
		     , A.CHNL_SEND_CNT 
		     , NULL 															AS CHNL_SEND_CNT_OVER_SUM /* 발송 건수 누적합 */
		     , E.CHNL_UNIT_PRICE 												AS CHNL_UNIT_PRICE  	/* 발송단가 기본료(원) */
		     , CASE WHEN H.DSFRC_CODE = '20' THEN E.CHNL_UNIT_FEE ELSE NULL END AS CHNL_UNIT_FEE		/* 발송단가 수수료(원) */
		     , CASE WHEN H.DSFRC_CODE = '20' THEN E.CHNL_UNIT_PRICE_SH ELSE E.CHNL_UNIT_PRICE END 	AS CHNL_UNIT_PRICE_SH 	/* 발송단가 */
		     , NULL 															AS APRV_DATE
		     , NULL 															AS PROMOTION_ID
		     , NULL 															AS PROMOTION_NM
		     , NULL 															AS RPLAN_GP
		     , NULL 															AS PROM_TYPE
		     , NULL 															AS PROM_DESC
		     , NULL 															AS PROM_SEND_CNT
		  FROM ${jdbc.QuadMaxMart.SchemaName}i_ums_cms_chnl_send_sum A
		       INNER JOIN ${jdbc.QuadMax.SchemaName}t_campaign B
		    ON A.CAMP_ID = B.CAMP_ID
		       INNER JOIN ${jdbc.QuadMax.SchemaName}T_camp_cell C
		    ON A.CAMP_ID = C.CAMP_ID 
		       INNER JOIN ${jdbc.QuadMax.SchemaName}Z_CHNL_SEND_REQ_REF D
		    ON A.CAMP_ID = D.CAMP_ID
		   AND A.CHNL_SEND_REQ = D.REF_SEND_REQ_SEQ
		   AND A.CHNL_SEND_REQ LIKE '%R%'
		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}T_CHANNEL E
		    ON D.CHNL_ID = E.CHNL_ID
		   AND E.DEL_F ='N'
		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_channel E1
			ON E.CHNG_CHNL_YN = 'Y' /*전환채널1*/
		   AND E.CHNL_ID_1 = E1.CHNL_ID
			   LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_channel E2
			ON E.CHNG_CHNL_YN = 'Y' /*전환채널2*/
		   AND E.CHNL_ID_2 = E2.CHNL_ID
		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values F
		    ON F.LOOKUP_TYPE = 'CHANNEL_TYPE'
		   AND E.CHNL_TYPE_CD = F.LOOKUP_CODE
		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values F1
			ON F1.LOOKUP_TYPE ='CHANNEL_TYPE'
		   AND A.CHNL_CD = F1.VAL10  /*전환채널1*/
		   AND E.CHNG_CHNL_YN = 'Y'
		   AND E1.CHNL_TYPE_CD = F1.LOOKUP_CODE
			   LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values F2
			ON F2.LOOKUP_TYPE ='CHANNEL_TYPE'
		   AND A.CHNL_CD = F2.VAL10  /*전환채널2*/
		   AND E.CHNG_CHNL_YN = 'Y'
		   AND E2.CHNL_TYPE_CD = F2.LOOKUP_CODE
		       INNER JOIN ${jdbc.QuadMax.SchemaName}t_camp_bill_shop G
		    ON A.CAMP_ID = G.CAMP_ID
		       INNER JOIN ${jdbc.QuadMaxMart.SchemaName}i_cdw_cms_cdw_ria_smt100tm H
		    ON G.SHOP_CD = H.STORECD
		 WHERE 1=1
		   AND A.CHNL_CD <![CDATA[<>]]> 'PUSH' 	/*고정조건 PUSH 제외 - 2023.01.27 추가*/
                AND S1.ORDER_DATE BETWEEN @@구매기간@@ [AND S3.BRAND_CD IN @@구매브랜드_SSG@@] 
          [AND S1.SHOP_CD IN @@매장_C@@] /*안녕하세요*/ 
          [AND moon in '2']
          [AND moon2 =2]
		   AND ((E.CHNG_CHNL_YN IS NULL AND A.CHNL_CD = F.VAL10) OR E.CHNG_CHNL_YN ='Y' AND (F1.VAL10 IS NOT NULL OR F2.VAL10 IS NOT NULL)) /*고정조건*/
		       UNION ALL 
		/* 테스트 및 참조발송(이상치 ONLY) 프로모션 적용 안함, 없어야 정상 */
		SELECT A.CHNL_SEND_DATE 												AS CHNL_SEND_DATE  		/* 발송일 */
		     , B.CAMP_ID        												AS CAMP_ID  			/* 캠페인 ID */
		     , B.CAMP_NAME      												AS CAMP_NAME 			/* 캠페인 명 */
		     , B.BRAND_CD      												    AS BRAND_CD 			/* 브랜드명 */
		     , B.REG_DEPT_ID 													AS REG_DEPT_ID
		     , B.REG_EMP_ID     												AS REG_EMP_ID 			/* 담당자 ID */
		     , F.CHNL_NAME 														AS CHNL_NAME 			/* 발송채널 ID */
		     , H.DSFRC_CODE 																			/* 직가구분 */
		     , G.SHOP_CD        												AS SHOP_CD 				/* 대상 점포 코드 */
		     , H.STORE_NM       												AS STORE_NM 			/* 대상 점포 명 */
		     , B.BILL_CHRG_CD  										  									/* 비용 부담 부서 */
		     , B.BILL_DEPT_CD  													                  		/* 정산 부서 AND  */
		     , A.CHNL_SEND_CNT 
		     , NULL 															AS CHNL_SEND_CNT_OVER_SUM /* 발송 건수 누적합 */
		     , F.CHNL_UNIT_PRICE 												AS CHNL_UNIT_PRICE  	/* 발송단가 기본료(원) */
		     , CASE WHEN H.DSFRC_CODE = '20' THEN F.CHNL_UNIT_FEE ELSE NULL END AS CHNL_UNIT_FEE		/* 발송단가 수수료(원) */
		     , CASE WHEN H.DSFRC_CODE = '20' THEN F.CHNL_UNIT_PRICE_SH ELSE F.CHNL_UNIT_PRICE END 	AS CHNL_UNIT_PRICE_SH 	/* 발송단가 */
		     , NULL 															AS APRV_DATE
		     , NULL 															AS PROMOTION_ID
		     , NULL 															AS PROMOTION_NM
		     , NULL 															AS RPLAN_GP
		     , NULL 															AS PROM_TYPE
		     , NULL 															AS PROM_DESC
		     , NULL 															AS PROM_SEND_CNT
		  FROM ${jdbc.QuadMaxMart.SchemaName}i_ums_cms_chnl_send_sum A
		       INNER JOIN ${jdbc.QuadMax.SchemaName}t_campaign B
		    ON A.CAMP_ID = B.CAMP_ID
		       INNER JOIN ${jdbc.QuadMax.SchemaName}T_camp_cell C
		    ON A.CAMP_ID = C.CAMP_ID 
		       INNER JOIN ${jdbc.QuadMax.SchemaName}Z_CHNL_SEND_REQ_REF D1
		    ON A.CAMP_ID = D1.CAMP_ID
		   AND A.CHNL_SEND_REQ = D1.REF_SEND_REQ_SEQ
		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}Z_CHNL_SEND_REQ D2
		    ON A.CAMP_ID = D2.CAMP_ID
		   AND A.CHNL_SEND_REQ = D2.CHNL_SEND_REQ
		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}T_LOOKUP_VALUES E
		    ON E.LOOKUP_TYPE = 'CHANNEL_TYPE'
		   AND E.VAL9 IS NULL
		   AND A.CHNL_CD = E.VAL10
		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}T_CHANNEL F
		    ON E.LOOKUP_CODE = F.CHNL_TYPE_CD
		       INNER JOIN ${jdbc.QuadMax.SchemaName}t_camp_bill_shop G
		    ON A.CAMP_ID = G.CAMP_ID
		       INNER JOIN ${jdbc.QuadMaxMart.SchemaName}i_cdw_cms_cdw_ria_smt100tm H
		    ON G.SHOP_CD = H.STORECD
		 WHERE 1=1
		   AND D1.REF_SEND_REQ_SEQ IS NULL /*AND OR HAVING*/
		   AND D2.CHNL_SEND_REQ IS NULL
		   AND A.CHNL_CD <![CDATA[<>]]> 'PUSH' 	/*고정조건 PUSH 제외 - 2023.01.27 추가*/
		 ORDER BY CHNL_SEND_DATE 
		     , CAMP_ID
		     , SHOP_CD
       """

# sql_query="""SELECT TOT.CHNL_SEND_DATE 												AS CHNL_SEND_DATE  					/* 발송일 */
# 	     , TOT.CAMP_ID        												AS CAMP_ID  						/* 캠페인 ID */
# 	     , TOT.CAMP_NAME      												AS CAMP_NAME 						/* 캠페인 명 */
# 	     , ifnull(cd1.BRND_NM, '-')											AS BRAND_NM 						/* 브랜드명 */
# 	     , ifnull(cd2.DEPT_NAME, '-') 										AS REG_DEPT_NAME    				/* 부서명 */
# 	     , TOT.REG_EMP_ID     												AS REG_EMP_ID 						/* 담당자 ID */
# 	     , ifnull(cd3.EMP_NAME, '-')  										AS EMP_NAME 						/* 담당자명 */
# 	     , TOT.CHNL_NAME      												AS CHNL_NAME 						/* 발송 채널 */
# 	     , ifnull(cd4.DRCAFL_SE_NM, '-')									AS DSFRC_NAME						/* 직가구분 */
# 	     , TOT.SHOP_CD        												AS SHOP_CD 							/* 대상 점포 코드 */
# 	     , TOT.STORE_NM       												AS STORE_NM 						/* 대상 점포 명 */
# 	     , ifnull(cd5.LOOKUP_NAME, '-')  									AS BILL_CHRG_DEPT_NAME 				/* 비용 부담 부서 */
# 	     , ifnull(cd6.LOOKUP_NAME, '-')  									AS BILL_DEPT_NAME 					/* 정산 부서 */
# 	     , TOT.CHNL_SEND_CNT												AS CHNL_SEND_CNT					/* 발송 건수(건) */
# 	     , CAST(TOT.CHNL_UNIT_PRICE AS DECIMAL(20,1))						AS CHNL_UNIT_PRICE 					/* 발송단가 기본료(원) (화면) */
# 	     , CAST(TOT.CHNL_UNIT_FEE AS DECIMAL(20,1))							AS CHNL_UNIT_FEE 					/* 발송단가 수수료(원) */
# 	     , CAST(TOT.CHNL_SEND_CNT * TOT.CHNL_UNIT_PRICE AS DECIMAL(20,1))	AS CHNL_SEND_AMT_BASE_BEF_PROM  	/* (프로모션 적용 전) 발송금액 기본료(원) (화면) */
# 	     , CAST(TOT.CHNL_SEND_CNT * TOT.CHNL_UNIT_FEE AS DECIMAL(20,1))		AS CHNL_SEND_AMT_FEE_BEF_PROM   	/* (프로모션 적용 전) 발송금액 수수료(원) */
# 	     , CAST(TOT.CHNL_SEND_CNT * TOT.CHNL_UNIT_PRICE_SH AS DECIMAL(20,1))AS CHNL_SEND_AMT_BEF_PROM 			/* (프로모션 적용 전) 발송금액 (원) */
# 	     , TOT.APRV_DATE													AS PROM_APRV_DATE					/* 프로모션 적용일 */
# 	     , TOT.PROMOTION_ID													AS PROMOTION_ID						/* 프로모션 ID */
# 	     , TOT.PROMOTION_NM													AS PROMOTION_NM						/* 프로모션 명 */
# 	     , TOT.RPLAN_GP														AS RPLAN_GP							/* 대상요금제 */
# 	     , TOT.PROM_TYPE													AS PROM_TYPE						/* 프로모션 종류 */
# 	     , TOT.PROM_DESC													AS PROM_DESC						/* 프로모션 내용 */
# 	     , CASE WHEN TOT.PROM_SEND_CNT > CHNL_SEND_CNT_OVER_SUM 
# 	            THEN TOT.CHNL_SEND_CNT
# 	            ELSE (CASE WHEN TOT.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + TOT.CHNL_SEND_CNT > 0
# 	                      THEN TOT.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + TOT.CHNL_SEND_CNT
# 	                      ELSE 0 END)
# 	            END															AS PROM_APLY_CNT					/* (프로모션 무료) 발송 건수(건) */
#      , CAST((CASE WHEN TOT.PROM_SEND_CNT > CHNL_SEND_CNT_OVER_SUM 
#                        THEN TOT.CHNL_SEND_CNT
#                        ELSE (CASE WHEN TOT.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + TOT.CHNL_SEND_CNT > 0
#                                  THEN TOT.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + TOT.CHNL_SEND_CNT
#                                  ELSE 0 END)
#                         END) * TOT.CHNL_UNIT_PRICE AS DECIMAL(20,1))		AS PROM_APLY_AMT_BASE				/* (프로모션 무료) 발송금액 기본료(원) */
#      , CAST((CASE WHEN TOT.PROM_SEND_CNT > CHNL_SEND_CNT_OVER_SUM 
#                        THEN TOT.CHNL_SEND_CNT
#                        ELSE (CASE WHEN TOT.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + TOT.CHNL_SEND_CNT > 0
#                                  THEN TOT.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + TOT.CHNL_SEND_CNT
#                                  ELSE 0 END)
#                         END)	* TOT.CHNL_UNIT_FEE	AS DECIMAL(20,1))		AS PROM_APLY_AMT_FEE				/* (프로모션 무료) 발송금액 수수료(원) */
#      , CAST((CASE WHEN TOT.PROM_SEND_CNT > CHNL_SEND_CNT_OVER_SUM 
#             	       THEN TOT.CHNL_SEND_CNT
#             	       ELSE (CASE WHEN TOT.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + TOT.CHNL_SEND_CNT > 0
#                       	         THEN TOT.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + TOT.CHNL_SEND_CNT
#                       		     ELSE 0 END)
#             	        END) * TOT.CHNL_UNIT_PRICE_SH AS DECIMAL(20,1))	AS PROM_APLY_AMT					/* (프로모션 무료) 발송금액(원) */
#      , CAST(TOT.CHNL_SEND_CNT - CASE WHEN TOT.PROM_SEND_CNT > CHNL_SEND_CNT_OVER_SUM  THEN TOT.CHNL_SEND_CNT
#             					            										   ELSE (CASE WHEN TOT.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + TOT.CHNL_SEND_CNT > 0 THEN TOT.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + TOT.CHNL_SEND_CNT
# 			                 																																			  ELSE 0 
# 			                 																																			  END)
#             			                     										   END * TOT.CHNL_UNIT_PRICE AS DECIMAL(20,1))		AS CHNL_SEND_AMT_BASE_AFTER_PROM	/* (프로모션 적용 후) 발송금액 기본료(원) */
#      , CAST(TOT.CHNL_SEND_CNT - (CASE WHEN TOT.PROM_SEND_CNT > CHNL_SEND_CNT_OVER_SUM 
#             					            THEN TOT.CHNL_SEND_CNT
#             					            ELSE (CASE WHEN TOT.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + TOT.CHNL_SEND_CNT > 0
#                       					              THEN TOT.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + TOT.CHNL_SEND_CNT
#                       				                  ELSE 0 END)
#             			                     END) * TOT.CHNL_UNIT_FEE  AS DECIMAL(20,1))		AS CHNL_SEND_AMT_FEE_AFTER_PROM		/* (프로모션 적용 후) 발송금액 수수료(원) */
#      , CAST(TOT.CHNL_SEND_CNT - (CASE WHEN TOT.PROM_SEND_CNT > CHNL_SEND_CNT_OVER_SUM 
#             					            THEN TOT.CHNL_SEND_CNT
#             					            ELSE (CASE WHEN TOT.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + TOT.CHNL_SEND_CNT > 0
#                       					              THEN TOT.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + TOT.CHNL_SEND_CNT
#                       				                  ELSE 0 END)
#             			                     END) * TOT.CHNL_UNIT_PRICE_SH AS DECIMAL(20,1))	AS CHNL_SEND_AMT_AFTER_PROM			/* (프로모션 적용 후) 발송금액(원) */
#   FROM (A) TOT
#        INNER JOIN ${jdbc.QuadMaxMart.SchemaName}i_cdw_cms_cdm_d_div cd1
#     ON TOT.BRAND_CD = cd1.DIV_CD
#        LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_emp_dept cd2
#     ON TOT.REG_DEPT_ID = cd2.DEPT_ID
#        LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_emp cd3
#     ON TOT.REG_EMP_ID = cd3.EMP_ID
#        LEFT OUTER JOIN ${jdbc.QuadMaxMart.SchemaName}i_cdw_cms_cdm_d_drcafl_se cd4
#     ON TOT.DSFRC_CODE = cd4.DRCAFL_SE_CD
#        LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values cd5
#     ON TOT.BILL_CHRG_CD = cd5.LOOKUP_CODE
#    AND cd5.LOOKUP_TYPE = 'GRS_BILL_CHRG_CD'
#        LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values cd6
#     ON TOT.BILL_DEPT_CD = cd6.LOOKUP_CODE
#    AND cd6.LOOKUP_TYPE = 'GRS_BILL_DEPT_CD'
#     WHERE 1 = 1
# 	<if test="null != billDeptCd and '' != billDeptCd">
#    AND TOT.BILL_DEPT_CD = #{billDeptCd}	/* 변수 처리 정산 부서 */
# 	</if>
# 	<if test="null != chnlSendDeptIds">
#    AND TOT.REG_DEPT_ID IN <foreach collection="chnlSendDeptIds" item="item" index="index" separator="," open="(" close=")">#{item}</foreach>	/* 변수 처리 발송 부서 */
# 	</if>	
# HAVING SUBSTRING(TOT.CHNL_SEND_DATE, 1, 6) = #{yyyymm} /* 변수 처리 조회월 */
#  ORDER BY TOT.CHNL_SEND_DATE 
#      , TOT.CAMP_ID
#      , TOT.SHOP_CD"""

# sql_query="""SELECT A.CHNL_SEND_DATE AS CHNL_SEND_DATE /* 발송일 */
# 		     , B.CAMP_ID AS CAMP_ID /* 캠페인 ID */
# 		     , B.CAMP_NAME AS CAMP_NAME /* 캠페인 명 */
# 		     , B.BRAND_CD AS BRAND_CD /* 브랜드명 */
# 		     , B.REG_DEPT_ID AS REG_DEPT_ID
# 		     , B.REG_EMP_ID AS REG_EMP_ID /* 담당자 ID */
# 		     , CASE WHEN E.CHNG_CHNL_YN = 'Y' 
# 		            THEN (CASE WHEN F1.VAL10 IS NOT NULL 
# 		                       THEN E1.CHNL_NAME
# ELSE (CASE WHEN F2.VAL10 IS NOT NULL 
# 		     				              THEN E2.CHNL_NAME
# END)
# END)
# ELSE E.CHNL_NAME
# END AS CHNL_NAME /* 발송채널 ID */
# 		     , H.DSFRC_CODE /* 직가구분 */
# 		     , G.SHOP_CD AS SHOP_CD /* 대상 점포 코드 */
# 		     , H.STORE_NM AS STORE_NM /* 대상 점포 명 */
# 		     , B.BILL_CHRG_CD /* 비용 부담 부서 */
# 		     , B.BILL_DEPT_CD /* 정산 부서 */
# 		     , CASE WHEN E.CHNG_CHNL_YN IS NULL
# AND A.CHNL_CD = F.VAL10 
# 		            THEN (CASE WHEN D1.DETECT_SEQ IS NOT NULL
# 		                      THEN (CASE WHEN D1.CUST_TYPE_CD = 'T' THEN 1
# ELSE 0
# END)
# WHEN I.STOR_CD IS NULL 
# 		                 	  THEN A.CHNL_SEND_CNT
# ELSE I.STOR_DSTRB_CUST_CNT
# END)
# WHEN E.CHNG_CHNL_YN = 'Y'
# AND (F1.VAL10 IS NOT NULL
# OR F2.VAL10 IS NOT NULL) 
# 					THEN (CASE WHEN D1.DETECT_SEQ IS NOT NULL
# 		                      THEN (CASE WHEN D1.CUST_TYPE_CD = 'T' THEN 1
# ELSE 0
# END)
# WHEN I.STOR_CD IS NULL 
# 						      THEN A.CHNL_SEND_CNT
# ELSE I.STOR_DSTRB_CUST_CNT
# END)
# ELSE 0
# END AS CHNL_SEND_CNT /* 발송량 */
# 		     , SUM(CASE WHEN E.CHNG_CHNL_YN IS NULL AND A.CHNL_CD = F.VAL10 
# 		                THEN (CASE WHEN I.STOR_CD IS NULL 
# 		                          THEN A.CHNL_SEND_CNT 
# 		                          ELSE I.STOR_DSTRB_CUST_CNT END)
# 					    WHEN E.CHNG_CHNL_YN = 'Y' AND (F1.VAL10 IS NOT NULL OR F2.VAL10 IS NOT NULL) 
# 					    THEN (CASE WHEN I.STOR_CD IS NULL 
# 						          THEN A.CHNL_SEND_CNT 
# 						          ELSE I.STOR_DSTRB_CUST_CNT END)
# 					    ELSE 0 END) 
# 		          OVER(PARTITION BY J.PROMOTION_ID, G.SHOP_CD, D.CHNL_ID
# ORDER BY CHNL_SEND_DATE) AS CHNL_SEND_CNT_OVER_SUM /* 발송 건수 누적합 */
# 		     , E.CHNL_UNIT_PRICE AS CHNL_UNIT_PRICE /* 발송단가 기본료(원) */
# 		     , CASE WHEN H.DSFRC_CODE = '20' THEN E.CHNL_UNIT_FEE
# ELSE NULL
# END AS CHNL_UNIT_FEE /* 발송단가 수수료(원) */
# 		     , CASE WHEN H.DSFRC_CODE = '20' THEN E.CHNL_UNIT_PRICE_SH
# ELSE E.CHNL_UNIT_PRICE
# END AS CHNL_UNIT_PRICE_SH /* 발송단가 */
# 		     , J.APRV_DATE
# 		     , J.PROMOTION_ID
# 		     , J.PROMOTION_NM
# 		     , J.RPLAN_GP
# 		     , J.PROM_TYPE
# 		     , J.PROM_DESC
# 		     , J.PROM_SEND_CNT
# FROM(table) A
# INNER JOIN ${jdbc.QuadMax.SchemaName}z_campaign B
# 		    ON
# A.CAMP_ID = B.CAMP_ID
# INNER JOIN ${jdbc.QuadMax.SchemaName}z_camp_cell C
# 		    ON
# A.CAMP_ID = C.CAMP_ID
# AND B.CAMP_EXEC_NO = C.CAMP_EXEC_NO
# INNER JOIN ${jdbc.QuadMax.SchemaName}Z_CHNL_SEND_REQ D
# 		    ON
# A.CAMP_ID = D.CAMP_ID
# AND B.CAMP_EXEC_NO = D.CAMP_EXEC_NO
# AND A.CHNL_SEND_REQ = D.CHNL_SEND_REQ
# LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}Z_EBM_SEND_CHANNEL_CUST D1 /* 실시간 발송의 경우 -> Z_EBM_SEND_CHANNEL_CUST 에서 참조 */
# 		    ON
# B.CAMP_BASE_TYPE = 'EBM'
# AND A.CHNL_SEND_REQ = D1.DETECT_SEQ
# LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}T_CHANNEL E
# 		    ON
# IFNULL(D1.CHNL_ID, D.CHNL_ID) = E.CHNL_ID
# AND E.DEL_F = 'N'
# LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_channel E1
# 			ON
# E.CHNG_CHNL_YN = 'Y' /* 전환채널1 */
# AND E.CHNL_ID_1 = E1.CHNL_ID
# LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_channel E2
# 			ON
# E.CHNG_CHNL_YN = 'Y' /* 전환채널2 */
# AND E.CHNL_ID_2 = E2.CHNL_ID
# LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values F
# 		    ON
# F.LOOKUP_TYPE = 'CHANNEL_TYPE'
# AND E.CHNL_TYPE_CD = F.LOOKUP_CODE
# LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values F1
# 			ON
# F1.LOOKUP_TYPE = 'CHANNEL_TYPE'
# AND A.CHNL_CD = F1.VAL10 /* 전환채널1 */
# AND E.CHNG_CHNL_YN = 'Y'
# AND E1.CHNL_TYPE_CD = F1.LOOKUP_CODE
# LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values F2
# 			ON
# F2.LOOKUP_TYPE = 'CHANNEL_TYPE'
# AND A.CHNL_CD = F2.VAL10 /* 전환채널2 */
# AND E.CHNG_CHNL_YN = 'Y'
# AND E2.CHNL_TYPE_CD = F2.LOOKUP_CODE
# INNER JOIN ${jdbc.QuadMax.SchemaName}z_camp_bill_shop G
# 		    ON
# A.CAMP_ID = G.CAMP_ID
# INNER JOIN ${jdbc.QuadMaxMart.SchemaName}i_cdw_cms_cdw_ria_smt100tm H
# 		    ON
# G.SHOP_CD = H.STORECD
# LEFT OUTER JOIN ${jdbc.QuadMaxMart.SchemaName}I_CDW_CMS_TMP_CMP_STOR_CUST_DSTRB I
# 		    ON
# a.CAMP_ID = I.CMP_ID
# AND G.SHOP_CD = I.STOR_CD
# LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}rplan_join K
# 		    ON
# G.SHOP_CD = K.STORE_CD
# AND A.CHNL_SEND_DATE >= K.RPLAN_JOIN_DT
# AND A.CHNL_SEND_DATE <![CDATA[<=]]> K.RPLAN_END_DT
# LEFT OUTER JOIN 
# 		       (SELECT a.PROMOTION_ID
# 				      , b.promotion_nm
# 				      , a.STORE_CD
# 				      , b.RPLAN_ID
# 				      , e.LOOKUP_NAME AS RPLAN_GP
# 				      , F.LOOKUP_NAME AS PROM_TYPE
# 				      , CONCAT(H.PROM_DESC, ' (', b.PROM_DAY_CNT, '일)') AS PROM_DESC
# 				      , a.APRV_DATE
# 				      , b.PROM_DAY_CNT
# 				      , date_format(date_add(str_to_date(a.aprv_date, '%Y%m%d'), INTERVAL b.PROM_DAY_CNT - 1 DAY), '%Y%m%d') AS END_DATE
# 				      , c.CHNL_ID
# 				      , c.PROM_SEND_CNT
# FROM ${jdbc.QuadMax.SchemaName}promotion_req a
# INNER JOIN ${jdbc.QuadMax.SchemaName}promotion_list b
# 					 ON
# a.PROMOTION_ID = b.PROMOTION_ID
# INNER JOIN ${jdbc.QuadMax.SchemaName}promotion_chnnl_capacity c
# 				     ON
# a.PROMOTION_ID = c.PROMOTION_ID
# LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}RPLAN_LIST d
# 				     ON
# b.RPLAN_ID = d.RPLAN_ID
# LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}T_LOOKUP_VALUES E
# 				     ON
# E.LOOKUP_TYPE = 'FEE_TYPE'
# AND D.RPLAN_GP_CD = E.LOOKUP_CODE
# LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}T_LOOKUP_VALUES F
# 				     ON
# F.LOOKUP_TYPE = 'PROM_TYPE'
# AND B.PROM_TYPE = F.LOOKUP_CODE
# LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}T_CHANNEL G
# 				     ON
# C.CHNL_ID = G.CHNL_ID
# LEFT OUTER JOIN
# 				        (SELECT A.PROMOTION_ID
# 						      , GROUP_CONCAT(CONCAT(C.CHNL_NAME), ' ', B.PROM_SEND_CNT, '건' SEPARATOR ', ') AS PROM_DESC
# FROM ${jdbc.QuadMax.SchemaName}PROMOTION_LIST A
# INNER JOIN ${jdbc.QuadMax.SchemaName}PROMOTION_CHNNL_CAPACITY B
# 						     ON
# A.PROMOTION_ID = B.PROMOTION_ID
# AND A.PROM_TYPE = 'CHNL_SEND_FREE'
# INNER JOIN ${jdbc.QuadMax.SchemaName}T_CHANNEL C
# 						     ON
# B.CHNL_ID = C.CHNL_ID
# GROUP BY PROMOTION_ID
# 				        ) H
# 				     ON
# A.PROMOTION_ID = H.PROMOTION_ID
# WHERE 1 = 1
# AND b.prom_TYPE = 'CHNL_SEND_FREE' /* 발송비프로모션 */
# AND a.APRV_STAT_CD IN ('Y', 'CF', 'F') /* 프로모션 승인 완료 */
# 			   ) J
# 		    ON
# G.SHOP_CD = J.STORE_CD
# AND D.CHNL_ID = J.CHNL_ID
# AND A.CHNL_SEND_DATE >= J.APRV_DATE
# AND A.CHNL_SEND_DATE <![CDATA[<=]]> J.END_DATE
# AND B.BILL_CHRG_CD = 'SH'
# AND J.RPLAN_ID = K.RPLAN_ID
# WHERE 1 = 1
# AND A.CHNL_CD <![CDATA[<>]]> 'PUSH' /* 고정조건 PUSH 제외 - 2023.01.27 추가 */
# AND ((E.CHNG_CHNL_YN IS NULL
# AND A.CHNL_CD = F.VAL10)
# OR E.CHNG_CHNL_YN = 'Y'
# AND (F1.VAL10 IS NOT NULL
# OR F2.VAL10 IS NOT NULL)) /* 고정조건 */
# UNION ALL
# 		/* 테스트 및 참조발송(이상치 제외) 프로모션 적용 안함 */	
# 		SELECT A.CHNL_SEND_DATE AS CHNL_SEND_DATE /* 발송일 */
# 		     , B.CAMP_ID AS CAMP_ID /* 캠페인 ID */
# 		     , B.CAMP_NAME AS CAMP_NAME /* 캠페인 명 */
# 		     , B.BRAND_CD AS BRAND_CD /* 브랜드명 */
# 		     , B.REG_DEPT_ID AS REG_DEPT_ID
# 		     , B.REG_EMP_ID AS REG_EMP_ID /* 담당자 ID */
# 		     , CASE WHEN E.CHNG_CHNL_YN = 'Y' 
# 		            THEN (CASE WHEN F1.VAL10 IS NOT NULL 
# 		                       THEN E1.CHNL_NAME
# ELSE (CASE WHEN F2.VAL10 IS NOT NULL 
# 		     				              THEN E2.CHNL_NAME
# END)
# END)
# ELSE E.CHNL_NAME
# END AS CHNL_NAME /* 발송채널 ID */
# 		     , H.DSFRC_CODE /* 직가구분 */
# 		     , G.SHOP_CD AS SHOP_CD /* 대상 점포 코드 */
# 		     , H.STORE_NM AS STORE_NM /* 대상 점포 명 */
# 		     , B.BILL_CHRG_CD /* 비용 부담 부서 */
# 		     , B.BILL_DEPT_CD /* 정산 부서 */
# 		     , A.CHNL_SEND_CNT 
# 		     , NULL AS CHNL_SEND_CNT_OVER_SUM /* 발송 건수 누적합 */
# 		     , E.CHNL_UNIT_PRICE AS CHNL_UNIT_PRICE /* 발송단가 기본료(원) */
# 		     , CASE WHEN H.DSFRC_CODE = '20' THEN E.CHNL_UNIT_FEE
# ELSE NULL
# END AS CHNL_UNIT_FEE /* 발송단가 수수료(원) */
# 		     , CASE WHEN H.DSFRC_CODE = '20' THEN E.CHNL_UNIT_PRICE_SH
# ELSE E.CHNL_UNIT_PRICE
# END AS CHNL_UNIT_PRICE_SH /* 발송단가 */
# 		     , NULL AS APRV_DATE
# 		     , NULL AS PROMOTION_ID
# 		     , NULL AS PROMOTION_NM
# 		     , NULL AS RPLAN_GP
# 		     , NULL AS PROM_TYPE
# 		     , NULL AS PROM_DESC
# 		     , NULL AS PROM_SEND_CNT
# FROM ${jdbc.QuadMaxMart.SchemaName}i_ums_cms_chnl_send_sum A
# INNER JOIN ${jdbc.QuadMax.SchemaName}t_campaign B
# 		    ON
# A.CAMP_ID = B.CAMP_ID
# INNER JOIN ${jdbc.QuadMax.SchemaName}T_camp_cell C
# 		    ON
# A.CAMP_ID = C.CAMP_ID
# INNER JOIN ${jdbc.QuadMax.SchemaName}Z_CHNL_SEND_REQ_REF D
# 		    ON
# A.CAMP_ID = D.CAMP_ID
# AND A.CHNL_SEND_REQ = D.REF_SEND_REQ_SEQ
# AND A.CHNL_SEND_REQ LIKE '%R%'
# LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}T_CHANNEL E
# 		    ON
# D.CHNL_ID = E.CHNL_ID
# AND E.DEL_F = 'N'
# LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_channel E1
# 			ON
# E.CHNG_CHNL_YN = 'Y' /* 전환채널1 */
# AND E.CHNL_ID_1 = E1.CHNL_ID
# LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_channel E2
# 			ON
# E.CHNG_CHNL_YN = 'Y' /* 전환채널2 */
# AND E.CHNL_ID_2 = E2.CHNL_ID
# LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values F
# 		    ON
# F.LOOKUP_TYPE = 'CHANNEL_TYPE'
# AND E.CHNL_TYPE_CD = F.LOOKUP_CODE
# LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values F1
# 			ON
# F1.LOOKUP_TYPE = 'CHANNEL_TYPE'
# AND A.CHNL_CD = F1.VAL10 /* 전환채널1 */
# AND E.CHNG_CHNL_YN = 'Y'
# AND E1.CHNL_TYPE_CD = F1.LOOKUP_CODE
# LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values F2
# 			ON
# F2.LOOKUP_TYPE = 'CHANNEL_TYPE'
# AND A.CHNL_CD = F2.VAL10 /* 전환채널2 */
# AND E.CHNG_CHNL_YN = 'Y'
# AND E2.CHNL_TYPE_CD = F2.LOOKUP_CODE
# INNER JOIN ${jdbc.QuadMax.SchemaName}t_camp_bill_shop G
# 		    ON
# A.CAMP_ID = G.CAMP_ID
# INNER JOIN ${jdbc.QuadMaxMart.SchemaName}i_cdw_cms_cdw_ria_smt100tm H
# 		    ON
# G.SHOP_CD = H.STORECD
# WHERE 1 = 1
# AND A.CHNL_CD <![CDATA[<>]]> 'PUSH' /* 고정조건 PUSH 제외 - 2023.01.27 추가 */
# AND ((E.CHNG_CHNL_YN IS NULL
# AND A.CHNL_CD = F.VAL10)
# OR E.CHNG_CHNL_YN = 'Y'
# AND (F1.VAL10 IS NOT NULL
# OR F2.VAL10 IS NOT NULL)) /* 고정조건 */
# UNION ALL 
# 		/* 테스트 및 참조발송(이상치 ONLY) 프로모션 적용 안함, 없어야 정상 */
# 		SELECT A.CHNL_SEND_DATE AS CHNL_SEND_DATE /* 발송일 */
# 		     , B.CAMP_ID AS CAMP_ID /* 캠페인 ID */
# 		     , B.CAMP_NAME AS CAMP_NAME /* 캠페인 명 */
# 		     , B.BRAND_CD AS BRAND_CD /* 브랜드명 */
# 		     , B.REG_DEPT_ID AS REG_DEPT_ID
# 		     , B.REG_EMP_ID AS REG_EMP_ID /* 담당자 ID */
# 		     , F.CHNL_NAME AS CHNL_NAME /* 발송채널 ID */
# 		     , H.DSFRC_CODE /* 직가구분 */
# 		     , G.SHOP_CD AS SHOP_CD /* 대상 점포 코드 */
# 		     , H.STORE_NM AS STORE_NM /* 대상 점포 명 */
# 		     , B.BILL_CHRG_CD /* 비용 부담 부서 */
# 		     , B.BILL_DEPT_CD /* 정산 부서 */
# 		     , A.CHNL_SEND_CNT 
# 		     , NULL AS CHNL_SEND_CNT_OVER_SUM /* 발송 건수 누적합 */
# 		     , F.CHNL_UNIT_PRICE AS CHNL_UNIT_PRICE /* 발송단가 기본료(원) */
# 		     , CASE WHEN H.DSFRC_CODE = '20' THEN F.CHNL_UNIT_FEE
# ELSE NULL
# END AS CHNL_UNIT_FEE /* 발송단가 수수료(원) */
# 		     , CASE WHEN H.DSFRC_CODE = '20' THEN F.CHNL_UNIT_PRICE_SH
# ELSE F.CHNL_UNIT_PRICE
# END AS CHNL_UNIT_PRICE_SH /* 발송단가 */
# 		     , NULL AS APRV_DATE
# 		     , NULL AS PROMOTION_ID
# 		     , NULL AS PROMOTION_NM
# 		     , NULL AS RPLAN_GP
# 		     , NULL AS PROM_TYPE
# 		     , NULL AS PROM_DESC
# 		     , NULL AS PROM_SEND_CNT
# FROM ${jdbc.QuadMaxMart.SchemaName}i_ums_cms_chnl_send_sum A
# INNER JOIN ${jdbc.QuadMax.SchemaName}t_campaign B
# 		    ON
# A.CAMP_ID = B.CAMP_ID
# INNER JOIN ${jdbc.QuadMax.SchemaName}T_camp_cell C
# 		    ON
# A.CAMP_ID = C.CAMP_ID
# INNER JOIN ${jdbc.QuadMax.SchemaName}Z_CHNL_SEND_REQ_REF D1
# 		    ON
# A.CAMP_ID = D1.CAMP_ID
# AND A.CHNL_SEND_REQ = D1.REF_SEND_REQ_SEQ
# LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}Z_CHNL_SEND_REQ D2
# 		    ON
# A.CAMP_ID = D2.CAMP_ID
# AND A.CHNL_SEND_REQ = D2.CHNL_SEND_REQ
# LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}T_LOOKUP_VALUES E
# 		    ON
# E.LOOKUP_TYPE = 'CHANNEL_TYPE'
# AND E.VAL9 IS NULL
# AND A.CHNL_CD = E.VAL10
# LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}T_CHANNEL F
# 		    ON
# E.LOOKUP_CODE = F.CHNL_TYPE_CD
# INNER JOIN ${jdbc.QuadMax.SchemaName}t_camp_bill_shop G
# 		    ON
# A.CAMP_ID = G.CAMP_ID
# INNER JOIN ${jdbc.QuadMaxMart.SchemaName}i_cdw_cms_cdw_ria_smt100tm H
# 		    ON
# G.SHOP_CD = H.STORECD
# WHERE 1 = 1
# AND D1.REF_SEND_REQ_SEQ IS NULL
# AND D2.CHNL_SEND_REQ IS NULL
# AND A.CHNL_CD <![CDATA[<>]]> 'PUSH' /* 고정조건 PUSH 제외 - 2023.01.27 추가 */
# ORDER BY CHNL_SEND_DATE 
# 		     , CAMP_ID
# 		     , SHOP_CD


# # """

# sql_query="""SELECT A.CHNL_SEND_DATE 																	AS CHNL_SEND_DATE  		/* 발송일 */
# 		     , A.CHNL_SEND_YM 																		AS CHNL_SEND_YM  		/* 발송 년월 */
# 		     , B.CAMP_ID        																	AS CAMP_ID  			/* 캠페인 ID */
# 		     , B.CAMP_NAME      																	AS CAMP_NAME 			/* 캠페인 명 */
# 		     , B.BRAND_CD      												    					AS BRAND_CD 			/* 브랜드명 */
# 		     , B.REG_DEPT_ID 																		AS REG_DEPT_ID
# 		     , B.REG_EMP_ID     																	AS REG_EMP_ID 			/* 담당자 ID */
# 		     , CASE WHEN E.CHNG_CHNL_YN = 'Y' 
# 		            THEN (CASE WHEN F1.VAL10 IS NOT NULL 
# 		                       THEN E1.CHNL_NAME
# 		     				   ELSE (CASE WHEN F2.VAL10 IS NOT NULL 
# 		     				              THEN E2.CHNL_NAME END) END)
# 			 		ELSE E.CHNL_NAME END 															AS CHNL_NAME 			/* 발송채널 */
# 		     , H.DSFRC_CD 																									/* 직가구분 */
# 		     , G.SHOP_CD        																	AS SHOP_CD 				/* 대상 점포 코드 */
# 		     , H.DEPT_NAME       																	AS STORE_NM 			/* 대상 점포 명 */
# 		     , B.BILL_CHRG_CD  										  														/* 비용 부담 부서 */
# 		     , B.BILL_DEPT_CD  													                  							/* 정산 부서 */
# 		     , CASE WHEN E.CHNG_CHNL_YN IS NULL AND A.CHNL_CD = F.VAL10 
# 		            THEN (CASE WHEN D1.DETECT_SEQ IS NOT NULL
# 		                      THEN (CASE WHEN D1.CUST_TYPE_CD = 'T' THEN 1 ELSE 0 END)
# 		                      WHEN I.STOR_CD IS NULL 
# 		                 	  THEN A.CHNL_SEND_CNT 
# 		                 	  ELSE I.STOR_DSTRB_CUST_CNT END)
# 					WHEN E.CHNG_CHNL_YN ='Y' AND (F1.VAL10 IS NOT NULL OR F2.VAL10 IS NOT NULL) 
# 					THEN (CASE WHEN D1.DETECT_SEQ IS NOT NULL
# 		                      THEN (CASE WHEN D1.CUST_TYPE_CD = 'T' THEN 1 ELSE 0 END)
# 						      WHEN I.STOR_CD IS NULL 
# 						      THEN A.CHNL_SEND_CNT 
# 						      ELSE I.STOR_DSTRB_CUST_CNT END)
# 					ELSE 0 END																		AS CHNL_SEND_CNT		/* 발송량 */
# 		     , SUM(CASE WHEN E.CHNG_CHNL_YN IS NULL AND A.CHNL_CD = F.VAL10 
# 		                THEN (CASE WHEN I.STOR_CD IS NULL 
# 		                          THEN A.CHNL_SEND_CNT 
# 		                          ELSE I.STOR_DSTRB_CUST_CNT END)
# 					    WHEN E.CHNG_CHNL_YN ='Y' AND (F1.VAL10 IS NOT NULL OR F2.VAL10 IS NOT NULL) 
# 					    THEN (CASE WHEN I.STOR_CD IS NULL 
# 						          THEN A.CHNL_SEND_CNT 
# 						          ELSE I.STOR_DSTRB_CUST_CNT END)
# 					    ELSE 0 END) 
# 		          OVER(PARTITION BY J.PROMOTION_ID, G.SHOP_CD, D.CHNL_ID ORDER BY CHNL_SEND_DATE) 	AS CHNL_SEND_CNT_OVER_SUM /* 발송 건수 누적합 */
# 		     , E.CHNL_UNIT_PRICE 																	AS CHNL_UNIT_PRICE  	/* 발송단가 기본료(원) */
# 		     , CASE WHEN H.DSFRC_CD = '20' THEN E.CHNL_UNIT_FEE ELSE NULL END 					AS CHNL_UNIT_FEE		/* 발송단가 수수료(원) */
# 		     , CASE WHEN H.DSFRC_CD = '20' THEN E.CHNL_UNIT_PRICE_SH ELSE E.CHNL_UNIT_PRICE END 	AS CHNL_UNIT_PRICE_SH 	/* 발송단가 */
# 		     , J.APRV_DATE
# 		     , J.PROMOTION_ID
# 		     , J.PROMOTION_NM
# 		     , J.RPLAN_GP
# 		     , J.PROM_TYPE
# 		     , J.PROM_CHNL_NAME
# 		     , J.PROM_DESC
# 		     , J.PROM_SEND_CNT
# 		  FROM ${jdbc.QuadMaxMart.SchemaName}i_ums_cms_chnl_send_sum A
# 		       INNER JOIN ${jdbc.QuadMax.SchemaName}z_campaign B
# 		    ON A.CAMP_ID = B.CAMP_ID
# 		       INNER JOIN ${jdbc.QuadMax.SchemaName}z_camp_cell C
# 		    ON A.CAMP_ID = C.CAMP_ID 
# 		   AND B.CAMP_EXEC_NO = C.CAMP_EXEC_NO
# 		       INNER JOIN ${jdbc.QuadMax.SchemaName}Z_CHNL_SEND_REQ D
# 		    ON A.CAMP_ID = D.CAMP_ID
# 		   AND B.CAMP_EXEC_NO = D.CAMP_EXEC_NO
# 		   AND A.CHNL_SEND_REQ = D.CHNL_SEND_REQ 
# 		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}Z_EBM_SEND_CHANNEL_CUST D1							/* 실시간 발송의 경우 -> Z_EBM_SEND_CHANNEL_CUST 에서 참조 */
# 		    ON B.CAMP_BASE_TYPE = 'EBM'
# 		   AND A.CHNL_SEND_REQ = D1.DETECT_SEQ
# 		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}T_CHANNEL E
# 		    ON IFNULL(D1.CHNL_ID, D.CHNL_ID) = E.CHNL_ID
# 		   AND E.DEL_F ='N'
# 		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_channel E1
# 			ON E.CHNG_CHNL_YN = 'Y' /*전환채널1*/
# 		   AND E.CHNL_ID_1 = E1.CHNL_ID
# 			   LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_channel E2
# 			ON E.CHNG_CHNL_YN = 'Y' /*전환채널2*/
# 		   AND E.CHNL_ID_2 = E2.CHNL_ID
# 		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values F
# 		    ON F.LOOKUP_TYPE = 'CHANNEL_TYPE'
# 		   AND E.CHNL_TYPE_CD = F.LOOKUP_CODE
# 		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values F1
# 			ON F1.LOOKUP_TYPE ='CHANNEL_TYPE'
# 		   AND A.CHNL_CD = F1.VAL10  /*전환채널1*/
# 		   AND E.CHNG_CHNL_YN = 'Y'
# 		   AND E1.CHNL_TYPE_CD = F1.LOOKUP_CODE
# 			   LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values F2
# 			ON F2.LOOKUP_TYPE ='CHANNEL_TYPE'
# 		   AND A.CHNL_CD = F2.VAL10  /*전환채널2*/
# 		   AND E.CHNG_CHNL_YN = 'Y'
# 		   AND E2.CHNL_TYPE_CD = F2.LOOKUP_CODE
# 		       INNER JOIN ${jdbc.QuadMax.SchemaName}z_camp_bill_shop G
# 		    ON A.CAMP_ID = G.CAMP_ID
# 		       INNER JOIN ${jdbc.QuadMax.SchemaName}t_emp_dept H
# 		    ON G.SHOP_CD = H.DEPT_ID
# 		       LEFT OUTER JOIN ${jdbc.QuadMaxMart.SchemaName}I_CDW_CMS_TMP_CMP_STOR_CUST_DSTRB I
# 		    ON a.CAMP_ID = I.CMP_ID 
# 		   AND G.SHOP_CD = I.STOR_CD
# 		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}rplan_join K
# 		    ON G.SHOP_CD = K.STORE_CD
# 		   AND A.CHNL_SEND_DATE >= K.RPLAN_JOIN_DT
# 		   AND A.CHNL_SEND_DATE <![CDATA[<=]]> K.RPLAN_END_DT
# 		       LEFT OUTER JOIN 
# 		       (SELECT a.PROMOTION_ID
# 				      , b.promotion_nm
# 				      , a.STORE_CD
# 				      , b.RPLAN_ID
# 				      , d.RPLAN_NM AS RPLAN_GP
# 				      , F.LOOKUP_NAME AS PROM_TYPE
# 				      , CONCAT(b.PROM_DAY_CNT, '일 ', c.PROM_SEND_CNT, '건 무료') AS PROM_DESC
# 				      , a.APRV_DATE
# 				      , b.PROM_DAY_CNT
# 				      , date_format(date_add(str_to_date(a.aprv_date, '%Y%m%d'), INTERVAL b.PROM_DAY_CNT - 1 DAY), '%Y%m%d') AS END_DATE
# 				      , c.CHNL_ID
# 				      , c.PROM_SEND_CNT
# 				      , G.CHNL_NAME		AS PROM_CHNL_NAME
# 				   FROM ${jdbc.QuadMax.SchemaName}promotion_req a
# 						INNER JOIN ${jdbc.QuadMax.SchemaName}promotion_list b
# 					 ON a.PROMOTION_ID = b.PROMOTION_ID
# 						INNER JOIN ${jdbc.QuadMax.SchemaName}promotion_chnnl_capacity c
# 				     ON a.PROMOTION_ID = c.PROMOTION_ID
# 				        LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}RPLAN_LIST d
# 				     ON b.RPLAN_ID = d.RPLAN_ID
# 				        LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}T_LOOKUP_VALUES F
# 				     ON F.LOOKUP_TYPE = 'PROM_TYPE'
# 				    AND B.PROM_TYPE = F.LOOKUP_CODE
# 				        LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}T_CHANNEL G
# 				     ON C.CHNL_ID = G.CHNL_ID
# 				  WHERE 1 = 1
# 					AND b.prom_TYPE = 'CHNL_SEND_FREE' /* 발송비프로모션 */
# 					AND a.APRV_STAT_CD IN ('Y', 'CF', 'F') /* 프로모션 승인 완료 */
# 			   ) J
# 		    ON G.SHOP_CD = J.STORE_CD
# 		   AND D.CHNL_ID = J.CHNL_ID
# 		   AND A.CHNL_SEND_DATE >= J.APRV_DATE
# 		   AND A.CHNL_SEND_DATE <![CDATA[<=]]> J.END_DATE  
# 		   AND B.BILL_CHRG_CD = 'SH'
# 		   AND J.RPLAN_ID = K.RPLAN_ID
# 		 WHERE 1=1
# 		   AND (B.BILL_CHRG_CD = 'SH' AND H.DSFRC_CD = '20') /* 가맹점에 한해 정산 */
# 		   AND A.CHNL_CD <![CDATA[<>]]> 'PUSH' 	/*고정조건 PUSH 제외 - 2023.01.27 추가*/
# 		   AND ((E.CHNG_CHNL_YN IS NULL AND A.CHNL_CD = F.VAL10) OR E.CHNG_CHNL_YN ='Y' AND (F1.VAL10 IS NOT NULL OR F2.VAL10 IS NOT NULL)) /*고정조건*/
# 		   AND a.BILL_DEPT_CD = #{billDeptCd}	/* 변수 처리 정산 부서 */"""



# sql_query = """/*예시 설명 부분 추가*/ WITH SH_BILL_INFO 
#     AS  ( 
#     /*zz*/ SELECT A.CHNL_SEND_DATE 																	AS CHNL_SEND_DATE  		/* 발송일 */
# 		     , A.CHNL_SEND_YM 																		AS CHNL_SEND_YM  		/* 발송 년월 */
# 		     , B.CAMP_ID        																	AS CAMP_ID  			/* 캠페인 ID */
# 		     , B.CAMP_NAME      																	AS CAMP_NAME 			/* 캠페인 명 */
# 		     , B.BRAND_CD      												    					AS BRAND_CD 			/* 브랜드명 */
# 		     , B.REG_DEPT_ID 																		AS REG_DEPT_ID
# 		     , B.REG_EMP_ID     																	AS REG_EMP_ID 			/* 담당자 ID */
# 		     , CASE WHEN E.CHNG_CHNL_YN = 'Y' 
# 		            THEN (CASE WHEN F1.VAL10 IS NOT NULL 
# 		                       THEN E1.CHNL_NAME
# 		     				   ELSE (CASE WHEN F2.VAL10 IS NOT NULL 
# 		     				              THEN E2.CHNL_NAME END) END)
# 			 		ELSE E.CHNL_NAME END 															AS CHNL_NAME 			/* 발송채널 */
# 		     , H.DSFRC_CD 																									/* 직가구분 */
# 		     , G.SHOP_CD        																	AS SHOP_CD 				/* 대상 점포 코드 */
# 		     , H.DEPT_NAME       																	AS STORE_NM 			/* 대상 점포 명 */
# 		     , B.BILL_CHRG_CD  										  														/* 비용 부담 부서 */
# 		     , B.BILL_DEPT_CD  													                  							/* 정산 부서 */
# 		     , CASE WHEN E.CHNG_CHNL_YN IS NULL AND A.CHNL_CD = F.VAL10 
# 		            THEN (CASE WHEN D1.DETECT_SEQ IS NOT NULL
# 		                      THEN (CASE WHEN D1.CUST_TYPE_CD = 'T' THEN 1 ELSE 0 END)
# 		                      WHEN I.STOR_CD IS NULL 
# 		                 	  THEN A.CHNL_SEND_CNT 
# 		                 	  ELSE I.STOR_DSTRB_CUST_CNT END)
# 					WHEN E.CHNG_CHNL_YN ='Y' AND (F1.VAL10 IS NOT NULL OR F2.VAL10 IS NOT NULL) 
# 					THEN (CASE WHEN D1.DETECT_SEQ IS NOT NULL
# 		                      THEN (CASE WHEN D1.CUST_TYPE_CD = 'T' THEN 1 ELSE 0 END)
# 						      WHEN I.STOR_CD IS NULL 
# 						      THEN A.CHNL_SEND_CNT 
# 						      ELSE I.STOR_DSTRB_CUST_CNT END)
# 					ELSE 0 END																		AS CHNL_SEND_CNT		/* 발송량 */
# 		     , SUM(CASE WHEN E.CHNG_CHNL_YN IS NULL AND A.CHNL_CD = F.VAL10 
# 		                THEN (CASE WHEN I.STOR_CD IS NULL 
# 		                          THEN A.CHNL_SEND_CNT 
# 		                          ELSE I.STOR_DSTRB_CUST_CNT END)
# 					    WHEN E.CHNG_CHNL_YN ='Y' AND (F1.VAL10 IS NOT NULL OR F2.VAL10 IS NOT NULL) 
# 					    THEN (CASE WHEN I.STOR_CD IS NULL 
# 						          THEN A.CHNL_SEND_CNT 
# 						          ELSE I.STOR_DSTRB_CUST_CNT END)
# 					    ELSE 0 END) 
# 		          OVER(PARTITION BY J.PROMOTION_ID, G.SHOP_CD, D.CHNL_ID ORDER BY CHNL_SEND_DATE) 	AS CHNL_SEND_CNT_OVER_SUM /* 발송 건수 누적합 */
# 		     , E.CHNL_UNIT_PRICE 																	AS CHNL_UNIT_PRICE  	/* 발송단가 기본료(원) */
# 		     , CASE WHEN H.DSFRC_CD = '20' THEN E.CHNL_UNIT_FEE ELSE NULL END 					AS CHNL_UNIT_FEE		/* 발송단가 수수료(원) */
# 		     , CASE WHEN H.DSFRC_CD = '20' THEN E.CHNL_UNIT_PRICE_SH ELSE E.CHNL_UNIT_PRICE END 	AS CHNL_UNIT_PRICE_SH 	/* 발송단가 */
# 		     , J.APRV_DATE
# 		     , J.PROMOTION_ID
# 		     , J.PROMOTION_NM
# 		     , J.RPLAN_GP
# 		     , J.PROM_TYPE
# 		     , J.PROM_CHNL_NAME
# 		     , J.PROM_DESC
# 		     , J.PROM_SEND_CNT
# 		  FROM ${jdbc.QuadMaxMart.SchemaName}i_ums_cms_chnl_send_sum A
# 		       INNER JOIN ${jdbc.QuadMax.SchemaName}z_campaign B
# 		    ON A.CAMP_ID = B.CAMP_ID
# 		       INNER JOIN ${jdbc.QuadMax.SchemaName}z_camp_cell C
# 		    ON A.CAMP_ID = C.CAMP_ID 
# 		   AND B.CAMP_EXEC_NO = C.CAMP_EXEC_NO
# 		       INNER JOIN ${jdbc.QuadMax.SchemaName}Z_CHNL_SEND_REQ D
# 		    ON A.CAMP_ID = D.CAMP_ID
# 		   AND B.CAMP_EXEC_NO = D.CAMP_EXEC_NO
# 		   AND A.CHNL_SEND_REQ = D.CHNL_SEND_REQ 
# 		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}Z_EBM_SEND_CHANNEL_CUST D1							/* 실시간 발송의 경우 -> Z_EBM_SEND_CHANNEL_CUST 에서 참조 */
# 		    ON B.CAMP_BASE_TYPE = 'EBM'
# 		   AND A.CHNL_SEND_REQ = D1.DETECT_SEQ
# 		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}T_CHANNEL E
# 		    ON IFNULL(D1.CHNL_ID, D.CHNL_ID) = E.CHNL_ID
# 		   AND E.DEL_F ='N'
# 		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_channel E1
# 			ON E.CHNG_CHNL_YN = 'Y' /*전환채널1*/
# 		   AND E.CHNL_ID_1 = E1.CHNL_ID
# 			   LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_channel E2
# 			ON E.CHNG_CHNL_YN = 'Y' /*전환채널2*/
# 		   AND E.CHNL_ID_2 = E2.CHNL_ID
# 		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values F
# 		    ON F.LOOKUP_TYPE = 'CHANNEL_TYPE'
# 		   AND E.CHNL_TYPE_CD = F.LOOKUP_CODE
# 		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values F1
# 			ON F1.LOOKUP_TYPE ='CHANNEL_TYPE'
# 		   AND A.CHNL_CD = F1.VAL10  /*전환채널1*/
# 		   AND E.CHNG_CHNL_YN = 'Y'
# 		   AND E1.CHNL_TYPE_CD = F1.LOOKUP_CODE
# 			   LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values F2
# 			ON F2.LOOKUP_TYPE ='CHANNEL_TYPE'
# 		   AND A.CHNL_CD = F2.VAL10  /*전환채널2*/
# 		   AND E.CHNG_CHNL_YN = 'Y'
# 		   AND E2.CHNL_TYPE_CD = F2.LOOKUP_CODE
# 		       INNER JOIN ${jdbc.QuadMax.SchemaName}z_camp_bill_shop G
# 		    ON A.CAMP_ID = G.CAMP_ID
# 		       INNER JOIN ${jdbc.QuadMax.SchemaName}t_emp_dept H
# 		    ON G.SHOP_CD = H.DEPT_ID
# 		       LEFT OUTER JOIN ${jdbc.QuadMaxMart.SchemaName}I_CDW_CMS_TMP_CMP_STOR_CUST_DSTRB I
# 		    ON a.CAMP_ID = I.CMP_ID 
# 		   AND G.SHOP_CD = I.STOR_CD
# 		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}rplan_join K
# 		    ON G.SHOP_CD = K.STORE_CD
# 		   AND A.CHNL_SEND_DATE >= K.RPLAN_JOIN_DT
# 		   AND A.CHNL_SEND_DATE <![CDATA[<=]]> K.RPLAN_END_DT
# 		       LEFT OUTER JOIN 
# 		       (SELECT a.PROMOTION_ID
# 				      , b.promotion_nm
# 				      , a.STORE_CD
# 				      , b.RPLAN_ID
# 				      , d.RPLAN_NM AS RPLAN_GP
# 				      , F.LOOKUP_NAME AS PROM_TYPE
# 				      , CONCAT(b.PROM_DAY_CNT, '일 ', c.PROM_SEND_CNT, '건 무료') AS PROM_DESC
# 				      , a.APRV_DATE
# 				      , b.PROM_DAY_CNT
# 				      , date_format(date_add(str_to_date(a.aprv_date, '%Y%m%d'), INTERVAL b.PROM_DAY_CNT - 1 DAY), '%Y%m%d') AS END_DATE
# 				      , c.CHNL_ID
# 				      , c.PROM_SEND_CNT
# 				      , G.CHNL_NAME		AS PROM_CHNL_NAME
# 				   FROM ${jdbc.QuadMax.SchemaName}promotion_req a
# 						INNER JOIN ${jdbc.QuadMax.SchemaName}promotion_list b
# 					 ON a.PROMOTION_ID = b.PROMOTION_ID
# 						INNER JOIN ${jdbc.QuadMax.SchemaName}promotion_chnnl_capacity c
# 				     ON a.PROMOTION_ID = c.PROMOTION_ID
# 				        LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}RPLAN_LIST d
# 				     ON b.RPLAN_ID = d.RPLAN_ID
# 				        LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}T_LOOKUP_VALUES F
# 				     ON F.LOOKUP_TYPE = 'PROM_TYPE'
# 				    AND B.PROM_TYPE = F.LOOKUP_CODE
# 				        LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}T_CHANNEL G
# 				     ON C.CHNL_ID = G.CHNL_ID
# 				  WHERE 1 = 1
# 					AND b.prom_TYPE = 'CHNL_SEND_FREE' /* 발송비프로모션 */
# 					AND a.APRV_STAT_CD IN ('Y', 'CF', 'F') /* 프로모션 승인 완료 */
# 			   ) J
# 		    ON G.SHOP_CD = J.STORE_CD
# 		   AND D.CHNL_ID = J.CHNL_ID
# 		   AND A.CHNL_SEND_DATE >= J.APRV_DATE
# 		   AND A.CHNL_SEND_DATE <![CDATA[<=]]> J.END_DATE  
# 		   AND B.BILL_CHRG_CD = 'SH'
# 		   AND J.RPLAN_ID = K.RPLAN_ID
# 		 WHERE 1=1
# 		   AND (B.BILL_CHRG_CD = 'SH' AND H.DSFRC_CD = '20') /* 가맹점에 한해 정산 */
# 		   AND A.CHNL_CD <![CDATA[<>]]> 'PUSH' 	/*고정조건 PUSH 제외 - 2023.01.27 추가*/
# 		   AND ((E.CHNG_CHNL_YN IS NULL AND A.CHNL_CD = F.VAL10) OR E.CHNG_CHNL_YN ='Y' AND (F1.VAL10 IS NOT NULL OR F2.VAL10 IS NOT NULL)) /*고정조건*/
# 		   AND a.BILL_DEPT_CD = #{billDeptCd}	/* 변수 처리 정산 부서 */
		   
# 		       UNION ALL
		       
# 		/* 테스트 및 참조발송(이상치 제외) 프로모션 적용 안함 */	
# 		SELECT A.CHNL_SEND_DATE 												AS CHNL_SEND_DATE  		/* 발송일 */
# 		     , A.CHNL_SEND_YM 													AS CHNL_SEND_YM  		/* 발송 년월 */
# 		     , B.CAMP_ID        												AS CAMP_ID  			/* 캠페인 ID */
# 		     , B.CAMP_NAME      												AS CAMP_NAME 			/* 캠페인 명 */
# 		     , B.BRAND_CD      												    AS BRAND_CD 			/* 브랜드명 */
# 		     , B.REG_DEPT_ID 													AS REG_DEPT_ID
# 		     , B.REG_EMP_ID     												AS REG_EMP_ID 			/* 담당자 ID */
# 		     , CASE WHEN E.CHNG_CHNL_YN = 'Y' 
# 		            THEN (CASE WHEN F1.VAL10 IS NOT NULL 
# 		                       THEN E1.CHNL_NAME
# 		     				   ELSE (CASE WHEN F2.VAL10 IS NOT NULL 
# 		     				              THEN E2.CHNL_NAME END) END)
# 			 		ELSE E.CHNL_NAME END 										AS CHNL_NAME 			/* 발송채널 */
# 		     , H.DSFRC_CD 																				/* 직가구분 */
# 		     , G.SHOP_CD        												AS SHOP_CD 				/* 대상 점포 코드 */
# 		     , H.DEPT_NAME       												AS STORE_NM 			/* 대상 점포 명 */
# 		     , B.BILL_CHRG_CD  										  									/* 비용 부담 부서 */
# 		     , B.BILL_DEPT_CD  													                  		/* 정산 부서 */
# 		     , A.CHNL_SEND_CNT 
# 		     , NULL 															AS CHNL_SEND_CNT_OVER_SUM /* 발송 건수 누적합 */
# 		     , E.CHNL_UNIT_PRICE 												AS CHNL_UNIT_PRICE  	/* 발송단가 기본료(원) */
# 		     , CASE WHEN H.DSFRC_CD = '20' THEN E.CHNL_UNIT_FEE ELSE NULL END AS CHNL_UNIT_FEE		/* 발송단가 수수료(원) */
# 		     , CASE WHEN H.DSFRC_CD = '20' THEN E.CHNL_UNIT_PRICE_SH ELSE E.CHNL_UNIT_PRICE END 	AS CHNL_UNIT_PRICE_SH 	/* 발송단가 */
# 		     , NULL 															AS APRV_DATE
# 		     , NULL 															AS PROMOTION_ID
# 		     , NULL 															AS PROMOTION_NM
# 		     , NULL 															AS RPLAN_GP
# 		     , NULL 															AS PROM_TYPE
# 		     , NULL 															AS PROM_CHNL_NAME
# 		     , NULL 															AS PROM_DESC
# 		     , NULL 															AS PROM_SEND_CNT
# 		  FROM ${jdbc.QuadMaxMart.SchemaName}i_ums_cms_chnl_send_sum A
# 		       INNER JOIN ${jdbc.QuadMax.SchemaName}t_campaign B
# 		    ON A.CAMP_ID = B.CAMP_ID
# 		   AND B.BILL_CHRG_CD = 'SH'
# 		       INNER JOIN ${jdbc.QuadMax.SchemaName}T_camp_cell C
# 		    ON A.CAMP_ID = C.CAMP_ID 
# 		       INNER JOIN ${jdbc.QuadMax.SchemaName}Z_CHNL_SEND_REQ_REF D
# 		    ON A.CAMP_ID = D.CAMP_ID
# 		   AND A.CHNL_SEND_REQ = D.REF_SEND_REQ_SEQ
# 		   AND A.CHNL_SEND_REQ LIKE '%R%'
# 		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}T_CHANNEL E
# 		    ON D.CHNL_ID = E.CHNL_ID
# 		   AND E.DEL_F ='N'
# 		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_channel E1
# 			ON E.CHNG_CHNL_YN = 'Y' /*전환채널1*/
# 		   AND E.CHNL_ID_1 = E1.CHNL_ID
# 			   LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_channel E2
# 			ON E.CHNG_CHNL_YN = 'Y' /*전환채널2*/
# 		   AND E.CHNL_ID_2 = E2.CHNL_ID
# 		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values F
# 		    ON F.LOOKUP_TYPE = 'CHANNEL_TYPE'
# 		   AND E.CHNL_TYPE_CD = F.LOOKUP_CODE
# 		       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values F1
# 			ON F1.LOOKUP_TYPE ='CHANNEL_TYPE'
# 		   AND A.CHNL_CD = F1.VAL10  /*전환채널1*/
# 		   AND E.CHNG_CHNL_YN = 'Y'
# 		   AND E1.CHNL_TYPE_CD = F1.LOOKUP_CODE
# 			   LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values F2
# 			ON F2.LOOKUP_TYPE ='CHANNEL_TYPE'
# 		   AND A.CHNL_CD = F2.VAL10  /*전환채널2*/
# 		   AND E.CHNG_CHNL_YN = 'Y'
# 		   AND E2.CHNL_TYPE_CD = F2.LOOKUP_CODE
# 		       INNER JOIN ${jdbc.QuadMax.SchemaName}t_camp_bill_shop G
# 		    ON A.CAMP_ID = G.CAMP_ID
# 		       INNER JOIN ${jdbc.QuadMax.SchemaName}t_emp_dept H
# 		    ON G.SHOP_CD = H.DEPT_ID
# 		 WHERE 1=1
# 		   AND (B.BILL_CHRG_CD = 'SH' AND H.DSFRC_CD = '20') /* 가맹점에 한해 정산 */
# 		   AND A.CHNL_CD <![CDATA[<>]]> 'PUSH' 	/*고정조건 PUSH 제외 - 2023.01.27 추가*/
# 		   AND ((E.CHNG_CHNL_YN IS NULL AND A.CHNL_CD = F.VAL10) OR E.CHNG_CHNL_YN ='Y' AND (F1.VAL10 IS NOT NULL OR F2.VAL10 IS NOT NULL)) /*고정조건*/
# 		   AND a.BILL_DEPT_CD = #{billDeptCd}	/* 변수 처리 정산 부서 */
# 		 order by CHNL_SEND_DATE
# 		     , SHOP_CD
#        ),
# moon as (
# /*CTE 구문 테스트*/select * from 1)
# , moon2  as(/*union 시험 테스트*/ 
# select * from 1 where 1=1 and talb2 =1 or 2 group by 2)       
# SELECT CONCAT(SUBSTRING(A.CHNL_SEND_YM,1, 4), '년 ', CASE WHEN SUBSTRING(A.CHNL_SEND_YM, 5, 6) <![CDATA[<]]> 10 
#  														THEN SUBSTRING(A.CHNL_SEND_YM, 6, 6)
#  														ELSE SUBSTRING(A.CHNL_SEND_YM, 5, 6) END , '월') 	AS a1	/* 조회월 (화면) */
#  	 , A.CHNL_SEND_YM
#      , CONCAT(SUBSTRING(#{billPeriod} /* 변수 처리 조회월*/, 5, 6), '월 ', #{billGeneration} /* 변수 처리 조회 기수 */, '기') 			AS a2 	/* 정산월 (화면) */
#      , A.SHOP_CD																							AS a3	/* 점포 코드 */
#      , A.STORE_NM																							AS a4 	/* 점포명 (화면) */
#      , CASE WHEN A.DSFRC_CD = '10' THEN '직'
#             WHEN A.DSFRC_CD = '20' THEN '가'	
#             ELSE '직/가 구분 불명' END 																			AS a5	/* 직가 */
#      , '' 																									AS a6	/* 사업자 번호 */
#      , CONCAT(SUBSTRING(B.STLM_YYYYMM, 5, 6), '월 ', B.STLM_PERIOD, '기') 									AS a7	/* 조기마감 (화면) */
#      , C.LOOKUP_NAME 																						AS a8	/* 조기마감종류 (화면) */
#      , E.EMP_NAME 																							AS a9	/* SV사원 */
#      , A.CHNL_NAME																							AS a10	/* 발송 채널 (화면) */	
#      , SUM(A.CHNL_SEND_CNT)																					AS a11	/* 발송 건수(건) */
#      , CAST(ROUND(MAX(A.CHNL_UNIT_PRICE), 1) AS DECIMAL(20, 1))												AS a12 	/* 발송단가 기본료(원) */
#      , CAST(ROUND(MAX(A.CHNL_UNIT_FEE), 1) AS DECIMAL(20, 1))												AS a13 	/* 발송단가 수수료(원) */
#      , CAST(ROUND(SUM(A.CHNL_SEND_CNT * A.CHNL_UNIT_PRICE),0) AS DECIMAL(20, 0))							AS a14  /* (프로모션 적용 전) 발송금액 기본료(원) */
#      , CAST(ROUND(SUM(A.CHNL_SEND_CNT * A.CHNL_UNIT_FEE),0) AS DECIMAL(20, 0))								AS a15  /* (프로모션 적용 전) 발송금액 수수료(원) */
#      , CAST(ROUND(SUM(A.CHNL_SEND_CNT * A.CHNL_UNIT_PRICE_SH),0) AS DECIMAL(20, 0))							AS a16  /* (프로모션 적용 전) 발송금액(원) */
#      , A.APRV_DATE																							AS a17	/* 프로모션 적용일 */
#      , A.PROMOTION_ID																						AS a18	/* 프로모션 ID */
#      , A.PROMOTION_NM																						AS a19	/* 프로모션 명 */
#      , A.RPLAN_GP																							AS a20	/* 대상요금제 */
#      , A.PROM_TYPE					 																		AS a21	/* 프로모션 종류 */
#      , A.PROM_DESC																							AS a22	/* 프로모션 내용 */
#      , A.PROM_CHNL_NAME																						AS a23	/* 발송 채널*/	
#      , SUM(CASE WHEN A.PROM_SEND_CNT > CHNL_SEND_CNT_OVER_SUM 
#                 THEN A.CHNL_SEND_CNT
#                 ELSE (CASE WHEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT > 0
#                           THEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT
#                           ELSE NULL END)
#                 END)																						AS a24	/* (프로모션 무료) 발송 건수(건) */
#      , CAST(ROUND(SUM(CASE WHEN A.PROM_SEND_CNT > CHNL_SEND_CNT_OVER_SUM 
#                       THEN A.CHNL_SEND_CNT
#                       ELSE (CASE WHEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT > 0
#                                 THEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT
#                                 ELSE 0 END)
#                        END * A.CHNL_UNIT_PRICE), 0)	AS DECIMAL(20,0))										AS a25	/* (프로모션 무료) 발송금액 기본료(원) */
#      , CAST(ROUND(SUM(CASE WHEN A.PROM_SEND_CNT > CHNL_SEND_CNT_OVER_SUM 
#                       THEN A.CHNL_SEND_CNT
#                       ELSE (CASE WHEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT > 0
#                                 THEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT
#                                 ELSE 0 END)
#                        END	* A.CHNL_UNIT_FEE), 0) AS DECIMAL(20,0))										AS a26	/* (프로모션 무료) 발송금액 수수료(원) */
#      , CAST(ROUND(SUM(CASE WHEN A.PROM_SEND_CNT > CHNL_SEND_CNT_OVER_SUM 
#             	      THEN A.CHNL_SEND_CNT
#             	      ELSE (CASE WHEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT > 0
#                       	        THEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT
#                       		    ELSE 0 END)
#             	       END * A.CHNL_UNIT_PRICE_SH), 0) AS DECIMAL(20,0))									AS a27	/* (프로모션 무료) 발송금액(원) (화면) */
#      , CAST(ROUND(SUM(A.CHNL_SEND_CNT - CASE WHEN A.PROM_SEND_CNT > CHNL_SEND_CNT_OVER_SUM 
#             					         THEN A.CHNL_SEND_CNT
#             					         ELSE (CASE WHEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT > 0
#                       					           THEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT
#                       				       	   	   ELSE 0 END)
#             			          		  END	* A.CHNL_UNIT_PRICE),0) AS DECIMAL(20,0))					AS a28	/* (프로모션 적용 후) 발송금액 기본료(원) */
#      , CAST(ROUND(SUM(A.CHNL_SEND_CNT - CASE WHEN A.PROM_SEND_CNT > CHNL_SEND_CNT_OVER_SUM 
#             					 		 THEN A.CHNL_SEND_CNT
#             					 		 ELSE (CASE WHEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT > 0
#                       					   		   THEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT
#                       				       		   ELSE 0 END)
#             			          		  END	* A.CHNL_UNIT_FEE),0) AS DECIMAL(20,0))						AS a29	/* (프로모션 적용 후) 발송금액 수수료(원) */
#      , CAST(ROUND(SUM(A.CHNL_SEND_CNT - CASE WHEN A.PROM_SEND_CNT > CHNL_SEND_CNT_OVER_SUM 
#             					 		 THEN A.CHNL_SEND_CNT
#             					 		 ELSE (CASE WHEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT > 0
#                       					   		   THEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT
#                       				       		   ELSE 0 END)
#             			          		  END	* A.CHNL_UNIT_PRICE_SH), 0)	AS DECIMAL(20,0))				AS a30	/* (프로모션 적용 후) 발송금액(원) (화면) */
#   FROM SH_BILL_INFO A
#        LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}EARLY_CLOSING_STORE_LIST B
#     ON A.SHOP_CD = B.STORE_CD
#    AND ((B.STLM_YYYYMM = #{billPeriod} /* 변수 처리 조회월 */ AND B.STLM_PERIOD = '1') /* 당월 1기 정산의 경우 모두 제외 */
#    		 OR (B.STLM_YYYYMM = DATE_FORMAT(DATE_ADD(concat(#{billPeriod} /* 변수 처리 조회월 */, '01'), INTERVAL -1 MONTH), '%Y%m') AND B.STLM_PERIOD = '1') /* 전월 1기 정산의 경우 15일까지의 건수 제외 */
#          OR (B.STLM_YYYYMM = DATE_FORMAT(DATE_ADD(concat(#{billPeriod} /* 변수 처리 조회월 */, '01'), INTERVAL -1 MONTH), '%Y%m') AND B.STLM_PERIOD = '2') /* 전월 2기 정산의 경우 모두 제외 */
#        )
#    AND B.DEL_F = 'N'
#        LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}T_LOOKUP_VALUES C
#     ON C.LOOKUP_TYPE = 'GRS_SHOP_STAT_CD'
#    AND B.CHG_TYPE_CD = C.LOOKUP_CODE
#        LEFT OUTER JOIN
#        (SELECT STORECD
#              , SUBSTRING(WORK_DE, 1, 6) AS WORK_DE
#              , SV_EMPNO
#              , ROW_NUMBER() OVER(PARTITION BY STORECD, SUBSTRING(WORK_DE, 1, 6) ORDER BY WORK_DE DESC) AS RN
#           FROM ${jdbc.QuadMaxMart.SchemaName}CDW_RIA_SMT100TM_SV 
#          ) D						/* 사용월 기준 가장 최신 SV 데이터를 이용함 */
#     ON A.CHNL_SEND_YM = D.WORK_DE
#    AND A.SHOP_CD = D.STORECD
#    AND D.RN = 1
#        LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_emp E
#     ON D.SV_EMPNO = E.ORG_USER_CODE
#  WHERE 1 = 1
#    AND #{billGeneration} /* 화면 INPUT 조회 기수 */ = '2'
#    AND ((B.STORE_CD IS NULL AND A.CHNL_SEND_YM = DATE_FORMAT(DATE_ADD(concat( #{billPeriod} /* 변수 처리 조회월 */, '01'), INTERVAL -1 MONTH), '%Y%m'))	/* 당월 1기, 전월 2기 정산 제외 */
#        OR ((B.STLM_YYYYMM = DATE_FORMAT(DATE_ADD(concat(#{billPeriod} /* 변수 처리 조회월 */, '01'), INTERVAL -1 MONTH), '%Y%m') AND B.STLM_PERIOD = '1')
#           AND A.CHNL_SEND_DATE > DATE_FORMAT(DATE_ADD(concat(#{billPeriod} /* 변수 처리 조회월 */, '15'), INTERVAL -1 MONTH), '%Y%m')
#           AND A.CHNL_SEND_DATE <![CDATA[<]]> concat(#{billPeriod} /* 변수 처리 조회월 */, '01')
#           )
#        )			/* 전월 1기 정산의 경우 16일 이후 건만 조회 */
#  GROUP BY A.SHOP_CD
#  	 , A.STORE_NM 
#  	 , A.DSFRC_CD
#      , A.CHNL_SEND_YM
#      , B.STLM_YYYYMM
#      , B.STLM_PERIOD
#      , C.LOOKUP_NAME
#      , E.EMP_NAME 
#      , A.CHNL_NAME
#      , A.APRV_DATE																						
#      , A.PROMOTION_ID																					
#      , A.PROMOTION_NM																						
#      , A.RPLAN_GP																							
#      , A.PROM_TYPE					 																
#      , A.PROM_DESC	
#      , A.PROM_CHNL_NAME		
     
     
#        UNION ALL
       
       
# SELECT CONCAT(SUBSTRING(A.CHNL_SEND_YM,1, 4), '년 ', CASE WHEN SUBSTRING(A.CHNL_SEND_YM, 5, 6) <![CDATA[<]]> 10 
#  														THEN SUBSTRING(A.CHNL_SEND_YM, 6, 6)
#  														ELSE SUBSTRING(A.CHNL_SEND_YM, 5, 6) END , '월') 	AS a1	/* 조회월 (화면) */
#  	 , A.CHNL_SEND_YM
#      , CONCAT(SUBSTRING(#{billPeriod} /* 변수 처리 조회월*/, 5, 6), '월 ', #{billGeneration} /* 변수 처리 조회 기수 */, '기') 			AS a2 	/* 정산월 (화면) */
#      , A.SHOP_CD																							AS a3	/* 점포 코드 */
#      , A.STORE_NM																							AS a4 	/* 점포명 (화면) */
#      , CASE WHEN A.DSFRC_CD = '10' THEN '직'
#             WHEN A.DSFRC_CD = '20' THEN '가'	
#             ELSE '직/가 구분 불명' END 																			AS a5	/* 직가 */
#      , '' 																									AS a6	/* 사업자 번호 */
#      , CONCAT(SUBSTRING(B.STLM_YYYYMM, 5, 6), '월 ', B.STLM_PERIOD, '기') 									AS a7	/* 조기마감 (화면) */
#      , C.LOOKUP_NAME 																						AS a8	/* 조기마감종류 (화면) */
#      , E.EMP_NAME 																							AS a9	/* SV사원 */
#      , A.CHNL_NAME																							AS a10	/* 발송 채널 (화면) */	
#      , SUM(A.CHNL_SEND_CNT)																					AS a11	/* 발송량(건) */
#      , CAST(ROUND(MAX(A.CHNL_UNIT_PRICE), 1) AS DECIMAL(20, 1))												AS a12 	/* 발송단가 기본료(원) */
#      , CAST(ROUND(MAX(A.CHNL_UNIT_FEE), 1) AS DECIMAL(20, 1))												AS a13 	/* 발송단가 수수료(원) */
#      , CAST(ROUND(SUM(A.CHNL_SEND_CNT * A.CHNL_UNIT_PRICE),0) AS DECIMAL(20, 0))							AS a14  /* (프로모션 적용 전) 발송금액 기본료(원) */
#      , CAST(ROUND(SUM(A.CHNL_SEND_CNT * A.CHNL_UNIT_FEE),0) AS DECIMAL(20, 0))								AS a15  /* (프로모션 적용 전) 발송금액 수수료(원) */
#      , CAST(ROUND(SUM(A.CHNL_SEND_CNT * A.CHNL_UNIT_PRICE_SH),0) AS DECIMAL(20, 0))							AS a16  /* (프로모션 적용 전) 발송금액(원) */
#      , A.APRV_DATE																							AS a17	/* 프로모션 적용일 */
#      , A.PROMOTION_ID																						AS a18	/* 프로모션 ID */
#      , A.PROMOTION_NM																						AS a19	/* 프로모션 명 */
#      , A.RPLAN_GP																							AS a20	/* 대상요금제 */
#      , A.PROM_TYPE					 																		AS a21	/* 프로모션 종류 */
#      , A.PROM_DESC																							AS a22	/* 프로모션 내용 */
#      , A.PROM_CHNL_NAME																						AS a23	/* 프로모션 적용 채널*/	
#      , SUM(CASE WHEN A.PROM_SEND_CNT > CHNL_SEND_CNT_OVER_SUM 
#                 THEN A.CHNL_SEND_CNT
#                 ELSE (CASE WHEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT > 0
#                           THEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT
#                           ELSE NULL END)
#                 END)																						AS a24	/* (프로모션 무료) 발송 건수(건) */
#      , CAST(ROUND(SUM(CASE WHEN A.PROM_SEND_CNT > CHNL_SEND_CNT_OVER_SUM 
#                       THEN A.CHNL_SEND_CNT
#                       ELSE (CASE WHEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT > 0
#                                 THEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT
#                                 ELSE 0 END)
#                        END * A.CHNL_UNIT_PRICE), 0)	AS DECIMAL(20,0))										AS a25	/* (프로모션 무료) 발송금액 기본료(원) */
#      , CAST(ROUND(SUM(CASE WHEN A.PROM_SEND_CNT > CHNL_SEND_CNT_OVER_SUM 
#                       THEN A.CHNL_SEND_CNT
#                       ELSE (CASE WHEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT > 0
#                                 THEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT
#                                 ELSE 0 END)
#                        END	* A.CHNL_UNIT_FEE), 0) AS DECIMAL(20,0))										AS a26	/* (프로모션 무료) 발송금액 수수료(원) */
#      , CAST(ROUND(SUM(CASE WHEN A.PROM_SEND_CNT > CHNL_SEND_CNT_OVER_SUM 
#             	      THEN A.CHNL_SEND_CNT
#             	      ELSE (CASE WHEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT > 0
#                       	        THEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT
#                       		    ELSE 0 END)
#             	       END * A.CHNL_UNIT_PRICE_SH), 0) AS DECIMAL(20,0))									AS a27	/* (프로모션 무료) 발송금액(원) (화면) */
#      , CAST(ROUND(SUM(A.CHNL_SEND_CNT - CASE WHEN A.PROM_SEND_CNT > CHNL_SEND_CNT_OVER_SUM 
#             					         THEN A.CHNL_SEND_CNT
#             					         ELSE (CASE WHEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT > 0
#                       					           THEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT
#                       				       	   	   ELSE 0 END)
#             			          		  END	* A.CHNL_UNIT_PRICE),0) AS DECIMAL(20,0))					AS a28	/* (프로모션 적용 후) 발송금액 기본료(원) */
#      , CAST(ROUND(SUM(A.CHNL_SEND_CNT - CASE WHEN A.PROM_SEND_CNT > CHNL_SEND_CNT_OVER_SUM 
#             					 		 THEN A.CHNL_SEND_CNT
#             					 		 ELSE (CASE WHEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT > 0
#                       					   		   THEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT
#                       				       		   ELSE 0 END)
#             			          		  END	* A.CHNL_UNIT_FEE),0) AS DECIMAL(20,0))						AS a29	/* (프로모션 적용 후) 발송금액 수수료(원) */
#      , CAST(ROUND(SUM(A.CHNL_SEND_CNT - CASE WHEN A.PROM_SEND_CNT > CHNL_SEND_CNT_OVER_SUM 
#             					 		 THEN A.CHNL_SEND_CNT
#             					 		 ELSE (CASE WHEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT > 0
#                       					   		   THEN A.PROM_SEND_CNT - CHNL_SEND_CNT_OVER_SUM + A.CHNL_SEND_CNT
#                       				       		   ELSE 0 END)
#             			          		  END	* A.CHNL_UNIT_PRICE_SH), 0)	AS DECIMAL(20,0))				AS a30	/* (프로모션 적용 후) 발송금액(원) (화면) */
#   FROM SH_BILL_INFO A
#        INNER JOIN ${jdbc.QuadMax.SchemaName}EARLY_CLOSING_STORE_LIST B
#     ON A.SHOP_CD = B.STORE_CD
#    AND B.STLM_YYYYMM = #{billPeriod} /* 변수 처리 조회월 */
#    AND B.STLM_PERIOD = #{billGeneration} /* 변수 처리 조회 기수 */ 
#    AND B.DEL_F = 'N'
#        LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}T_LOOKUP_VALUES C
#     ON C.LOOKUP_TYPE = 'GRS_SHOP_STAT_CD'
#    AND B.CHG_TYPE_CD = C.LOOKUP_CODE
#        LEFT OUTER JOIN
#        (SELECT STORECD
#              , SUBSTRING(WORK_DE, 1, 6) AS WORK_DE
#              , SV_EMPNO
#              , ROW_NUMBER() OVER(PARTITION BY STORECD, SUBSTRING(WORK_DE, 1, 6) ORDER BY WORK_DE DESC) AS RN
#           FROM ${jdbc.QuadMaxMart.SchemaName}CDW_RIA_SMT100TM_SV 
#          ) D						/* 사용월 기준 가장 최신 SV 데이터를 이용함 */
#     ON A.CHNL_SEND_YM = D.WORK_DE
#    AND A.SHOP_CD = D.STORECD
#    AND D.RN = 1
#        LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_emp E
#     ON D.SV_EMPNO = E.ORG_USER_CODE
#  WHERE a.CHNL_SEND_DATE >= CASE WHEN #{billGeneration} /* 변수 처리 조회 기수 */ = '1' 
#                                 THEN DATE_FORMAT(DATE_ADD(concat(#{billPeriod} /* 변수 처리 조회월 */, '01'), INTERVAL -1 MONTH), '%Y%m%d')
# 			                    ELSE concat(#{billPeriod} /* 변수 처리 조회월 */, '01') END 
#    AND a.CHNL_SEND_DATE <![CDATA[<=]]> CASE WHEN #{billGeneration} /* 변수 처리 조회 기수 */ = '1'  
#                                 THEN concat(#{billPeriod} /* 변수 처리 조회월 */, '15')
# 			                    ELSE DATE_FORMAT(last_day(DATE_FORMAT(concat(#{billPeriod} /* 변수 처리 조회월*/, '01'), '%Y%m%d')), '%Y%m%d') END
#  GROUP BY A.SHOP_CD
#  	 , A.STORE_NM
#  	 , A.DSFRC_CD
#      , A.CHNL_SEND_YM
#      , B.STLM_YYYYMM
#      , B.STLM_PERIOD
#      , C.LOOKUP_NAME
#      , E.EMP_NAME 
#      , A.CHNL_NAME
#      , A.APRV_DATE																						
#      , A.PROMOTION_ID																					
#      , A.PROMOTION_NM																						
#      , A.RPLAN_GP																							
#      , A.PROM_TYPE					 																
#      , A.PROM_DESC	
#      , A.PROM_CHNL_NAME		
#  ORDER BY a3
#      , CHNL_SEND_YM"""



# sql_query="""SELECT 
#     u.user_id,
#     u.user_name,
#     u.email,
#     COALESCE(SUM(p.amount), 0) AS total_payments,
#     COUNT(DISTINCT o.order_id) AS total_orders,
#     CASE 
#         WHEN AVG(EXTRACT(EPOCH FROM (o.order_end - o.order_start))) > 3600 THEN 'Long Session'
#         WHEN AVG(EXTRACT(EPOCH FROM (o.order_end - o.order_start))) > 1800 THEN 'Medium Session'
#         ELSE 'Short Session'
#     END AS avg_session_category
# FROM users u
# LEFT JOIN orders o
#     ON u.user_id = o.user_id
# INNER JOIN payments p
#     ON o.order_id = p.order_id
# CROSS JOIN (
#     SELECT config_key, config_value
#     FROM system_config
#     WHERE environment = 'production'
# ) sc
# INNER JOIN A
#  ON o.user_id = 
#         CASE 
#             WHEN u.user_type = 'guest' THEN 
#                 (CASE 
#                     WHEN u.temp_id IS NOT NULL THEN u.temp_id
#                     ELSE -1
#                 END)
#             ELSE u.user_id
#         END
# WHERE 1 = 1
#   AND 
#     CASE 
#         WHEN u.country = 'US' THEN 
#             (CASE WHEN u.age >= 18 THEN TRUE ELSE FALSE end)
#         ELSE 
#             (CASE WHEN u.age >= 20 THEN TRUE ELSE FALSE end)
#     END
  
# GROUP BY 
#     u.user_id,
#     u.user_name,
#     u.email,
#     case when 1=1 then (case when 2=2 then 2 end )end 0
# HAVING 
#     AND (
#         SUM(p.amount) > 1000
#     )
#     AND (
#         COUNT(o.order_id) >= 3
#     )
#     and case when 1=1 then (case when 2=2 then 2 end )end 0
# ORDER BY 
#     total_payments DESC,
#     avg_session_category ASC,
#     case when 1=1 then (case when 2=2 then 2 end )end 0
#     ;
# """


open_count = sql_query.count('(')
close_count = sql_query.count(')')
print(open_count)
print(close_count)


def save_to_sql_file(filename: str, sql_content: str):
    """정렬된 SQL을 파일로 저장"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(sql_content + "\n")


#final_sql = add_space_around_parentheses(sql_query)
#final_sql = moon_gogo(sql_query)
final_sql = last_start(sql_query)

matches = re.findall(r'[A-Za-z0-9\(\),\.\'\*=-]', sql_query)

matches2 = re.findall(r'[A-Za-z0-9\(\),\.\'\*=-]', final_sql)
# 순수 문자 갯수 세기
pure_char_count = len(matches)
pure_char_count2 = len(matches2)

print('변경전 글자수:',pure_char_count)
print('변경후 글자수:',pure_char_count2)


save_to_sql_file("sql_sorted.sql",final_sql)


