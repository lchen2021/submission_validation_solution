import pandas as pd
import seaborn as sns
import numpy as np
from datetime import datetime
import datetime
import ccy
from fuzzywuzzy import process


# function to check date format
def date_format_check(date_string):
    for fmt in ('%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'):
        try:
            return 'PASSED'
        except ValueError:
            pass
    raise ValueError('Invalid date format - pls check!!')
    


def client_name_check(name_string):
    valid_client =['Credit Suisse', 'Barclays', 'HSBC', 'Santander','SC','UBS']
    if name_string in valid_client:
        return 'PASSED'
    else:
        return 'Invalid client name - pls check!!'
        

def submission_asset_check(asset_string):
    valid_asset =['Foreign','Foreign Exchange']
    best_match = process.extractOne(asset_string,valid_asset, score_cutoff = 90)
    if best_match != None:
        return best_match[0]
    else:
        return 'Invalid asset name - pls Check!!'


def submission_snaptime_check(service_string):
    valid_val = ['London 4 PM', 'Tokyo 3 PM', 'New York 4 PM']
    if service_string.lower() == 'london 4 pm':
        return 'London 4 PM'
    elif service_string.lower() == 'tokyo 3 pm':
        return 'Tokyo 3 PM'
    elif service_string.lower() == 'new york 4 pm':
        return 'New York 4 PM'
    else:
        return 'Invalid service name - pls Check!!'


def submission_curr_check(ccy_code):
    additional_ccy = ['XAU','XAG','XPT','XPD','CNH','UDI']
    if ccy.currency(ccy_code) is not None or ccy_code.upper() in additional_ccy:
        return ccy_code.upper()
    else:
        return 'Invalid currency code - pls Check!!'


def submission_service_check(service_name):
    valid_servie_name =['Vanilla']
    best_match = process.extractOne(service_name,valid_servie_name, score_cutoff = 90)
    if best_match != None:
        return best_match[0]
    else:
        return 'Invalid service name - pls check!!'
        

def valid_currency_pair_check(curr1, curr2):
    valid_pair =['aud_usd', 'gbp_usd','jpy_twd']
    pair = '_'.join([curr1.lower(),curr2.lower()])
    if pair in valid_pair:
        return 'PASSED'
    else:
        return 'Invalid currency pair - pls check!!'


def submission_instrument_type_match(instr_type):
    valid_types =['fx forward','Forward','forward fx','spot']
    best_match = process.extractOne(instr_type,valid_types)
    return best_match[0]    
def submission_instrument_type_match_score(instr_type):
    valid_types =['fx forward','Forward','forward fx','spot']
    best_match = process.extractOne(instr_type,valid_types)
    return best_match[1]
    

def submission_tenor_check(tenor):
    valid_tenor =["ON", "TN", "SpotNext", "1W", "2W", "3W", "1M", "2M", "3M", "4M", "5M", "6M", "9M", "1Y", "18M", "2Y", "3Y", "4Y", "5Y", "6Y", "7Y", "10Y"]
    best_match = process.extractOne(tenor,valid_tenor)
    return best_match[0]
def submission_tenor_match_score_check(tenor):
    valid_tenor =["ON", "TN", "SpotNext", "1W", "2W", "3W", "1M", "2M", "3M", "4M", "5M", "6M", "9M", "1Y", "18M", "2Y", "3Y", "4Y", "5Y", "6Y", "7Y", "10Y"]
    best_match = process.extractOne(tenor,valid_tenor)
    return best_match[1]
    

def submission_fwrd_conversion_factor_double_check(factor):
    if isinstance(factor, float) == True or isinstance(factor, int) == True :
        return 'PASSED'
    else:
        return 'Invalid conversion factor - pls check!!'


def submission_value_source_check(value_source):
    valid_value_source = ['Trade', 'Model', 'Order']
    best_match = process.extractOne(value_source,valid_value_source)
    if value_source != value_source: # this is to check if value is NaN i.e. null value
        pass
    else:
        return best_match[0]
def submission_value_match_score(value_source):
    valid_value_source = ['Trade', 'Model', 'Order']
    best_match = process.extractOne(value_source,valid_value_source)
    if value_source != value_source: # this is to check if value is NaN i.e. null value
        pass
    else:
        return best_match[1]


def submission_onshore_offshore_check(onoffshore_flag):
    valid_off_onshore_value =['Onshore','Offshore']
    best_match = process.extractOne(onoffshore_flag,valid_off_onshore_value)
    if onoffshore_flag != onoffshore_flag:
        pass
    else:
        return best_match[0]
def submission_onshore_offshore_match_score(onoffshore_flag):
    valid_off_onshore_value =['Onshore','Offshore']
    best_match = process.extractOne(onoffshore_flag,valid_off_onshore_value)
    if onoffshore_flag != onoffshore_flag:
        pass
    else:
        return best_match[1]
        

def submission_onshore_offshore_curr_check(curr,onshore_flag):
    ndf_list = ['CNY','IDR','INR','KRW','MYR','PHP','TWD','VND']
    if onshore_flag !=onshore_flag:
        return 'PASSED'
    else:
        if curr.upper() in ndf_list:
            if str(onshore_flag).lower() =='offshore':
                return 'PASSED'
            else:
                return 'Inconsistent currency to the onshore/offshore flag - pls check!!'
        elif curr.upper() not in ndf_list:
            if str(onshore_flag).lower() =='onshore':
                return 'PASSED'
            else:
                return 'Inconsistent currency to the onshore/offshore flag - pls check!!'


def submission_spot_reference_price_check(spot_price):
    if spot_price !=spot_price:
        return 'Invalid spot price as it cannot be null - pls check!!'
    else:
        if isinstance(spot_price, float) == True or isinstance(spot_price, int) == True:
            return 'PASSED'
        else:
            return 'Invalid spot price - pls check!!'


def submission_mid_fwrd_outright_check(fwrd_outright_value):
    if fwrd_outright_value !=fwrd_outright_value:
        return 'Invalid fwrd outright value as it cannot be null - pls check!!'
    else:
        if isinstance(fwrd_outright_value, float) == True or isinstance(fwrd_outright_value, int) == True :
            return 'PASSED'
        else:
            return 'Invalid fwrd outright value - pls check!!'
        
        
def submission_mid_fwrd_points_check(mid_fwrd_points):
    if mid_fwrd_points !=mid_fwrd_points:
        return 'Invalid fwrd points as it cannot be null - pls check!!'
    else:
        if isinstance(mid_fwrd_points, float) == True or isinstance(mid_fwrd_points, int) == True :
            return 'PASSED'
        else:
            return 'Invalid fwrd points - pls check!!'


def submission_mid_fwrd_points_calculation(mid_fwrd_outright,spot_reference_price,fwrd_conversion_factor):
    return ((mid_fwrd_outright - spot_reference_price) * fwrd_conversion_factor)
    
def submission_mid_fwrd_points_cal_tolerance_check(diff):
    #diff = (mid_fwrd_points-cal)/mid_fwrd_points
    if diff !=diff:
        return 'PASSED'
    else:
        if diff <=0.01 or diff >= -0.01:
            return 'PASSED'
        else:
            return 'Invalid mid fwrd points as it exceeds calculation tolerance of 1% - pls check!!'


def submission_service_check(service_name):
    valid_servie_name =['Vanilla']
    best_match = process.extractOne(service_name,valid_servie_name, score_cutoff = 90)
    if best_match != None:
        return best_match[0]
    else:
        return 'Invalid service name - pls check!!'