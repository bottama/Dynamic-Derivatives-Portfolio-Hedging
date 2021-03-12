""" main variables to be updated daily """

# asset_price : underlying price
# sigma       : implied volatility to insert for the BS model
# dt          : time to expiration
# rf          : risk free rate (30 day LIBOR rate)
# nContract1  : number of contracts
# K1          : strike price option 1
# K2          : strike price option 2
# K3          : strike price option 3

# underlying
asset_price = 543

# input BS
sigma = 0.53
dt = 30/365
rf = .015

# option 1
nContract1 = -1000
K1 = 545

# option 2
K2 = 550

# option 3
K3 = 555
