# ============================================================
# 연산자를 이용한 웨이퍼 생산제어 프로그램 작성
# ============================================================
# 이 예제는 실제 반도체 장비를 제어하는 프로그램이 아닙니다.
# 생산 진행 여부를 판단하기 전에 필요한 계산값을
# 연산자로 구해보는 교육용 예제입니다.
#
# 아직 조건문을 배우기 전 단계이므로 if문은 사용하지 않습니다.
# 대신 비교 연산자와 논리 연산자의 결과인 True/False를 확인합니다.
#
# 학습 목표:
# - 산술 연산자로 전체 칩 수, 정상 칩 수, 수율을 계산한다.
# - 비교 연산자로 공정값이 기준을 만족하는지 확인한다.
# - 논리 연산자 and로 여러 조건을 하나로 묶는다.
#
# 주의:
# 아래 기준값은 실제 공정 기준이 아닙니다.
# 파이썬 연산자 학습을 위한 교육용 가상 기준입니다.
# ============================================================

# ------------------------------------------------------------
# 교육용 가상 생산 데이터
# 실제 장비에서 가져온 데이터가 아닙니다.
# ------------------------------------------------------------
wafer_count = 3
chips_per_wafer = 650
defective_chips = 42

temperature = 73.5
pressure = 1.8

# ------------------------------------------------------------
# 교육용 가상 기준값
# 실제 공정 기준이 아닙니다.
# ------------------------------------------------------------
min_temperature = 70.0
max_temperature = 75.0

min_pressure = 1.5
max_pressure = 2.0

min_yield_rate = 95.0


# ============================================================
# 수강생 작성 영역
#
# 목표:
# 연산자를 사용해 아래 값을 계산하세요.
#
# 1. total_chips
#    전체 칩 수 = 웨이퍼 개수 * 웨이퍼 1장당 칩 개수
#
# 2. good_chips
#    정상 칩 수 = 전체 칩 수 - 불량 칩 수
#
# 3. defect_rate
#    불량률 = 불량 칩 수 / 전체 칩 수 * 100
#
# 4. yield_rate
#    수율 = 정상 칩 수 / 전체 칩 수 * 100
#
# 5. temperature_ok
#    온도가 min_temperature 이상 max_temperature 이하이면 True
#
# 6. pressure_ok
#    압력이 min_pressure 이상 max_pressure 이하이면 True
#
# 7. yield_ok
#    수율이 min_yield_rate 이상이면 True
#
# 8. production_ok
#    온도, 압력, 수율 조건이 모두 True이면 True
#
# 주의:
# 이 예제에서는 if문을 사용하지 않습니다.
# ============================================================

###########################################################################
# 여기에 코드 작성
total_chips = wafer_count * chips_per_wafer
good_chips = total_chips - defective_chips

defect_rate = defective_chips / total_chips * 100
yield_rate = good_chips / total_chips * 100

temperature_ok = temperature >= min_temperature and temperature <= max_temperature
pressure_ok = pressure >= min_pressure and pressure <= max_pressure
yield_ok = yield_rate >= min_yield_rate

production_ok = temperature_ok and pressure_ok and yield_ok
###########################################################################



print("[웨이퍼 생산 상태 계산 결과]")
print("웨이퍼 개수:", wafer_count)
print("웨이퍼 1장당 칩 개수:", chips_per_wafer)
print("전체 칩 수:", total_chips)
print("정상 칩 수:", good_chips)
print("불량 칩 수:", defective_chips)
print("불량률:", round(defect_rate, 2), "%")
print("수율:", round(yield_rate, 2), "%")
print("온도 기준 만족:", temperature_ok)
print("압력 기준 만족:", pressure_ok)
print("수율 기준 만족:", yield_ok)
print("생산 진행 조건 만족:", production_ok)