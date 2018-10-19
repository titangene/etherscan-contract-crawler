import io

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests

def parse_html(url, class_):
	req = requests.get(url)
	soup = BeautifulSoup(req.text, 'lxml')
	return soup.find(class_=class_)

def main():
	base_url = 'https://etherscan.io'
	contracts_verified_url = base_url + '/contractsVerified'
	contract_address_base_url = base_url + '/address/'

	contracts_verified_table = parse_html(url=contracts_verified_url, class_='table-hover')
	contracts_verified_df = pd.read_html(str(contracts_verified_table))[0]
	print(contracts_verified_df.head())

	for idx, row in contracts_verified_df.head(3).iterrows():
		contract_address_url = contract_address_base_url + row['Address']
		contract_code = parse_html(url=contract_address_url, class_='js-sourcecopyarea').contents[0]

		contract_path = 'contract/{}.sol'.format(row['ContractName'])
		with io.open(contract_path, 'w', encoding='utf8') as file:
			file.write(contract_code)

		print('save:', 'address:', row['Address'][:10], row['ContractName'])

if __name__ == '__main__':
	main()