from src.utils import *
from src.variables import *
import numpy as np

# Portfolio position
option1 = EuropeanCall(asset_price=asset_price, asset_volatility=sigma, strike_price=K1, time_to_expiration=dt,risk_free_rate=rf)

# theoretical value of the position
print('Theoretical Initial Portfolio value: ', str(option1.price * abs(nContract1)))

# greeks
print('Initial Portfolio Greeks:\n '
      'Delta: {}\n '
      'Gamma: {}\n '
      'Vega: {}'.format(option1.delta * nContract1,
                        option1.gamma * nContract1,
                        option1.vega * nContract1))

# Price option2 and option3 and find the greeks
option2 = EuropeanCall(asset_price=asset_price, asset_volatility=sigma, strike_price=K2, time_to_expiration=dt, risk_free_rate=rf)

option3 = EuropeanCall(asset_price=asset_price, asset_volatility=sigma, strike_price=K3, time_to_expiration=dt, risk_free_rate=rf)

# greek neutralization -- gamma and vega
greeks = np.array([[option2.gamma, option3.gamma], [option2.vega, option3.vega]])
portfolio_greeks = [[option1.gamma * abs(nContract1)], [option1.vega * abs(nContract1)]]
inv = np.linalg.inv(np.round(greeks, 2))  # We need to round otherwise we can end up with a non-invertible matrix

# position on option 2 and 3 to be gamma and vega neutral
w = np.dot(inv, portfolio_greeks)

# Greeks including delta
portfolio_greeks = [[option1.delta * nContract1], [option1.gamma * nContract1], [option1.vega * nContract1]]
greeks = np.array([[option2.delta, option3.delta], [option2.gamma, option3.gamma], [option2.vega, option3.vega]])
w_stock = (np.round(np.dot(np.round(greeks, 2), w) + portfolio_greeks))[0]

# final allocation
print('Final asset allocation: \n '
      'option1: {}\n '
      'option2: {}\n '
      'option3: {}\n '
      'underlying asset: {}'.format(nContract1,
                                    int(w[0]),
                                    int(w[1]),
                                    int(w_stock)))


