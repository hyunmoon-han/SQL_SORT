SELECT A.CHNL_SEND_DATE  AS CHNL_SEND_DATE /*발송일*/
     , B.CAMP_ID  AS CAMP_ID /*캠페인 ID*/
     , B.CAMP_NAME       AS CAMP_NAME /*캠페인 명*/
     , B.BRAND_CD        AS BRAND_CD /*브랜드명*/
     , B.REG_DEPT_ID     AS REG_DEPT_ID
     , B.REG_EMP_ID      AS REG_EMP_ID /*담당자 ID*/
     , CASE WHEN E.CHNG_CHNL_YN = 'Y' THEN ( CASE WHEN F1.VAL10 IS NOT NULL THEN E1.CHNL_NAME 
                                                                            ELSE ( CASE WHEN F2.VAL10 IS NOT NULL THEN E2.CHNL_NAME 
                                                                                                                 END ) 
                                                                            END ) 
                                      ELSE E.CHNL_NAME 
                                      END AS CHNL_NAME /*발송채널 ID*/
     , H.DSFRC_CODE /*직가구분*/
     , G.SHOP_CD  AS SHOP_CD /*대상 점포 코드*/
     , H.STORE_NM        AS STORE_NM /*대상 점포 명*/
     , B.BILL_CHRG_CD /*비용 부담 부서*/
     , B.BILL_DEPT_CD /*정산 부서*/
     , CASE WHEN E.CHNG_CHNL_YN IS NULL AND A.CHNL_CD = F.VAL10 THEN ( CASE WHEN D1.DETECT_SEQ IS NOT NULL THEN ( CASE WHEN D1.CUST_TYPE_CD = 'T' THEN 1 
                                                                                                                                                     ELSE 0 
                                                                                                                                                     END ) 
                                                                            WHEN I.STOR_CD IS NULL THEN A.CHNL_SEND_CNT 
                                                                            ELSE I.STOR_DSTRB_CUST_CNT 
                                                                            END ) 
            WHEN E.CHNG_CHNL_YN ='Y' AND (F1.VAL10 IS NOT NULL OR F2.VAL10 IS NOT NULL) THEN ( CASE WHEN D1.DETECT_SEQ IS NOT NULL THEN ( CASE WHEN D1.CUST_TYPE_CD = 'T' THEN 1 
                                                                                                                                                                             ELSE 0 
                                                                                                                                                                             END ) 
                                                                                                    WHEN I.STOR_CD IS NULL THEN A.CHNL_SEND_CNT 
                                                                                                    ELSE I.STOR_DSTRB_CUST_CNT 
                                                                                                    END ) 
            ELSE 0 
            END AS CHNL_SEND_CNT /*발송량*/
     , SUM ( CASE WHEN E.CHNG_CHNL_YN IS NULL AND A.CHNL_CD = F.VAL10 THEN ( CASE WHEN I.STOR_CD IS NULL THEN A.CHNL_SEND_CNT 
                                                                                                         ELSE I.STOR_DSTRB_CUST_CNT 
                                                                                                         END ) 
                  WHEN E.CHNG_CHNL_YN ='Y' AND (F1.VAL10 IS NOT NULL OR F2.VAL10 IS NOT NULL) THEN ( CASE WHEN I.STOR_CD IS NULL THEN A.CHNL_SEND_CNT 
                                                                                                                                 ELSE I.STOR_DSTRB_CUST_CNT 
                                                                                                                                 END ) 
                  ELSE 0 
                  END ) OVER (PARTITION BY J.PROMOTION_ID, G.SHOP_CD, D.CHNL_ID ORDER BY CHNL_SEND_DATE) AS CHNL_SEND_CNT_OVER_SUM /*발송 건수 누적합*/
     , E.CHNL_UNIT_PRICE AS CHNL_UNIT_PRICE /*발송단가 기본료(원)*/
     , CASE WHEN H.DSFRC_CODE = '20' THEN E.CHNL_UNIT_FEE 
                                     ELSE NULL 
                                     END AS CHNL_UNIT_FEE /*발송단가 수수료(원)*/
     , CASE WHEN H.DSFRC_CODE = '20' THEN E.CHNL_UNIT_PRICE_SH 
                                     ELSE E.CHNL_UNIT_PRICE 
                                     END AS CHNL_UNIT_PRICE_SH /*발송단가*/
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
   AND A.CHNL_CD = F1.VAL10 /*전환채널1*/
   AND E.CHNG_CHNL_YN = 'Y'
   AND E1.CHNL_TYPE_CD = F1.LOOKUP_CODE
       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values F2
    ON F2.LOOKUP_TYPE ='CHANNEL_TYPE'
   AND A.CHNL_CD = F2.VAL10 /*전환채널2*/
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
       LEFT OUTER JOIN (SELECT a.PROMOTION_ID
                             , b.promotion_nm
                             , a.STORE_CD
                             , b.RPLAN_ID
                             , e.LOOKUP_NAME                                                          AS RPLAN_GP
                             , F.LOOKUP_NAME                                                          AS PROM_TYPE
                             , CONCAT (H.PROM_DESC, ' (', b.PROM_DAY_CNT, '일) ')                      AS PROM_DESC
                             , a.APRV_DATE
                             , b.PROM_DAY_CNT
                             , date_format (date_add (str_to_date (a.aprv_date, '%Y%m%d') , INTERVAL b.PROM_DAY_CNT - 1 DAY) , '%Y%m%d') AS END_DATE
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
                               LEFT OUTER JOIN (SELECT A.PROMOTION_ID
                                                     , GROUP_CONCAT (CONCAT (C.CHNL_NAME) , ' ', B.PROM_SEND_CNT, '건' SEPARATOR ', ') AS PROM_DESC
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
                           AND b.prom_TYPE = 'CHNL_SEND_FREE' /*발송비프로모션*/
                           AND a.APRV_STAT_CD IN ('Y', 'CF', 'F') /*프로모션 승인 완료*/ 
                        ) J
    ON G.SHOP_CD = J.STORE_CD
   AND D.CHNL_ID = J.CHNL_ID
   AND A.CHNL_SEND_DATE >= J.APRV_DATE
   AND A.CHNL_SEND_DATE <![CDATA[<=]]> J.END_DATE
   AND B.BILL_CHRG_CD = 'SH'
   AND J.RPLAN_ID = K.RPLAN_ID
 WHERE 1=1
   AND A.CHNL_CD <![CDATA[<>]]> 'PUSH' /*고정조건 PUSH 제외 - 2023.01.27 추가*/
   AND ((E.CHNG_CHNL_YN IS NULL AND A.CHNL_CD = F.VAL10)
    OR E.CHNG_CHNL_YN ='Y'
   AND (F1.VAL10 IS NOT NULL OR F2.VAL10 IS NOT NULL) ) /*고정조건*/
UNION ALL
/*테스트 및 참조발송(이상치 제외) 프로모션 적용 안함*/
SELECT A.CHNL_SEND_DATE  AS CHNL_SEND_DATE /*발송일*/
     , B.CAMP_ID  AS CAMP_ID /*캠페인 ID*/
     , B.CAMP_NAME       AS CAMP_NAME /*캠페인 명*/
     , B.BRAND_CD        AS BRAND_CD /*브랜드명*/
     , B.REG_DEPT_ID     AS REG_DEPT_ID
     , B.REG_EMP_ID      AS REG_EMP_ID /*담당자 ID*/
     , CASE WHEN E.CHNG_CHNL_YN = 'Y' THEN ( CASE WHEN F1.VAL10 IS NOT NULL THEN E1.CHNL_NAME 
                                                                            ELSE ( CASE WHEN F2.VAL10 IS NOT NULL THEN E2.CHNL_NAME 
                                                                                                                 END ) 
                                                                            END ) 
                                      ELSE E.CHNL_NAME 
                                      END AS CHNL_NAME /*발송채널 ID*/
     , H.DSFRC_CODE /*직가구분*/
     , G.SHOP_CD  AS SHOP_CD /*대상 점포 코드*/
     , H.STORE_NM        AS STORE_NM /*대상 점포 명*/
     , B.BILL_CHRG_CD /*비용 부담 부서*/
     , B.BILL_DEPT_CD /*정산 부서*/
     , A.CHNL_SEND_CNT
     , NULL       AS CHNL_SEND_CNT_OVER_SUM /*발송 건수 누적합*/
     , E.CHNL_UNIT_PRICE AS CHNL_UNIT_PRICE /*발송단가 기본료(원)*/
     , CASE WHEN H.DSFRC_CODE = '20' THEN E.CHNL_UNIT_FEE 
                                     ELSE NULL 
                                     END AS CHNL_UNIT_FEE /*발송단가 수수료(원)*/
     , CASE WHEN H.DSFRC_CODE = '20' THEN E.CHNL_UNIT_PRICE_SH 
                                     ELSE E.CHNL_UNIT_PRICE 
                                     END AS CHNL_UNIT_PRICE_SH /*발송단가*/
     , NULL       AS APRV_DATE
     , NULL       AS PROMOTION_ID
     , NULL       AS PROMOTION_NM
     , NULL       AS RPLAN_GP
     , NULL       AS PROM_TYPE
     , NULL       AS PROM_DESC
     , NULL       AS PROM_SEND_CNT
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
   AND A.CHNL_CD = F1.VAL10 /*전환채널1*/
   AND E.CHNG_CHNL_YN = 'Y'
   AND E1.CHNL_TYPE_CD = F1.LOOKUP_CODE
       LEFT OUTER JOIN ${jdbc.QuadMax.SchemaName}t_lookup_values F2
    ON F2.LOOKUP_TYPE ='CHANNEL_TYPE'
   AND A.CHNL_CD = F2.VAL10 /*전환채널2*/
   AND E.CHNG_CHNL_YN = 'Y'
   AND E2.CHNL_TYPE_CD = F2.LOOKUP_CODE
       INNER JOIN ${jdbc.QuadMax.SchemaName}t_camp_bill_shop G
    ON A.CAMP_ID = G.CAMP_ID
       INNER JOIN ${jdbc.QuadMaxMart.SchemaName}i_cdw_cms_cdw_ria_smt100tm H
    ON G.SHOP_CD = H.STORECD
 WHERE 1=1
   AND A.CHNL_CD <![CDATA[<>]]> 'PUSH' /*고정조건 PUSH 제외 - 2023.01.27 추가*/
   AND S1.ORDER_DATE BETWEEN @@구매기간@@ [AND S3.BRAND_CD IN @@구매브랜드_SSG@@] 
  [AND S1.SHOP_CD IN @@매장_C@@] /*안녕하세요*/ 
  [AND moon in '2'] 
  [AND moon2 =2]
   AND ((E.CHNG_CHNL_YN IS NULL AND A.CHNL_CD = F.VAL10)
    OR E.CHNG_CHNL_YN ='Y'
   AND (F1.VAL10 IS NOT NULL OR F2.VAL10 IS NOT NULL) ) /*고정조건*/
UNION ALL
/*테스트 및 참조발송(이상치 ONLY) 프로모션 적용 안함, 없어야 정상*/
SELECT A.CHNL_SEND_DATE  AS CHNL_SEND_DATE /*발송일*/
     , B.CAMP_ID  AS CAMP_ID /*캠페인 ID*/
     , B.CAMP_NAME       AS CAMP_NAME /*캠페인 명*/
     , B.BRAND_CD        AS BRAND_CD /*브랜드명*/
     , B.REG_DEPT_ID     AS REG_DEPT_ID
     , B.REG_EMP_ID      AS REG_EMP_ID /*담당자 ID*/
     , F.CHNL_NAME       AS CHNL_NAME /*발송채널 ID*/
     , H.DSFRC_CODE /*직가구분*/
     , G.SHOP_CD  AS SHOP_CD /*대상 점포 코드*/
     , H.STORE_NM        AS STORE_NM /*대상 점포 명*/
     , B.BILL_CHRG_CD /*비용 부담 부서*/
     , B.BILL_DEPT_CD /*정산 부서 AND*/
     , A.CHNL_SEND_CNT
     , NULL       AS CHNL_SEND_CNT_OVER_SUM /*발송 건수 누적합*/
     , F.CHNL_UNIT_PRICE AS CHNL_UNIT_PRICE /*발송단가 기본료(원)*/
     , CASE WHEN H.DSFRC_CODE = '20' THEN F.CHNL_UNIT_FEE 
                                     ELSE NULL 
                                     END AS CHNL_UNIT_FEE /*발송단가 수수료(원)*/
     , CASE WHEN H.DSFRC_CODE = '20' THEN F.CHNL_UNIT_PRICE_SH 
                                     ELSE F.CHNL_UNIT_PRICE 
                                     END AS CHNL_UNIT_PRICE_SH /*발송단가*/
     , NULL       AS APRV_DATE
     , NULL       AS PROMOTION_ID
     , NULL       AS PROMOTION_NM
     , NULL       AS RPLAN_GP
     , NULL       AS PROM_TYPE
     , NULL       AS PROM_DESC
     , NULL       AS PROM_SEND_CNT
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
   AND A.CHNL_CD <![CDATA[<>]]> 'PUSH' /*고정조건 PUSH 제외 - 2023.01.27 추가*/
 ORDER BY CHNL_SEND_DATE
     , CAMP_ID
     , SHOP_CD
