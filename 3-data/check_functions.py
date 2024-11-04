import pandas as pd
checks = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/dining/check-data.csv')

def clean_currency(value:str) -> float:
    '''
    This function will take a string value and remove the dollar sign and commas
    and return a float value.
    '''
    return float(value.replace(',', '').replace('$', ''))
checks['total_amount_of_check_cleaned'] = checks['total amount of check'].apply(clean_currency)
checks['price_per_item'] = checks['total_amount_of_check_cleaned'] / checks['total items on check']

def detect_whale(
        items_per_person:float, 
        price_per_person:float, 
        items_per_person_75th_pctile:float, 
        price_per_person_75_pctile:float) -> str:
    if items_per_person > items_per_person_75th_pctile and price_per_person > price_per_person_75_pctile:
        return 'whale'
    if items_per_person > items_per_person_75th_pctile:
        return 'big eater'
    if price_per_person > price_per_person_75_pctile:
        return 'big spender'
    
    return ''

detect_tipper()