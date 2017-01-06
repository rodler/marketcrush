from __future__ import division
import os
import random
import string
import numpy as np
import pytest


@pytest.fixture
def random_filename(tmpdir_factory):
    dir = str(tmpdir_factory.mktemp('marketcrush').realpath())
    fname = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    filename = os.path.join(dir, fname)
    return filename


@pytest.fixture
def gbm():
    T = 20
    mu = 0.01
    sigma = 0.1
    S0 = 20
    dt = 0.01
    N = round(T/dt)
    t = np.linspace(0, T, N)
    W = np.random.standard_normal(size=N)
    W = np.cumsum(W)*np.sqrt(dt)  ### standard brownian motion ###
    X = (mu-0.5*sigma**2)*t + sigma*W
    return S0*np.exp(X)  ### geometric brownian motion ###


@pytest.fixture
def config_test(random_filename):
    class Config:
        def __init__(self):
            self.short_tp = 25
            self.long_tp = 50
            self.filter_fp = 75
            self.filter_sp = 150
            self.risk_factor = 0.002
            self.initial_cap = 1e6
            self.atr_exit_fraction = 3
            self.atr_stops_period = 20
            self.commission = 0.001
            self.point_value = 10
            self.output_file = random_filename
    return Config()