#결과값을 지정된 정밀도로 반올림 하는 함수
def round_result(value, precision):
    return round(value, precision)

#각도를 라디안으로 변환하는 함수
import math 

def convert_to_radian(angle, unit):
    if unit == 'degree':
    #각도를 라디안으로 변환
        return angle*(math.pi/180) #math.pi는 math모듈 내의 파이값
    elif unit == 'radian':
    #이미 라디안값인 경우 그대로 반환
        return angle
    else :
        raise ValueError("Invalid unit. Use 'degree' or 'radian'.")
