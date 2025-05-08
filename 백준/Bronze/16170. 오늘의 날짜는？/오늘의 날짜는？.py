# https://www.acmicpc.net/problem/16170
# 백준 16170 오늘의 날짜는?
# 문제를 푸는 지금 시각이 UTC+0(세계 표준시)을 기준으로 무슨 날짜인지 출력

from datetime import datetime, timedelta

now = datetime.now() - timedelta(hours=9)
print(now.year)
print('%02d' % now.month)
print('%02d' % now.day)