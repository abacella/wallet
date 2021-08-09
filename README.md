# Homework Wallet




```bash
$ pip install -r requirements.txt
```
```bash
>>> from wallet import *
```
![image](https://github.com/abacella/wallet/blob/main/Screenshots/btc_derive.png)
![image](https://github.com/abacella/wallet/blob/main/Screenshots/eth_derive.png)


### Getting Account Access (BTCTEST, and ETH) using private Key
```bash
>>> Account_ETH = priv_key_to_account(ETH, (coins[ETH][0]['privkey']))
>>> Account_BTCTEST = priv_key_to_account(BTCTEST, (coins[BTCTEST][0]['privkey']))
```
## Account that will Receive BTCTEST
![image](https://github.com/abacella/wallet/blob/main/Screenshots/btc_address.png)


## Send BTCTEST Formula
```bash
>>> send_tx(BTCTEST, Account_BTCTEST, 'n3xdmfgWz8ZvMnqPYxoDS8rtfARNJtDBE2', 0.0000001)
>>> print(priv_key_to_account(BTCTEST, (coins[BTCTEST][0]['privkey'])).get_transactions()[0])
5b37c293e2322f68a0786b8ec4e6a020bbdc061a12a300b6fb3c787ca60c69f1
```

## Confirm BTCTEST transmission on https://tbtc.bitaps.com/
![image](https://github.com/abacella/wallet/blob/main/Screenshots/btc_block.png)


## Account that will Receive ETH
![image](https://github.com/abacella/wallet/blob/main/Screenshots/eth_address.png)

## Send ETH Formula
```bash
>>> send_tx(ETH, Account_ETH, '0xCE4B45cD08Dd665900a70282f0714560Bc8AE38C', 1000)
HexBytes('0x8dac21294a03ff81ed5900af9212a232a658f56f2ee8b9319915434e997378bc')
```

## Confirm ETH transaction on MyCrypto
![image](https://github.com/abacella/wallet/blob/main/Screenshots/eth_mycrypto.png)


## How to install HD-Wallet-Derive
Tutorial from https://columbia.bootcampcontent.com/columbia-bootcamp/cu-nyc-virt-fin-pt-03-2021-u-c/-/blob/master/02-Homework/19-Blockchain-Python/Instructions/Resources/HD_Wallet_Derive_Install_Guide.md

Initiallly create a folder called wallet

```bash
  mkdir wallet
```

With the latest version of PHP installed on our machines install the `hd-wallet-derive` library.

1. With your terminal open as indicated for your operating system, cd into your wallet folder and run the following code:

```bash
    git clone https://github.com/dan-da/hd-wallet-derive
    cd hd-wallet-derive
    curl https://getcomposer.org/installer -o installer.php
    php installer.php
    php composer.phar install
```

3. You should now have a folder called `hd-wallet-derive` containing the PHP library!










