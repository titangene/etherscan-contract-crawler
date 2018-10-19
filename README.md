# etherscan-contract-crawler
Ethereum contract crawler (target: Etherscan)

# Packages
- beautifulsoup4
- lxml
- numpy
- pandas
- requests

# Usage
To create an environment:

```shell
$ conda create -n crawler
```

Activate the new environment:

```shell
# Windows
$ activate <environment>

# Linux and macOS
$ source activate <environment>
```

Install packages:

```
$ pip install -r requirements.txt
```

Executive crawler:

```shell
$ python crawler.py
```