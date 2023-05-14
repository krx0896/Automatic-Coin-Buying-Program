import pyupbit
import numpy as np


# 변동성 전략 백테스팅 코드
def get_ror(k=0.5):
    df = pyupbit.get_ohlcv("KRW-BTC", count=7)
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'],
                         1)

# 누적 수익률 계산
    ror = df['ror'].cumprod()[-2]
    return ror

# k값이 0.1부터 0.9까지 일때 각각의 수익률 (하락장일수록 k값이 클때 더 이득)
for k in np.arange(0.1, 1.0, 0.1):
    ror = get_ror(k)
    print("%.1f %f" % (k, ror))