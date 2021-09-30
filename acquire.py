import requests

# Question 1):
def items_df():
    url = 'https://python.zgulde.net'
    response = requests.get(url + '/api/v1/items')

    filename = 'items.csv'
    if os.path.isfile(filename):
        items = pd.read_csv(filename, index_col=[0])
    else:
        if response.ok:
            extracted_data = list()
            payload = response.json()['payload']
            max_page = payload['max_page']
            print(url + '/api/v1/items')
            for n in range(max_page):
                extracted_data.extend(payload['items'])
                try:
                    new_url = url[:len(url)] + payload['next_page']
                    print(new_url)
                    response = requests.get(new_url)
                    payload = response.json()['payload']
                except:
                    pass
                
            items = pd.DataFrame(extracted_data)
            items.to_csv(filename)

        else:
            print(response.status_codeus_code)
    return items

# Question 2):
def stores_df():
    url = 'https://python.zgulde.net'
    response = requests.get(url + '/api/v1/stores')

    filename = 'stores.csv'
    if os.path.isfile(filename):
        stores = pd.read_csv(filename, index_col=[0])
    else:
        if response.ok:
            extracted_data = list()
            payload = response.json()['payload']
            max_page = payload['max_page']
            print(url + '/api/v1/stores')
            for n in range(max_page):
                extracted_data.extend(payload['stores'])
                try:
                    new_url = url[:len(url)] + payload['next_page']
                    print(new_url)
                    response = requests.get(new_url)
                    payload = response.json()['payload']
                except:
                    pass
                
            stores = pd.DataFrame(extracted_data)
            stores.to_csv(filename)

        else:
            print(response.status_codeus_code)
    return stores

def sales_df():
    url = 'https://python.zgulde.net'
    response = requests.get(url + '/api/v1/sales')

    filename = 'sales.csv'
    if os.path.isfile(filename):
        sales = pd.read_csv(filename, index_col=[0])
    else:
        if response.ok:
            extracted_data = list()
            payload = response.json()['payload']
            max_page = payload['max_page']
            print(url + '/api/v1/sales')
            for n in range(max_page):
                extracted_data.extend(payload['sales'])
                try:
                    new_url = url[:len(url)] + payload['next_page']
                    print(new_url)
                    response = requests.get(new_url)
                    payload = response.json()['payload']
                except:
                    pass
                
            sales = pd.DataFrame(extracted_data)
            sales.to_csv(filename)

        else:
            print(response.status_codeus_code)
    return sales

# Question 5):
def merge_data(sales = sales_df(), items = items_df(), stores = stores_df()):
    sales = sales.rename(columns={'store': 'store_id', 'item': 'item_id'})
    df = sales.join(stores.set_index('store_id'), on='store_id')
    df = df.join(items.set_index('item_id'), on='item_id')
    return df

# Question 6):
def germany_df():
    url = 'https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv'

    filename = 'opsd_germany.csv'
    if os.path.isfile(filename):
        opsd = pd.read_csv(filename, index_col=[0])
    else:
        opsd = pd.read_csv(url, index_col=[0])
    return opsd

