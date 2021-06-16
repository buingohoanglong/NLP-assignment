import re

token_types = {
    'bus': ['bus', 'xe_bus', 'xe_buýt', 'Bus', 'Xe_bus', 'Xe_buýt', 'buýt', 'Buýt', 'xe', 'Xe'],
    'city': ['city', 'thành_phố', 'Thành_phố', 'tỉnh', 'Tỉnh'],
    'arrive': ['đến', 'tới'],
    'from': ['từ', 'từ_lúc'],
    'which': ['nào'],
    'atime': ['lúc', 'vào_lúc'],
    'dtime': ['lúc'],
    'name': ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'HUE', 'HCM', 'HN', 'DANANG', 'Hồ_Chí_Minh', 'Hà_Nội', 'Huế', 'Đà_Nẵng'],
    'runtime': ['Thời_gian', 'thời_gian'],
    'time': ['time'],
}

def token_type(token):
    for token_type in token_types:
        if token in token_types[token_type]:
            return token_type
    if re.search('\d{3,4}HR', token):
        return 'time'
    if token == '<ROOT>':
        return token
    return '<UNKNOWN>'