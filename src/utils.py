""" Algorithmic Portfolio Hedging - Multi Options strategy  - BS pricing for Dynamic Hedges """

"""
Author: Matteo Bottacini, matteo.bottacini@usi.ch
last update: March 11, 2021
"""

import math
from scipy.stats import norm

# define the European call option
class EuropeanCall:

    def call_delta(
            self, asset_price, asset_volatility, strike_price,
            time_to_expiration, risk_free_rate
    ):
        b = math.exp(-risk_free_rate * time_to_expiration)
        x1 = math.log(asset_price / (b * strike_price)) + .5 * (
                    asset_volatility * asset_volatility) * time_to_expiration
        x1 = x1 / (asset_volatility * (time_to_expiration ** .5))
        z1 = norm.cdf(x1)
        return z1

    def call_gamma(
            self, asset_price, asset_volatility, strike_price,
            time_to_expiration, risk_free_rate
    ):
        b = math.exp(-risk_free_rate * time_to_expiration)
        x1 = math.log(asset_price / (b * strike_price)) + .5 * (
                    asset_volatility * asset_volatility) * time_to_expiration
        x1 = x1 / (asset_volatility * (time_to_expiration ** .5))
        z1 = norm.cdf(x1)
        z2 = z1 / (asset_price * asset_volatility * math.sqrt(time_to_expiration))
        return z2

    def call_vega(
            self, asset_price, asset_volatility, strike_price,
            time_to_expiration, risk_free_rate
    ):
        b = math.exp(-risk_free_rate * time_to_expiration)
        x1 = math.log(asset_price / (b * strike_price)) + .5 * (
                    asset_volatility * asset_volatility) * time_to_expiration
        x1 = x1 / (asset_volatility * (time_to_expiration ** .5))
        z1 = norm.cdf(x1)
        z2 = asset_price * z1 * math.sqrt(time_to_expiration)
        return z2 / 100

    def call_price(
            self, asset_price, asset_volatility, strike_price,
            time_to_expiration, risk_free_rate
    ):
        b = math.exp(-risk_free_rate * time_to_expiration)
        x1 = math.log(asset_price / (b * strike_price)) + .5 * (
                    asset_volatility * asset_volatility) * time_to_expiration
        x1 = x1 / (asset_volatility * (time_to_expiration ** .5))
        z1 = norm.cdf(x1)
        z1 = z1 * asset_price
        x2 = math.log(asset_price / (b * strike_price)) - .5 * (
                    asset_volatility * asset_volatility) * time_to_expiration
        x2 = x2 / (asset_volatility * (time_to_expiration ** .5))
        z2 = norm.cdf(x2)
        z2 = b * strike_price * z2
        return z1 - z2

    def __init__(
            self, asset_price, asset_volatility, strike_price,
            time_to_expiration, risk_free_rate
    ):
        self.asset_price = asset_price
        self.asset_volatility = asset_volatility
        self.strike_price = strike_price
        self.time_to_expiration = time_to_expiration
        self.risk_free_rate = risk_free_rate
        self.price = self.call_price(asset_price, asset_volatility, strike_price, time_to_expiration, risk_free_rate)
        self.delta = self.call_delta(asset_price, asset_volatility, strike_price, time_to_expiration, risk_free_rate)
        self.gamma = self.call_gamma(asset_price, asset_volatility, strike_price, time_to_expiration, risk_free_rate)
        self.vega = self.call_vega(asset_price, asset_volatility, strike_price, time_to_expiration, risk_free_rate)

# define the European Put option
class EuropeanPut:

    def put_delta(
            self, asset_price, asset_volatility, strike_price,
            time_to_expiration, risk_free_rate
    ):
        b = math.exp(-risk_free_rate * time_to_expiration)
        x1 = math.log(asset_price / (b * strike_price)) + .5 * (
                    asset_volatility * asset_volatility) * time_to_expiration
        x1 = x1 / (asset_volatility * (time_to_expiration ** .5))
        z1 = norm.cdf(x1)
        return z1 - 1

    def put_gamma(
            self, asset_price, asset_volatility, strike_price,
            time_to_expiration, risk_free_rate
    ):
        b = math.exp(-risk_free_rate * time_to_expiration)
        x1 = math.log(asset_price / (b * strike_price)) + .5 * (
                    asset_volatility * asset_volatility) * time_to_expiration
        x1 = x1 / (asset_volatility * (time_to_expiration ** .5))
        z1 = norm.cdf(x1)
        z2 = z1 / (asset_price * asset_volatility * math.sqrt(time_to_expiration))
        return z2

    def put_vega(
            self, asset_price, asset_volatility, strike_price,
            time_to_expiration, risk_free_rate
    ):
        b = math.exp(-risk_free_rate * time_to_expiration)
        x1 = math.log(asset_price / (b * strike_price)) + .5 * (
                    asset_volatility * asset_volatility) * time_to_expiration
        x1 = x1 / (asset_volatility * (time_to_expiration ** .5))
        z1 = norm.cdf(x1)
        z2 = asset_price * z1 * math.sqrt(time_to_expiration)
        return z2 / 100

    def put_price(
            self, asset_price, asset_volatility, strike_price,
            time_to_expiration, risk_free_rate
    ):
        b = math.exp(-risk_free_rate * time_to_expiration)
        x1 = math.log((b * strike_price) / asset_price) + .5 * (
                    asset_volatility * asset_volatility) * time_to_expiration
        x1 = x1 / (asset_volatility * (time_to_expiration ** .5))
        z1 = norm.cdf(x1)
        z1 = b * strike_price * z1
        x2 = math.log((b * strike_price) / asset_price) - .5 * (
                    asset_volatility * asset_volatility) * time_to_expiration
        x2 = x2 / (asset_volatility * (time_to_expiration ** .5))
        z2 = norm.cdf(x2)
        z2 = asset_price * z2
        return z1 - z2

    def __init__(
            self, asset_price, asset_volatility, strike_price,
            time_to_expiration, risk_free_rate
    ):
        self.asset_price = asset_price
        self.asset_volatility = asset_volatility
        self.strike_price = strike_price
        self.time_to_expiration = time_to_expiration
        self.risk_free_rate = risk_free_rate
        self.price = self.put_price(asset_price, asset_volatility, strike_price, time_to_expiration, risk_free_rate)
        self.delta = self.put_delta(asset_price, asset_volatility, strike_price, time_to_expiration, risk_free_rate)
        self.gamma = self.put_gamma(asset_price, asset_volatility, strike_price, time_to_expiration, risk_free_rate)
        self.vega = self.put_vega(asset_price, asset_volatility, strike_price, time_to_expiration, risk_free_rate)
