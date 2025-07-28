import pandas as pd

def get_option_data():
    # Mock data simulating real-time option chain (replace with API)
    data = pd.DataFrame({
        'Strike': [24800, 24900, 25000, 25100, 25200],
        'Type': ['Call', 'Call', 'Call', 'Put', 'Put'],
        'LTP': [100, 80, 50, 70, 90],
        'IV': [15.0, 13.0, 10.0, 12.0, 14.0],
        'OI': [100000, 80000, 120000, 95000, 110000],
        'Change_OI': [5000, 3000, 10000, 7000, 8500]
    })
    return data