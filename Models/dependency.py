dependency = {
    'arrive': {'<ROOT>': 'PRED'},
    'bus': {'arrive': 'LSUBJ'},
    'from': {'arrive': 'PREP'},
    'dtime': {'from': 'FROM-TIME'},
    'atime': {'arrive': 'PREP-TIME'},
    'runtime': {'arrive': 'RUN-TIME'},
    'time': {'atime': 'TO-TIME', 'dtime': 'FROM-TIME'},
    'city': {'from': 'FROM-LOC', 'arrive': 'TO-LOC'},
    'name': {'city': 'CITY-NAME', 'from': 'CITY-NAME', 'arrive': 'CITY-NAME', 'bus': 'BUS-NAME'},
    'which': {'bus': 'WH-BUS', 'atime': 'WH-TO-TIME', 'dtime': 'WH-FROM-TIME', 'runtime': 'WH-RUN-TIME', 'city': 'WH-CITY'},
}