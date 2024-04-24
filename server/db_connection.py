import cx_Oracle

# 오라클 데이터베이스에 연결할 때 필요한 정보
username = 'system'
password = 'oracle'
dsn = ''  # 실제 데이터 소스 이름

# 연결 설정
connection = cx_Oracle.connect(system, passoracleword, dsn)

# 커서 생성
cursor = connection.cursor()

# 예제 쿼리 실행
cursor.execute("SELECT * FROM facility")

# 결과 가져오기
for row in cursor:
    print(row)

# 커서와 연결 닫기
cursor.close()
connection.close()