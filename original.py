import re
import sys
#<회사 양식 SQL 정렬하는 프로그램>
#SQL문 SELECT,WHERE,FROM,GRUOP BY ,HAVING ,ORDER BY 등으로 구분하여 저장
def extract_sql_clauses(query: str):

    #쿼리 줄 바꿈 제거.
    query = remove_line_breaks(query)

    #추가 : 기존 분할은 서브쿼리의 경우 분할시 정확한 매칭이 안됬는데, 서브쿼리를 치환하는 함수 사용하여 처리.
    query,moon_test = test_moon(query)

    #()안에 FROM 하나만 있을 경우 치환 -> 문장 구문 split시 from 절을 인식하는데 함수에 FROM절 예외처리.
    query = kk_test_from(query)

    # SQL 키워드 패턴 정의 (순서대로 구분하기 위해 그룹화)
    pattern = re.compile(
        r"(?P<select>SELECT\s+.*?)(?=\s+FROM|\Z)|"   # SELECT 절
        r"(?P<from>FROM\s+.*?)(?=\s+WHERE|\s+GROUP BY|\s+HAVING|\s+ORDER BY|\Z)|"  # FROM 절
        r"(?P<where>WHERE\s+.*?)(?=\s+GROUP BY|\s+HAVING|\s+ORDER BY|\Z)|"  # WHERE 절
        r"(?P<group_by>GROUP BY\s+.*?)(?=\s+HAVING|\s+ORDER BY|\Z)|"  # GROUP BY 절
        r"(?P<having>HAVING\s+.*?)(?=\s+ORDER BY|\Z)|"  # HAVING 절
        r"(?P<order_by>ORDER BY\s+.*?)(?=\Z)",  # ORDER BY 절
        re.IGNORECASE | re.DOTALL
    )

    # 패턴 매칭 실행
    matches = pattern.finditer(query)

    # 기본값 설정
    clauses = {
        "select": "",
        "from": "",
        "where": "",
        "group_by": "",
        "having": "",
        "order_by": ""
    }

    # 매칭된 절을 딕셔너리에 저장
    for match in matches:
        for key in clauses.keys():
            if match.group(key):
                clauses[key] = match.group(key).strip()


    # 치환된 서브쿼리 복원
    for key, clause in clauses.items():
        for i, subquery in enumerate(moon_test):
            placeholder = f"MOON_SUBQUERY{i}"
            if placeholder in clause:
                #clauses[key] = clause.replace(placeholder, subquery)
                clause = clause.replace(placeholder, subquery) #20250627수정
        clauses[key] = clause
    
    return clauses

#구분 완료된 딕셔너리중, SELECT절을 가져와 정렬 진행행
def format_select(clauses: dict, select_end_pos: int):
    select_clause = clauses.get("select", "")
    select_end_pos -= 1  # T 정렬 위치 보정

    # 괄호 안 쉼표 임시 치환
    inside_parentheses = math_check(select_clause)
    column_list = [col.strip() for col in inside_parentheses.split(",")]
    column_list = [col.replace('@', ',') for col in column_list]

    # 첫 번째 컬럼은 같은 줄 유지
    formatted_columns = [column_list[0]]


    # 두 번째 컬럼부터 `T` 위치에 맞춰 정렬
    for col in column_list[1:]:
        if re.search(r'\bCASE\b', col, re.IGNORECASE):
            col = case_for_sorted(' ' * select_end_pos + ', ' + col)
            formatted_columns.append(col)
            continue
        formatted_columns.append(f"{' ' * select_end_pos}, {col}")

    # 정렬된 SELECT 절 조합
    formatted_select = "\n".join(formatted_columns)

    # AS 정렬 처리 시작
    lines = formatted_select.splitlines()

    

    as_lengths = []

    for line in lines:

        # 'CASE'가 단어로 포함되어 있으면 0 저장
        if re.search(r'\bCASE\b', line, re.IGNORECASE):
            as_lengths.append(0)
            continue

        # 문장 가장 오른쪽에 있는 AS를 찾기 위해, 역방향 검색
        matches = re.finditer(r'\bAS\b', line, re.IGNORECASE)
        last_as = None
        for match in matches:
            last_as = match.start()

        as_lengths.append(last_as if last_as is not None else 0)


    if as_lengths:
        max_len = max(as_lengths)
        
        avg_len = int(max_len * 3 / 4)

        aligned_lines = []
        for line in lines:
            
             # CASE가 있는 줄은 그냥 추가
            if re.search(r'\bCASE\b', line, re.IGNORECASE):            
                aligned_lines.append(line)
                continue

            # 가장 오른쪽에 있는 AS 위치를 찾은 후 그에 맞게 정렬
            matches = re.finditer(r'\bAS\b', line, re.IGNORECASE)
            last_as = None
            for match in matches:
                last_as = match.start()

            if last_as is not None:
                 # avg_len 또는 max_len 기준으로 정렬
                if last_as < avg_len:
                    pad_len = avg_len - last_as
                    line = line[:last_as] + ' ' * pad_len + line[last_as:]
                elif last_as < max_len:
                    pad_len = max_len - last_as
                    line = line[:last_as] + ' ' * pad_len + line[last_as:]
            aligned_lines.append(line)

        formatted_select = "\n".join(aligned_lines)

        # 대소문자 구분 없이 'ASㅏ'를 'AS'로 변환
        formatted_select = re.sub(r'ASㅏ', 'AS', formatted_select, flags=re.IGNORECASE)


    #실행 순서 차일로 괄호안의 @치환작업 마지막으로 수정     
    #formatted_select=formatted_select.replace("@",' , ')
    return formatted_select


#FROM절 정렬 + CASE문 예외처리
def format_from (clauses: dict,select_end_pos:int):
    from_clause = clauses.get("from", "")

    # `FROM` 키워드가 저장된 `T` 위치에서 시작하도록 설정
    from_end_pos = select_end_pos-len("FROM")
    formatted_from = "\n" +" " * (from_end_pos) + from_clause


    # JOIN 위치 저장 (select 문 위치 +1 )
    join_indent = " " * (select_end_pos + 1)  

    # 'ON', `OR`, `AND` 위치 저장
    on_or_cnt = (select_end_pos )  -len("ON")
    and_cnt = (select_end_pos )  -len("and")

    # JOIN 사용시 줄 바꿈 및 공백 정렬
    join_pattern = re.sub(r"\s*\b(INNER|LEFT|RIGHT|FULL|CROSS)\b", rf"\n{' ' * (select_end_pos + 1)}\1", formatted_from, flags=re.IGNORECASE)


    #함수추가 : 줄바꿈 정렬된 문자열의 괄호안에 and or 조건이 있다면 해당 괄호는 치환처리    
    join_pattern = re.sub(r'\((.*?)\)', lambda m: f"({re.sub(r'\bAND\b', '&&&&', re.sub(r'\bOR\b', '||||', m.group(1), flags=re.IGNORECASE), flags=re.IGNORECASE)})", join_pattern)



    # ON/OR/AND 앞에서 줄바꿈 후 공백 추가
    join_pattern = re.sub(r"\s*\b(ON|OR)\b\s*", rf"\n{' ' * on_or_cnt}\1 ", join_pattern, flags=re.IGNORECASE)
    join_pattern = re.sub(r"\s*\bAND\b\s*", rf"\n{' ' * and_cnt}AND ", join_pattern, flags=re.IGNORECASE)

    

    #치환된 괄호속 AND,OR 를  롤백
    join_pattern = join_pattern.replace('&&&&','AND').replace('||||','OR')

    #BETWEEN 정렬용 함수 실행
    join_pattern = between_sorted(join_pattern)

    join_pattern = process_case_lines(join_pattern,select_end_pos-1)
    return join_pattern


#WHERE 정렬 함수 + case문 예외처리
def format_where (clauses: dict,select_end_pos:int):
    where_clause = clauses.get("where", "")
    
    # `WHERE` 시작 위치 저장
    where_end_pos = select_end_pos-len("WHERE")

    # `OR`, `AND` 취이 조정
    or_cnt = (select_end_pos )  -len("OR")
    and_cnt = (select_end_pos )  -len("and")

    where_pattern = re.sub(r"\s*\bWHERE\b", rf"\n{' ' * where_end_pos}WHERE", where_clause, flags=re.IGNORECASE)
    
    #함수추가 : 줄바꿈 정렬된 문자열의 괄호안에 and or 조건이 있다면 해당 괄호는 치환  
    where_pattern = re.sub(r'\((.*?)\)', lambda m: f"({re.sub(r'\bAND\b', '&&&&', re.sub(r'\bOR\b', '||||', m.group(1), flags=re.IGNORECASE), flags=re.IGNORECASE)})", where_pattern)

    #BETWEEN 사용하는 AND 도 처리
    where_pattern = re.sub(r'(\bBETWEEN\b[^\s]+)\s+AND', r'\1 &&&&', where_pattern, count=1)

    # ON/OR/AND 앞에서 줄바꿈 후 공백 추가
    where_pattern = re.sub(r"\s*\bOR\b\s*", rf"\n{' ' * or_cnt}OR ", where_pattern, flags=re.IGNORECASE)    
    where_pattern = re.sub(r"\s*\bAND\b\s*", rf"\n{' ' * and_cnt}AND ", where_pattern, flags=re.IGNORECASE)

    # 여기에서 네 가지 경우 ([AND, [OR, [and, [or]을 처리
    where_pattern = re.sub(r"\[\s*AND\b", rf"\n{' ' * (or_cnt-2)}[AND", where_pattern, flags=re.IGNORECASE)
    where_pattern = re.sub(r"\[\s*OR\b", rf"\n{' ' * (or_cnt-2)}[OR", where_pattern, flags=re.IGNORECASE)



    # 2. 나머지 OR, AND는 원래대로 처리 (중복되거나 잘못된 부분 처리)
   # where_pattern = re.sub(r"\s*\bOR\b\s*(?!\[)", rf"\n{' ' * or_cnt}OR ", where_pattern, flags=re.IGNORECASE)
    #where_pattern = re.sub(r"\s*\bAND\b\s*(?!\[)", rf"\n{' ' * and_cnt}AND ", where_pattern, flags=re.IGNORECASE)
    
    
    #치환된 괄호속 AND,OR 를  롤백
    where_pattern = where_pattern.replace('&&&&','AND').replace('||||','OR')

    #BETWEEN정렬용 함수 실행
    where_pattern = between_sorted(where_pattern)

    #CASE 문 정렬 함수 적용
    where_pattern = process_case_lines(where_pattern,select_end_pos-2)
    

    return where_pattern

# GROUP BY 정렬함수 + CASE문 예외처리
def format_groupby (clauses: dict,select_end_pos:int):
    groupby_clause = clauses.get("group_by", "")

    if not groupby_clause:
        return ""  
    
    # `WHERE` 시작 위치 조정
    groupby_end_pos = select_end_pos-len("GROUP")



    #GRUOP BY 는 , 를 기준으로 split 적용
    gruopby_pattern = re.sub(r"\s*\bGROUP BY\b", rf"\n{' ' * groupby_end_pos}GROUP BY", groupby_clause, flags=re.IGNORECASE)

    #함수를 사용한 () 안에 , 를 치환하는 함수 (','로 split하기 위해 치환)
    inside_parentheses = math_check(groupby_clause)

    #','기준으로 split
    gruopby_pattern = [col.strip() for col in inside_parentheses.split(",")]

    #맨 처음 값은 , 제외(줄바꿈 +공백)
    first_columns = ['\n'+" "*groupby_end_pos+gruopby_pattern[0].strip()]  # 첫 번째 컬럼은 쉼표 없이 추가

    #두 번째 부터 줄바꿈 +공백 +, 추가
    for col in gruopby_pattern[1:]:

        #split한 컬럼에 CASE 문이 존재하면,
        if re.search(r'\bCASE\b', col, re.IGNORECASE):
            col = case_for_sorted(' '* (select_end_pos-1)+ ', ' + col)
            first_columns.append(col) 

        else:
            first_columns.append(f"{' ' * (select_end_pos-1)}, {col.strip()}")
        
    
    #모든 값 조인
    formatted_gruopby ="\n".join(first_columns)

    # `@`를 다시 치환
    formatted_gruopby = formatted_gruopby.replace('@', ',') 

    return formatted_gruopby

# HAVING 정렬 함수 + CASE문 예외처리
def format_having (clauses: dict,select_end_pos:int):
    having_clause = clauses.get("having", "")
    
    
    # `WHERE` 시작 위치 조정
    having_end_pos = select_end_pos-len("HAVING")

    # `ON`, `OR`, `AND` 정렬 기준 설정
    on_or_cnt = (select_end_pos )  -len("on")
    and_cnt = (select_end_pos )  -len("and")


    having_pattern = re.sub(r"\s*\bHAVING\b", rf"\n{' ' * having_end_pos}HAVING", having_clause, flags=re.IGNORECASE)

    #함수추가 : 줄바꿈 정렬된 문자열의 괄호안에 and or 조건이 있다면 해당 괄호는 치환처리    
    having_pattern = re.sub(r'\((.*?)\)', lambda m: f"({re.sub(r'\bAND\b', '&&&&', re.sub(r'\bOR\b', '||||', m.group(1), flags=re.IGNORECASE), flags=re.IGNORECASE)})", having_pattern)
         
    # ON/OR/AND 앞에서 줄바꿈 후 공백 추가
    having_pattern = re.sub(r"\s*\bOR\b\s*", rf"\n{' ' * on_or_cnt}OR ", having_pattern, flags=re.IGNORECASE)
    having_pattern = re.sub(r"\s*\bAND\b\s*", rf"\n{' ' * and_cnt}AND ", having_pattern, flags=re.IGNORECASE)

    #치환된 괄호속 AND,OR 를  롤백
    having_pattern = having_pattern.replace('&&&&','AND').replace('||||','OR')

    #BETWEEN 사용하는 AND 도 처리
    having_pattern = between_sorted(having_pattern)

    #CASE 문 정렬 함수 적용
    having_pattern = process_case_lines(having_pattern,select_end_pos-2)


    return having_pattern


# ORDER BY 정렬함수 
def format_orderby (clauses: dict,select_end_pos:int):
    orderby_clause = clauses.get("order_by", "")

    # order_by가 없으면 빈 문자열 반환
    if not orderby_clause:
        return ""  
    
    # `ORDER' 시작 위치 조정
    orderby_end_pos = select_end_pos-len("ORDER")

   #함수를 사용한 () 안에 , 를 치환하는 함수 (','로 split하기 위해 치환)
    inside_parentheses = math_check(orderby_clause)

    #','기준으로 split
    orderby_pattern = [col.strip() for col in inside_parentheses.split(",")]

    #맨 처음 값은 , 제외(줄바꿈 +공백)
    first_columns = ['\n'+" "*orderby_end_pos+orderby_pattern[0].strip()]  # 첫 번째 컬럼은 쉼표 없이 추가

    #두 번째 부터 줄바꿈 +공백 +, 추가
    for col in orderby_pattern[1:]:

        #split한 컬럼에 CASE 문이 존재하면,
        if re.search(r'\bCASE\b', col, re.IGNORECASE):
            col = case_for_sorted(' '* (select_end_pos-1)+ ', ' + col)
            first_columns.append(col) 

        else:
            first_columns.append(f"{' ' * (select_end_pos-1)}, {col.strip()}")
            
    
    #모든 값 조인
    formatted_orderby ="\n".join(first_columns)

    # `@`를 다시 치환
    formatted_orderby = formatted_orderby.replace('@', ',') 


    return formatted_orderby


#정렬 대분류 끝
#-----------------------#
#CASE문 예외 처리 시작
#괄호안의 WHEN,THEN,ELSE,END를 치환하는 함수
def replace_when_then_else_end(sql):
    stack = []  # 괄호의 위치를 저장할 스택
    pairs = []  # 괄호 쌍을 저장할 리스트
    modified_sql = list(sql)  # 문자열을 리스트로 변환

    # 모든 괄호의 위치를 찾음
    for i, char in enumerate(sql):
        if char == '(':
            stack.append(i)  # 여는 괄호 위치 저장
        elif char == ')':
            if stack:
                start = stack.pop()  # 가장 안쪽 여는 괄호부터 처리
                pairs.append((start, i))  # 여는 괄호와 닫는 괄호의 위치 저장

    #괄호를 못 찾을 경우, 리턴
    if len(pairs) == 0:
        return sql  

    # 괄호 쌍을 **오른쪽에서 왼쪽으로(가장 바깥쪽부터)** 처리
    for idx, (start, end) in enumerate(reversed(pairs)):
        inside_sql = "".join(modified_sql[start + 1:end])  # 괄호 내부 문자열 추출

        # 내부의 WHEN, THEN, ELSE, END에 임시 문자 추가
        inside_sql = re.sub(r'\bWHEN\b', 'EXCLUDE_WHEN', inside_sql,flags=re.IGNORECASE)
        inside_sql = re.sub(r'\bTHEN\b', 'EXCLUDE_THEN', inside_sql,flags=re.IGNORECASE)
        inside_sql = re.sub(r'\bELSE\b', 'EXCLUDE_ELSE', inside_sql,flags=re.IGNORECASE)
        inside_sql = re.sub(r'\bEND\b', 'EXCLUDE_END', inside_sql,flags=re.IGNORECASE)

        # 변경된 내용을 적용
        modified_sql[start + 1:end] = list(inside_sql)

    join_sql = "".join(modified_sql)
    full_sql = first_replace(join_sql)

    return full_sql

#맨 처음 '(' 의 쌍을 찾는 함수 -> 찾은 후 '('를 <-  ||  ')'를 >-로 치환
def first_replace(sql):
    # 여는 괄호 '(' 위치를 찾기
    open_index = -1
    close_index = -1
    
    # 여는 괄호 위치 찾기
    for i, char in enumerate(sql):
        if char == '(':
            open_index = i
            break  # 첫 번째 여는 괄호만 찾으면 종료
    
    if open_index != -1:
        # 여는 괄호 '('를 <-로 치환
        sql = sql[:open_index] + '<- ' + sql[open_index + 1:]
        
        # 닫는 괄호 ')'를 찾기 (여는 괄호 이후로)
        open_count = 1  # 여는 괄호를 찾았으므로 1로 시작
        for i in range(open_index + 1, len(sql)):
            if sql[i] == '(':
                open_count += 1
            elif sql[i] == ')':
                open_count -= 1
            if open_count == 0:
                close_index = i
                break
        
        if close_index != -1:
            # 닫는 괄호 ')'를 ->로 치환
            sql = sql[:close_index] + ' >-' + sql[close_index + 1:]
    
    return sql

# SQL을 줄 단위로 분리하여, 인자값(keyword)의 위치를 리턴하는 함수.
def find_first_position(sql, keyword):
    
    lines = sql.splitlines()

    # 각 줄에서 keyword의 위치를 찾고 가장 먼저 발견된 위치를 반환
    for line_num, line in enumerate(lines, start=1):  

        # 각 줄에서 keyword가 있는지 확인
        match = re.search(rf'\b{keyword}\b', line)  
        if match:
            return (match.start())
    return 0

#CASE 문 정렬 함수
def case_sorted(sql, cnt):
    try :

        #괄호안의 값을 치환 후 리턴.
        formatted_sql = replace_when_then_else_end(sql)

        # WHEN 개수 세기
        outer_when_positions = [m.start() for m in re.finditer(r'\bWHEN\b', formatted_sql,flags=re.IGNORECASE)]

            
        #WHEN의 갯수가 1개일 떄, THEN의 위치로 ELSE,END 정렬
        if len(outer_when_positions) == 1:
            
            #THEN의 위치값 변수 저장        
            then_position = find_first_position(formatted_sql,"THEN")
            
            #WHEN,THEN -> CNT 조인.
            formatted_sql = re.sub(r'\bWHEN\b', f'WHEN{cnt}', formatted_sql, flags=re.IGNORECASE)
            formatted_sql = re.sub(r'\bTHEN\b', f'THEN{cnt}', formatted_sql, flags=re.IGNORECASE)
            
            #치환 변수를 고려한 인덱스 재 설정
            indent_then = then_position if cnt == 0 else then_position-3
            
            # ELSE 정렬
            formatted_sql = re.sub(r'\bELSE\b', f'\n{" " * indent_then}ELSE{cnt}', formatted_sql, count=1, flags=re.IGNORECASE)

            # END 정렬
            formatted_sql = re.sub(r'\bEND\b', f'\n{" " * indent_then}END{cnt}', formatted_sql, count=1, flags=re.IGNORECASE)

            return formatted_sql

        else:# WHEN이 여러 개인 경우
            
            #맨 처음 WHEN,THEN의 위치 저장.
            when_position = find_first_position(formatted_sql,"WHEN")
            then_position = find_first_position(formatted_sql,"THEN")

            #맨 처음 반복문은CNT만 ,그 이후는 줄 바꿈 및 CNT추가
            for i, k in enumerate(outer_when_positions):
                if i == 0:
                    # 첫 번째 WHEN에는 cnt만 추가
                    formatted_sql = re.sub(r'\bWHEN\b', f'WHEN{cnt}', formatted_sql, count=1, flags=re.IGNORECASE)
                    
                    #범위에 포함된 TEHN에 cnt 추가
                    formatted_sql = re.sub(r'\bTHEN\b', f'THEN{cnt}', formatted_sql, flags=re.IGNORECASE)

                else:
                    # 이후 WHEN에는 줄바꿈과 공백 추가
                    indent_when = when_position if cnt == 0 else when_position-3
                    formatted_sql = re.sub(r'\bWHEN\b', f'\n{" " * (indent_when)}WHEN{cnt}', formatted_sql, count=1, flags=re.IGNORECASE)                         					                								    

            # ELSE와 END 정렬 -> 임시 whendl 여러개일떄는 when을 기준으로 위치
            indent_then = then_position if cnt == 0 else then_position-3
            formatted_sql = re.sub(r'\bELSE\b', f'\n{" " * indent_when}ELSE{cnt}', formatted_sql, count=1, flags=re.IGNORECASE)
            formatted_sql = re.sub(r'\bEND\b', f'\n{" " * indent_when}END{cnt}', formatted_sql, count=1, flags=re.IGNORECASE)
        
    except Exception as e:
        #return f"CASE문 필터링 부분 에러 발생"
        raise Exception(f"CASE문 필터링 부분 에러 발생(중첩 CASE문의 괄호를 확인하세요)")
        
	
    return formatted_sql

        

#정렬작업 마지막, 치환된 값을 다시 롤백하는 함수
def replace_vactor(sql,cnt):
    #초기화
    formatted_case=sql

    for i in range(cnt):
          formatted_case = formatted_case.replace(f'WHEN{i}', 'WHEN')		
          formatted_case = formatted_case.replace(f'THEN{i}', 'THEN')
          formatted_case = formatted_case.replace(f'ELSE{i}', 'ELSE')
          formatted_case = formatted_case.replace(f'END{i}', 'END')

    #중첩 케이스문 괄호 롤백
    formatted_case = formatted_case.replace('<-', '(')                        
    formatted_case = formatted_case.replace('>-', ')')                        

    #함수나 다른 괄호들 롤백
    formatted_case = formatted_case.replace('ㄱ', '(')
    formatted_case = formatted_case.replace('ㄴ', ')')
    formatted_case = formatted_case.replace('@', ',')


    return formatted_case

 
#CASE문의 외각부터 내각까지 반복적으로 정렬하는 함수.
def case_for_sorted(sql):
    
# 함수 () 처리 - 중첩 CASE 문은 외각부터 내각까지 순서대로 정렬하기 위해 함수의 괄호는 치환
    #함수사용한 괄호(공백) 치환 처리 () -> ㄱ,ㄴ
    #sql = replace_empty_parentheses(sql)

    #함수를 사용한 ,에서 가장 가까운 ()치환 ##, ,->@
    #sql = replace_comma_in_parentheses(sql)

    #함수 인자값이 단일 값인 경우 치환용 함수.
    sql = replace_parentheses_with_conditions(sql) 

    #추가 : 단순 () 사용하여 사칙연산 사용한 경우.(통합)
    sql = replace_parentheses_without_when_then(sql)

    #AS정렬요 마지막 AS 치환 -> AS@
    sql =  re.sub(r'\bAS\b', 'ASㅏ', sql, flags=re.IGNORECASE)

    #CASE문의 위치 저장
    case_positions = [m.start() for m in re.finditer(r'\bCASE\b', sql, re.IGNORECASE)]


    #변수 초기화    	
    final_sql = sql 
	
    #실제 CASE문의 수 만큼 반복문 돌리면서 정렬작업 후, 원문 롤백.
    for i in range(len(case_positions)):
        
        #치환 -> 정렬함수 실행.
        formatted_case = case_sorted(final_sql,i)
   
        		
        # 변경된 WHEN의 값 롤백.
        formatted_case = formatted_case.replace('EXCLUDE_WHEN', 'WHEN')
        formatted_case = formatted_case.replace('EXCLUDE_THEN', 'THEN')
        formatted_case = formatted_case.replace('EXCLUDE_ELSE', 'ELSE')
        formatted_case = formatted_case.replace('EXCLUDE_END', 'END')

        # 최종 SQL에 반영 (부분적으로 업데이트)
        final_sql = formatted_case
            
	#치환 변수 다시 바꾸기.
    final_sql = replace_vactor(final_sql,len(case_positions))	

    return final_sql


#한 줄 정렬.
def remove_line_breaks(input_string):
    return re.sub(r'\s+', ' ', input_string.replace('\r', '')).strip()


##함수사용한 괄호 치환 처리 () -> ㄱ,ㄴ
def replace_empty_parentheses(sql):
    stack = []  # 괄호의 위치를 저장할 스택
    pairs = []  # 괄호 쌍을 저장할 리스트
    modified_sql = list(sql)  # 문자열을 리스트로 변환

    # 모든 괄호의 위치를 찾음
    for i, char in enumerate(sql):
        if char == '(':
            stack.append(i)  # 여는 괄호 위치 저장
        elif char == ')':
            if stack:
                start = stack.pop()  # 가장 안쪽 여는 괄호부터 처리
                pairs.append((start, i))  # 여는 괄호와 닫는 괄호의 위치 저장

    # 괄호를 못 찾을 경우, 리턴
    if len(pairs) == 0:
        return sql  

    # 괄호 쌍을 **오른쪽에서 왼쪽으로(가장 바깥쪽부터)** 처리
    for start, end in pairs:
        inside_sql = "".join(modified_sql[start + 1:end])  # 괄호 내부 문자열 추출

        # 괄호 내부가 비어 있으면, ㄱ,ㄴ으로 치환
        if not inside_sql.strip():  
            modified_sql[start] = 'ㄱ'  # 여는 괄호를 ㄱ로 치환
            modified_sql[end] = 'ㄴ'  # 닫는 괄호를 ㄴ로 치환


    return "".join(modified_sql)


        

#함수를 사용한 ,에서 가장 가까운 ()치환 ##, ,->@
def replace_comma_in_parentheses(sql):
    # ,의 갯수 카운트
    comma_count = sql.count(',')
    
    # 문자열을 리스트로 바꾸어서 수정하기 용이하게 만듦
    modified_sql = list(sql)
    
    # 첫 번째 쉼표는 제외하고 처리하려면 첫 번째 쉼표 위치를 찾음
    start_pos = sql.find(',') + 1  
    
    for _ in range(comma_count):

        # 가장 먼저 나오는 ,의 위치를 찾음
        comma_pos = sql.find(',', start_pos)

        # ,를 기준으로 가장 가까운 괄호 '('와 ')'를 찾음
        open_paren_pos = sql.rfind('(', 0, comma_pos)  # 가장 가까운 왼쪽 여는 괄호 '('
        close_paren_pos = sql.find(')', comma_pos)  # 가장 가까운 오른쪽 닫는 괄호 ')'
        
        # 만약 괄호가 없거나 올바른 위치에 없다면 넘어감
        if open_paren_pos == -1 or close_paren_pos == -1 or open_paren_pos > close_paren_pos:
            break
        

        # ,를 @로 치환
        modified_sql[comma_pos] = '@'
        # ,를 감싸는 괄호를 #으로 치환
        modified_sql[open_paren_pos] = 'ㄱ'
        modified_sql[close_paren_pos] = 'ㄴ'
        

        
        # 수정된 부분을 새로운 문자열로 업데이트
        sql = "".join(modified_sql)
    
    return "".join(modified_sql)


#함수 인자값이 단일 값인 경우 치환용 함수.
def replace_parentheses_with_conditions(sql):
    simple_functions = ['SUM', 'MIN', 'MAX', 'COUNT', 'AVG', 'ABS', 'ROUND', 'LENGTH', 'TRIM','CAST']
    stack = []  # 여는 괄호 위치를 저장할 스택
    pairs = []  # 괄호 쌍을 저장할 리스트
    modified_sql = list(sql)  # 문자열을 리스트로 변환 (수정 용이)

    # 모든 괄호의 위치를 찾음
    for i, char in enumerate(sql):
        if char == '(':
            stack.append(i)  # 여는 괄호 위치 저장
        elif char == ')':
            if stack:
                start = stack.pop()  # 가장 안쪽 여는 괄호부터 처리
                pairs.append((start, i))  # 여는 괄호와 닫는 괄호의 위치 저장

    # 괄호 쌍을 왼쪽에서 오른쪽으로 처리
    for start, end in pairs:
        inside_sql = "".join(modified_sql[start + 1:end])  # 괄호 내부 문자열 추출

        # 괄호 앞에 특정 함수가 있다면 괄호 치환
        for func in simple_functions:
            # 괄호 앞에 해당 함수가 있는지 확인
            if sql[(start - len(func))-1:start].strip().upper() == func:
                # 함수 이름이 있을 경우 괄호를 ㄱ()와 ㄴ()로 치환
                modified_sql[start] = 'ㄱ '  # 여는 괄호를 ㄱ로 치환
                modified_sql[end] = ' ㄴ'  # 닫는 괄호를 ㄴ로 치환

    return "".join(modified_sql)

#단순 ( )안에 사칙연산을 사용한 경우 괄호 치환('WHEN'과 'THEN'이 없을 경우 치환)
def replace_parentheses_without_when_then(sql):
    stack = []  # 여는 괄호 위치를 저장할 스택
    pairs = []  # 괄호 쌍을 저장할 리스트
    modified_sql = list(sql)  # 문자열을 리스트로 변환 (수정 용이)

    # 모든 괄호의 위치를 찾음
    for i, char in enumerate(sql):
        if char == '(':
            stack.append(i)  # 여는 괄호 위치 저장
        elif char == ')':
            if stack:
                start = stack.pop()  # 가장 안쪽 여는 괄호부터 처리
                pairs.append((start, i))  # 여는 괄호와 닫는 괄호의 위치 저장

    # 괄호 쌍을 왼쪽에서 오른쪽으로 처리
    for start, end in pairs:
        inside_sql = "".join(modified_sql[start + 1:end])  # 괄호 내부 문자열 추출

        # 괄호 내부에 'WHEN'과 'THEN'이 없을 경우 치환
        if not re.search(r'\bWHEN\b|\bTHEN\b', inside_sql,flags=re.IGNORECASE):
            # 여는 괄호를 ㄱ으로 치환하고, 닫는 괄호를 ㄴ으로 치환
            modified_sql[start] = 'ㄱ'  # 여는 괄호를 ㄱ로 치환
            modified_sql[end] = 'ㄴ'  # 닫는 괄호를 ㄴ으로 치환

    return "".join(modified_sql)

#CASE 문 처리 끝
############


#함수를 사용한 ,에서 가장 가까운 () 안에 , -> @로 치환 (select절 ,group by  split 사용)
def math_check(sql):
    # 문자열을 리스트로 변환하여 수정 용이하게 만듦
    modified_sql = list(sql)

    # 스택을 사용하여 괄호 쌍 찾기
    stack = []  # 여는 괄호 위치를 저장할 스택
    pairs = []  # 괄호 쌍을 저장할 리스트

    # 괄호의 짝을 찾는 과정
    for i, char in enumerate(sql):
        if char == '(':
            stack.append(i)  # 여는 괄호 위치 저장
        elif char == ')':
            if stack:
                start = stack.pop()  # 가장 안쪽 여는 괄호부터 처리
                pairs.append((start, i))  # 여는 괄호와 닫는 괄호의 위치 저장

    # 괄호 쌍을 뒤에서부터 처리 (가장 안쪽부터 처리)
    for start, end in reversed(pairs):
        inside_sql = "".join(modified_sql[start + 1:end])  # 괄호 내부 문자열 추출

        # 괄호 내부에 쉼표가 있으면, 가장 안쪽의 쉼표부터 @로 치환
        if ',' in inside_sql:
            # 쉼표를 @로 치환 (가장 안쪽 쉼표만)
            inside_sql = inside_sql.replace(',', '@')
            modified_sql[start + 1:end] = inside_sql  # 수정된 부분 반영

    return "".join(modified_sql)


#########서브쿼리 작업 시작

#test1 작업 순서:
#1. 모든 괄호의 쌍을 찾는다
#2. 가장 바깥의 괄호의 쌍을 찾는다.
#3. 해당 괄호안에 SELECT이 있는지 필터링
#4. 서브쿼리가 아닌 () 치환 
#5. 맨 처음 시작이 (SELECT ~),( SELECT~)로 시작하지 않는 괄호 치환
#6. 서브쿼리의 최 외각 괄호 치환 및 내용 치환
#7. 4번 내용 롤백.


def test1(sql):
    try:
        stack = []
        pairs = []
        modified_sql = list(sql)
        depths = [0] * len(sql)
        replaced_selects = []  # 치환된 SELECT 구문 저장 리스트

        # 괄호 위치와 깊이 계산
        for i, char in enumerate(sql):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    start = stack.pop()
                    pairs.append((start, i))
                    for j in range(start, i + 1):
                        depths[j] += 1

        if len(pairs) == 0:
            return sql, []  # 괄호 없을 경우 원본 그대로 반환

        # 가장 바깥 괄호만 추출
        outer_pairs = [(start, end) for start, end in pairs if depths[start] == 1 and depths[end] == 1]

        k_cnt = 0
        for start, end in reversed(outer_pairs):  # 역순 처리
            inside_sql = "".join(modified_sql[start + 1:end])

            #괄호안에 SELECT 있는경우.
            if re.search(r'\bSELECT\b', inside_sql.strip(), re.IGNORECASE):

                #서브쿼리 아닌것 임시 치환
                modified_sql = list(kk_test(modified_sql))

                ##서브쿼리의 시작이 ( SELECT)로 시작하지 않는 부분 괄호 치환 
                if not re.match(r'\s*select', "".join(modified_sql[start + 1:]), re.IGNORECASE):
                        
                        modified_sql[start] = '<~'
                        modified_sql[end] = '~>'

                        # start에서 end까지의 구간에서 쉼표가 있으면 @로 치환
                        segment = "".join(modified_sql[start + 1:end])  # start와 end 사이의 문자열 추출
                        if ',' in segment:  # 쉼표가 있으면
                            segment = segment.replace(',', '@')  # 쉼표를 @로 치환

                        # 치환된 값을 modified_sql에 반영
                        modified_sql[start + 1:end] = list(segment)

                        

                        # 내부 괄호 기준으로 실제 인덱스 계산
                        relative_first = "".join(modified_sql[start + 1:]).find('(')
                        relative_last = inside_sql.rfind(')')

                        # 전체 문자열 기준 인덱스로 보정
                        first_paren_index = start + 1 + relative_first
                        last_paren_index = start + 1 + relative_last

                        #실제 서브쿼리 부분 인덱스 조절 및 치환
                        inside_sql = "".join(modified_sql[first_paren_index + 1:last_paren_index])

                        replaced_selects.append(inside_sql)  # 치환 대상 저장
                        modified_sql[first_paren_index] = '<:'
                        modified_sql[last_paren_index] = f' {k_cnt}:>'
                        modified_sql[first_paren_index + 1:last_paren_index] = list(f"MOON{k_cnt}")
                        k_cnt += 1

                        continue


                #서브쿼리의 첫 시작이 select 으로 시작하는 경우
                else :

                    replaced_selects.append(inside_sql)  # 치환 대상 저장

                    #해당 괄호 치환
                    modified_sql[start] = '<:'
                    modified_sql[end] = f' {k_cnt}:>'
                    modified_sql[start + 1:end] = list(f"MOON{k_cnt}")
                    k_cnt += 1

                    continue  
                    

        
        #모든 괄호에서 select 없는 부분 치환했던거 롤백                

        modified_sql = "".join(modified_sql).replace('ㄱ','(').replace('ㄴ',')')

        # replaced_selects 리스트에 대해서도 "<-"와 "->"를 "("와 ")"로 교체
        replaced_selects = [sql.replace("ㄱ", "(").replace("ㄴ", ")") for sql in replaced_selects]


    except Exception as e:
        raise Exception(f"SQL 서브쿼리 치환작업 중 에러 발생")
        

    return modified_sql, replaced_selects




#치환된 값들을 정렬후 롤백.
def process_subqueries(sql_query, A):
    try:
        select_len = len("SELECT")
        w = sql_query  # 처음의 SQL 쿼리
        first_select_list =[]
        # 서브쿼리 처리 반복문
        for idx, subquery in enumerate(A):  # A에는 서브쿼리의 내용이 치환되서 저장.
            
            #쿼리를 구문별로 나누는 함수.
            subquery_clauses = extract_sql_clauses(subquery)    
        
            #라인 단위의 치환된 sql 위치 파악 . -1은 치환시 증가하는 값 고려
            first_select_location = (find_first_position(w, f"MOON{idx}")-1)

            first_select_list.append(first_select_location)
            # 서브쿼리에서 각 SQL 구성 요소 포맷하기
            k_w = sql_concat(subquery_clauses,select_len,first_select_location)
            
            # 서브쿼리 부분을 대체 문자로 치환
            w = re.sub(f"MOON{idx}", f"{k_w}",w)

    except Exception as e:
        raise Exception(f"SQL 서브쿼리 정렬 작업 중 에러") 
        

    return w,first_select_list


# 괄호의 앞뒤로 공백 추가. 
def add_space_around_parentheses(query: str) -> str:
     # 괄호 앞에 공백이 없으면 공백 추가
    query = re.sub(r'(?<=\w)(?=\()', r' ', query)  # 함수명과 여는 괄호 사이에 공백 추가
    
    # 괄호 뒤에 공백이 없으면 공백 추가
    query = re.sub(r'(?<=\))(?=\S)', r' ', query)  # 닫는 괄호와 그 뒤의 문자 사이에 공백 추가
    return query

#실제 작동하는 함수(호출용).
def moon_gogo(sql_query):
    #맨 처음 ()앞뒤로 공백 추가하는 함수.
    sql_query = add_space_around_parentheses(sql_query)

    #괄호의 , 를 @로 치환하는 함수 (중첩경우 때문에 미리 한 번 실행)
    #sql_query = math_check(sql_query)
    
    #줄 바꿈 제거하는 함수
    sql_query = remove_line_breaks(sql_query)

    #/**/ 안의 내용을 치환하는 함수.
    sql_query = replace_in_comment(sql_query)

    #문자의 첫 시작이 /**/ 인경우 예외처리
    a_moon=''
    comment, cleaned_sql =extract_comment_and_clean_sql(sql_query,'SELECT')
    if comment is not None:
        a_moon = comment
        #치환 완료된 쿼리 저장
        sql_query = cleaned_sql
    else:
        #치환 완료된 쿼리 저장
        sql_query = cleaned_sql
    
#################  
#처음 정렬은 하드코딩
    #최외각의 괄호를 제외한 내각의 괄호 치환(서브쿼리 치환)
    sql_query,A=test1(sql_query)

    #처음 실행하는 쿼리 정렬.
    first_select_location = find_first_position(sql_query,"SELECT")
    select_len = len("SELECT")
    clauses = extract_sql_clauses(sql_query)
    w = sql_concat(clauses,select_len,first_select_location)
    

    #치환된 서브쿼리를 정렬후 롤백
    final_sql,select_locatoin = process_subqueries(w, A)
    
    #서브쿼리 괄호 정렬용
    for i in range(len(select_locatoin)):       
        final_sql = final_sql.replace(f'{i}:>', '\n'+' '*(select_locatoin[i]-1)+':>')    
    a2 = final_sql    
################# 

    #남은 서브쿼리의 갯수 카운트
    select_cnt =   len(re.findall(r'(?i)\(\s*select', final_sql))
    
    #남은 서브쿼리 반복문 실행
    for i in range(select_cnt):
        
        #최외각의 괄호를 제외한 내각의 괄호 치환(서브쿼리 치환)
        sql_query,A=test1(final_sql)

        #치환된 서브쿼리를 정렬후 롤백
        final_sql,select_locatoin = process_subqueries(sql_query, A)

        #줄 정렬을 위해, 변경
        for i in range(len(select_locatoin)):       
            final_sql = final_sql.replace(f'{i}:>', '\n'+' '*(select_locatoin[i]-1)+':>')
        

    #최종적으로 '<:' -> '('  ':>' ->')'  치환
    #추가 : 여러 서브쿼리 처리시 , '<' -> '<~'로 치환하는 과정에서 인덱스 변화가 생기기 때문에 공백하나 추가
    final_sql = final_sql.replace('<:', '(').replace(':>', ' )')


    #서브쿼리 정렬시 처음시작이 (select~) or ( select ~) 가 아닌경우 치환 후 롤백
    #추가 : 여러 서브쿼리 처리시 , '<' -> '<~'로 치환하는 과정에서 인덱스 변화가 생기기 때문에 공백하나 추가
    final_sql = "".join(final_sql).replace("<~","( ").replace("~>",")") 

    #맨처음이 /**/로시작하는 경우 ,치환값 롤백
    if a_moon !='':
        final_sql = a_moon+'\n'+final_sql

    #/**/ 안의 내용 치환한거 롤백
    final_sql =final_sql.replace("ㅋ",",").replace("ㅌ","(").replace("ㅊ",")") 

    #내장함수안에 FROM 하나있는경우 롤백
    final_sql = final_sql.replace("FRHM","FROM")

    return final_sql


# split된 SQL쿼리들을 조합하는 함수
def sql_concat(clauses,select_len,first_select_location):

    try:
        base_index = select_len + first_select_location

        select_sql = format_select(clauses, base_index)
        from_sql = format_from(clauses, base_index)
        where_sql = format_where(clauses, base_index)
        groupby_sql = format_groupby(clauses, base_index)
        having_sql = format_having(clauses, base_index)
        orderby_sql = format_orderby(clauses, base_index)

        final_sql = select_sql + from_sql + where_sql + groupby_sql + having_sql + orderby_sql
        return final_sql

    except Exception as e:
        raise e
        




#서브쿼리의 최외각의 내용을 치환 -> 맨 처음 SQL 구분 split할 때, 서브쿼리가 있을 경우 split시 정확한 split되지 않음.
def test_moon(sql):
    stack = []  # 괄호의 위치를 저장할 스택
    pairs = []  # 괄호 쌍을 저장할 리스트
    modified_sql = list(sql)  # 문자열을 리스트로 변환

    # 모든 괄호의 위치를 찾음
    for i, char in enumerate(sql):
        if char == '(':
            stack.append(i)  # 여는 괄호 위치 저장
        elif char == ')':
            if stack:
                start = stack.pop()  # 가장 안쪽 여는 괄호부터 처리
                pairs.append((start, i))  # 여는 괄호와 닫는 괄호의 위치 저장
    cnt_test =[]
    k_cnt = 0
    # 괄호를 못 찾을 경우, 리턴
    if len(pairs) == 0:
        return sql,cnt_test
    
 
    # 괄호 쌍을 **오른쪽에서 왼쪽으로(가장 안쪽부터)** 처리
    for idx, (start, end) in enumerate(reversed(pairs)):
        inside_sql = "".join(modified_sql[start + 1:end])  # 괄호 내부 문자열 추출

        # 괄호 안에 SELECT가 있으면 처리
        if "SELECT" in inside_sql.upper():  # 대소문자 구분 없이 SELECT를 찾기
            cnt_test.append(inside_sql)  # 괄호 안의 SELECT 구문을 리스트에 저장        

            modified_sql[start + 1:end] = list(f"MOON_SUBQUERY{k_cnt}")  
            k_cnt+=1
            continue
    # 수정된 SQL을 반환
    join_sql = "".join(modified_sql)

    return join_sql, cnt_test


#서브쿼리 정렬전 ()안에 SELECT 이 있는 ()는 치환 -> 서브쿼리 정렬시, ()를 인식해서 반복문 돌리기 때문에, 서브쿼리가 아닌부분은 치환.
def kk_test(sql):
    stack = []  # 여는 괄호 위치를 저장할 스택
    pairs = []  # 괄호 쌍을 저장할 리스트
    modified_sql = list(sql)  # 문자열을 리스트로 변환 (수정 용이)

    # 모든 괄호의 위치를 찾음
    for i, char in enumerate(sql):
        if char == '(':
            stack.append(i)  # 여는 괄호 위치 저장
        elif char == ')':
            if stack:
                start = stack.pop()  # 가장 안쪽 여는 괄호부터 처리
                pairs.append((start, i))  # 여는 괄호와 닫는 괄호의 위치 저장

    # 괄호 쌍을 왼쪽에서 오른쪽으로 처리
    for start, end in pairs:
        inside_sql = "".join(modified_sql[start + 1:end])  # 괄호 내부 문자열 추출

        # 괄호 내부에 'WHEN'과 'THEN'이 없을 경우 치환
        if not re.search(r'\bSELECT\b', inside_sql,flags=re.IGNORECASE):
            # 여는 괄호를 ㄱ으로 치환하고, 닫는 괄호를 ㄴ으로 치환
            modified_sql[start] = 'ㄱ'  # 여는 괄호를 ㄱ로 치환
            modified_sql[end] = 'ㄴ'  # 닫는 괄호를 ㄴ으로 치환

    return "".join(modified_sql)

# /**/ 안의 , ( ,) 를 각각 ㅋ, ㅌ, ㅊ 로 치환
def replace_in_comment(text):
    
    def replace_match(match):
        comment = match.group(0)
        comment = comment.replace(',', 'ㅋ').replace('(', 'ㅌ').replace(')', 'ㅊ')
        return comment
    
    # /**/ 안의 내용을 찾아서 치환
    pattern = r'/\*.*?\*/'
    result = re.sub(pattern, replace_match, text)
    return result


# BETWEEN 병합 로직
def between_sorted(sql):
    
    lines = sql.splitlines()
    merged_lines = []
    skip_next = False

    for i, line in enumerate(lines):
        if skip_next:
            skip_next = False
            continue

        # 현재 줄에 BETWEEN이 있다면 다음 줄과 합치기
        if re.search(r'\bBETWEEN\b', line, re.IGNORECASE) and i + 1 < len(lines):
            merged_line = line.rstrip() + ' ' + lines[i + 1].lstrip()
            merged_lines.append(merged_line)
            skip_next = True
        else:
            merged_lines.append(line)

    between_pattern = "\n".join(merged_lines)
    return between_pattern


#괄호 안에 SELECT는 없고 FROM이 있는 경우만 FROM을 FRHM으로 치환
def kk_test_from(sql):
    stack = []  # 여는 괄호 위치를 저장할 스택
    pairs = []  # 괄호 쌍을 저장할 리스트
    modified_sql = list(sql)  # 문자열을 리스트로 변환 (수정 용이)

    # 모든 괄호의 위치를 찾음
    for i, char in enumerate(sql):
        if char == '(':
            stack.append(i)  # 여는 괄호 위치 저장
        elif char == ')':
            if stack:
                start = stack.pop()  # 가장 안쪽 여는 괄호부터 처리
                pairs.append((start, i))  # 여는 괄호와 닫는 괄호의 위치 저장

    # 괄호 쌍을 왼쪽에서 오른쪽으로 처리
    for start, end in pairs:
        inside_sql = "".join(modified_sql[start + 1:end])  # 괄호 내부 문자열 추출

        # 괄호 내부에 'SELECT'가 없고 'FROM'이 있을 경우 치환
        if not re.search(r'\bSELECT\b', inside_sql, flags=re.IGNORECASE) and re.search(r'\bFROM\b', inside_sql, flags=re.IGNORECASE):
            # 'FROM'을 FRHM으로 치환 (단어 경계를 이용하여 정확히 'FROM'만 찾음)
            inside_sql = re.sub(r'\bFROM\b', 'FRHM', inside_sql, flags=re.IGNORECASE)
            
            # 치환된 결과로 괄호 내부 수정
            modified_sql[start + 1:end] = list(inside_sql)  # 괄호 안의 내용만 수정

    return "".join(modified_sql)

#UNION 처리
def split_union_query(query):
    # UNION 또는 UNION ALL 분리
    parts = re.split(r'(\s+UNION\s+ALL?\s+|\s+UNION\s+)', query, flags=re.IGNORECASE)
    parts = [part.strip() for part in parts]

    sql_moon = []

    for part in parts:
        if re.match(r'^(UNION|UNION ALL)$', part, flags=re.IGNORECASE):
            sql_moon.append(part)
        else:            
            formatted = moon_gogo(part)
            sql_moon.append(formatted)

    #첫줄에 생기는 줄바꿈 제거
    final = '\n'.join(sql_moon).lstrip('\n')
    return final
        
    


#union여부에 따라 분기처리 (여기가 시작.)
def last_start(sql_query):
    try:
        # #맨 처음 ()앞뒤로 공백 추가하는 함수.
        # sql_query = add_space_around_parentheses(sql_query)

        # #줄 바꿈 제거하는 함수
        # sql_query = remove_line_breaks(sql_query)

        # #/**/ 안의 내용을 치환하는 함수.
        # sql_query= replace_in_comment(sql_query)
        sql_query,commend = replace_comments2(sql_query) 

        #추가 : 대문자로 변경
        sql_query = re.sub(r'\bselect\b', 'SELECT', sql_query, flags=re.IGNORECASE)
        sql_query = re.sub(r'\bfrom\b', 'FROM', sql_query, flags=re.IGNORECASE)
        sql_query = re.sub(r'\bwhere\b', 'WHERE', sql_query, flags=re.IGNORECASE)
        sql_query = re.sub(r'\bgroup by\b', 'GROUP BY', sql_query, flags=re.IGNORECASE)
        sql_query = re.sub(r'\bhaving\b', 'HAVING', sql_query, flags=re.IGNORECASE)
        sql_query = re.sub(r'\border by\b', 'ORDER BY', sql_query, flags=re.IGNORECASE)

        #CASE 문 대문자로 변경 
        sql_query = re.sub(r'\bwhen\b', 'WHEN', sql_query, flags=re.IGNORECASE)
        sql_query = re.sub(r'\bthen\b', 'THEN', sql_query, flags=re.IGNORECASE)
        sql_query = re.sub(r'\belse\b', 'ELSE', sql_query, flags=re.IGNORECASE)
        sql_query = re.sub(r'\bend\b', 'END', sql_query, flags=re.IGNORECASE)
        sql_query = re.sub(r'\bcase\b', 'CASE', sql_query, flags=re.IGNORECASE)
        

        # # (1) 서브쿼리 치환
        AA, subquery_placeholders = test1(sql_query)
        for i in subquery_placeholders:
        #서브쿼리안에 UNION ,UNION ALL 있을경우 예외처리.
            if re.search(r'\bUNION\b( ALL)?', i, flags=re.IGNORECASE):
                raise Exception("서브쿼리 안의 UNION은 현재 지원하지 않습니다.")        

        # (2) CTE 처리
        if re.search(r"\s*WITH\s+\w+\s+AS\s*\(", sql_query, re.IGNORECASE):
            
            #줄 바꿈 정렬
            sql_query = remove_line_breaks(sql_query)
               
            #CTE를 3개로 분리하는 로직 (CTE치환값(메인쿼리제외),치환된 값, 메인쿼리)
            with_query, sub, rest_of_query = CTE_REPLACE(sql_query)

            # CTE 부분의 각 쿼리 처리
            for idx , query in enumerate((sub)):
                
                # CTE - UNION 유무 체크
                if re.search(r'\bUNION\b( ALL)?', query, flags=re.IGNORECASE):                
                    final_sql = split_union_query(query)
                else :                            
                    final_sql = moon_gogo(query)
                
                # 치환된 값을 정렬 후 롤백 (with_query에 치환된 SQL을 반영)
                with_query = with_query.replace(f"CTE{idx}", final_sql)
            
            # CTE 이후의 쿼리 - UNION 유무 체크
            if re.search(r'\bUNION\b( ALL)?', rest_of_query, flags=re.IGNORECASE):            
                final_sql = split_union_query(rest_of_query)
            else :                        
                final_sql = moon_gogo(rest_of_query)

            # CTE와 나머지 쿼리 결합
            final_sql = "\n".join([with_query, final_sql])

        else:
            # CTE가 없으면 기존 쿼리 처리
            # UNION 유무 체크
            if re.search(r'\bUNION\b( ALL)?', sql_query, flags=re.IGNORECASE):            
                final_sql = split_union_query(sql_query)
            else :            
                final_sql = moon_gogo(sql_query)

        # sql,commend = replace_comments2(final_sql)  

        #치환된 /**/안의 내용 롤백(추가)        
        for i, comment in enumerate(commend):
           final_sql = final_sql.replace(f'/*commend_{i}*/',"/*"+comment+"*/")
           
        



    except Exception as e:                           
        raise e                                  

    
    return final_sql.strip()

#맨 처음 SELECT 이 시작하기 전에 쿼리앞에 /**/주석 있다면 치환 
def extract_comment_and_clean_sql(sql,keyword):
    # 대소문자 구분 없이 SELECT 위치 찾기
    select_match = re.search(rf'\b{keyword}\b', sql, re.IGNORECASE)
    
    # 기본 설정
    comment = None
    cleaned_sql = sql.strip()

    if select_match:
        select_start = select_match.start()

        # SELECT 앞에 /** */ 주석이 있는지 확인
        comment_match = re.search(r'/\*.*?\*/', sql[:select_start], re.DOTALL)
        if comment_match:
            comment = comment_match.group(0)
            # 주석 제거하고 공백 제거
            cleaned_sql = (sql[:comment_match.start()] + sql[comment_match.end():]).strip()

    return comment, cleaned_sql

#추가 : CTE 절 예외 처리
def CTE_REPLACE(sql):
    stack = []  # 괄호의 위치를 저장할 스택
    pairs = []  # 괄호 쌍을 저장할 리스트
    modified_sql = list(sql)  # 문자열을 리스트로 변환
    inside_sqls = []  # 괄호 안의 SELECT 구문을 저장할 리스트

    # AS ( 또는 AS( 앞에 오는 괄호 위치를 찾기 위한 패턴
    pattern = re.compile(r'AS\s*\(', re.IGNORECASE)

    # 일치하는 모든 위치 찾기
    matches = [m.end() - 1 for m in pattern.finditer(sql)]

    # 괄호를 열고 닫는 인덱스 쌍을 찾기 위한 로직
    for start_pos in matches:
        local_stack = []
        for i in range(start_pos, len(sql)):
            if sql[i] == '(':
                local_stack.append(i)
            elif sql[i] == ')':
                if local_stack:
                    open_idx = local_stack.pop()
                    if not local_stack:
                        pairs.append((start_pos, i))  # 가장 바깥 괄호 쌍만 저장
                        break

    cnt_test = []
    k_cnt = 0

    # 괄호를 못 찾을 경우, 리턴
    if len(pairs) == 0:
        return sql, cnt_test

    # 가장 안쪽 괄호부터 처리
    for idx, (start, end) in enumerate(reversed(pairs)):

        inside_sql = "".join(modified_sql[start + 1:end])  # 괄호 내부 문자열 추출
        
        if re.search(r'\bSELECT\b', inside_sql, re.IGNORECASE):            
            inside_sqls.append(inside_sql)
            modified_sql[start + 1:end] = list(f"CTE{idx}")
          

    with_clause = "".join(modified_sql)


    #맨처음 나오는 SELECT의 위치 저장
    match = re.search(r'\bSELECT\b', with_clause, re.IGNORECASE)
    select_pos = match.start() 
    
    #CTE 제외한 메인 쿼리
    rest_of_query = with_clause[select_pos:]
    with_clause = with_clause[:select_pos]


    #문자의 첫 시작이 /**/ 인경우 예외처리
    a_moon = ''
    comment, cleaned_sql =extract_comment_and_clean_sql(with_clause,'WITH')

    if comment is not None:
        a_moon = comment
        #치환 완료된 쿼리 저장
        with_clause = cleaned_sql
    else:
        #치환 완료된 쿼리 저장
        with_clause = cleaned_sql
    

    with_clause = format_with_clause(with_clause,a_moon)
    
    return with_clause, inside_sqls, rest_of_query
    
#치환된 CTE 부분을 형식 변환 로직.
def format_with_clause(with_clause,a_moon):
    with_clause = with_clause.strip()
 
    prefix = "WITH "
    rest = with_clause[5:]

    parts = []
    current = ''
    depth = 0
    for char in rest:
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        if char == ',' and depth == 0:
            parts.append(current.strip())
            current = ''
        else:
            current += char
    if current:
        parts.append(current.strip())

    formatted_parts = []
    for part in parts:
        match = re.match(r'(\w+)\s+AS\s*\((.*)\)', part, re.IGNORECASE | re.DOTALL)
        if match:
            name, body = match.groups()
            formatted_parts.append(f"{name} AS (\n{body.strip()}\n)")
        else:
            formatted_parts.append(part)

    #CTE 앞에 주석이 없을 경우는 그대로 출력
    if a_moon == '':
        return prefix + ",\n".join(formatted_parts)
    else:
    #주석이 있는경우 ,예외처리
        return a_moon+'\n'+prefix + ",\n".join(formatted_parts)
    
    
#추가 FROM ,WHERE ,HAVING : CASE 문 예외처리함수 
def process_case_lines(sql: str, select_end_pos: int):
    lines = sql.splitlines()
    processed_lines = []

    for line in lines:
        # CASE 문이 포함된 줄
        if re.search(r'\bCASE\b', line, re.IGNORECASE):
            # 정렬 함수 적용 후 라인 추가
            formatted_line = case_for_sorted(' ' * (select_end_pos - 1)  + line.strip())
            processed_lines.append(formatted_line)
        else:
            # 그대로 유지
            processed_lines.append(line)

    return "\n".join(processed_lines)



#추가작업 
# 1. order by : 함수(,) 예외처리 ->현재 , 를 기준으로 split (완료)
# 2. ( ) 안에 and , or 있을시 정렬하지 말고 pass (완료)
# 3. 코드 정리 (완료료)
# 4. 기능별 예외처리(완료)
# 5. 코드 분실시 예외처리 (완료)
# 6. /**/ 애 처리(완료)
# 8. 코드에 () 처리 미완료시 예외처리 (완료)
# 9. AS 처리(완료)
# 10 . between ~and 처리   select , where , join , having ,(완료)
# 11. union 처리
# case 문의 경우 현재는 select 절에만 있을때 사용가능.(완료)
# join  사용시 앞에 left ,right 등 안 붙이면 정렬x
# 내장 함수 안에 FROM 있는경우 예외 처리.(완료)
# 맨처음이 /**/으로 시작하는 부분 예외 처리.(완료)  


#/**/안에 나오는 AND OR 처리해야함.-> 애를 그냥 /**/안에 내용을 치환 후 마지막에 롤백하는걸로 함수 만들 예정.(완료)
#[ ] 사이의 내용 치환 -> 완료


#/**/사이에 AND,OR 등 다른 변수가 들어갈시 정렬이 깨짐 -> /**/안의 내용을 치환 -> 정렬 후 -> 롤백백
def replace_comments2(sql):
    # 인덱스 초기화
    count = 0

    # 치환된 주석 내용을 담을 리스트
    replaced_comments = []

    def replace_comment(match):
        nonlocal count
        original_comment = match.group()[2:-2].strip()
        replaced_comments.append(original_comment)
        result = f"/*commend_{count}*/"
        count += 1
        return result

    # 주석을 치환하고, 그 내용은 리스트에 추가
    modified_text = re.sub(r"/\*.*?\*/", replace_comment, sql)

    return modified_text, replaced_comments
