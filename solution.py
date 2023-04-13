import pandas as pd
import numpy as np
import math
from scipy.stats import norm
from scipy.stats import binomtest


chat_id = 784892881 # Ваш chat ID, не меняйте название переменной


def solution(x_success: int,            # Количество продаж на контроле
             x_cnt: int,                # Количество заявок на контроле
             y_success: int,            # Количество продаж на тесте
             y_cnt: int) -> bool:       # Количество заявок на тесте

    control_conversion = x_success / x_cnt
    test_conversion = y_success / y_cnt
    
    # perform two-sided hypothesis test with alpha significance level
    p_value = binomtest(y_success, n=y_cnt, p=control_conversion).pvalue
    
    alpha = 0.07
    reject_null = p_value < alpha
    
    return reject_null
