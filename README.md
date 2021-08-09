# Homework Wallet

This project builds a wallet in python in which you are abe to derive ETH and BTCTEST Accounts from a 12 word mneumonic phrase  and transfer values from those Accounts.

Inital intallation:
1) To begin you should have a python 3.7 enviroment on your computer.
2) Clone this repository to you computer.
3) We considered that you also installed the hd-wallet-derive library inside the wallet folder. If not see tutorial in the end of this file.
4) You will need an Ethereum Network running on your computer in this local address "http://127.0.0.1:8545"
5) Inside the wallet folder type the command below to install web3.py and bit to be able to interact with the ETH  and BTCTEST Blockchain
```bash
$ pip install -r requirements.txt
```

Type python
```bash
$ python
```

In the wallet folder create a file called mne.env with the 15 words meneumonic phrase in it.

Ex:
mnemonic = "15 words"


import wallet with the command line below. You will be able to execute the formulas to trasnfer funds and derive accounts.
In this command line we already derived 3 ETH adn 3 BTCTEST Account from the menumonic phrase and print it in the screen.
```bash
>>> from wallet import *
```
![image](https://github.com/abacella/wallet/blob/main/Screenshots/btc_derive.png)
![image](https://github.com/abacella/wallet/blob/main/Screenshots/eth_derive.png)


### Getting Account Access (BTCTEST, and ETH) using private Key for the first account derived fomr each one of them
```bash
>>> Account_ETH = priv_key_to_account(ETH, (coins[ETH][0]['privkey']))
>>> Account_BTCTEST = priv_key_to_account(BTCTEST, (coins[BTCTEST][0]['privkey']))
```

Formula inputs:
1. BTCTEST or ETH
2. Account_ETH or Account_BTCTEST
3. Sender Address as string
4. Amount

# BTCTEST Example

## Account that will Receive BTCTEST
![image](https://github.com/abacella/wallet/blob/main/Screenshots/btc_address.png)

## Send BTCTEST Formula Example

```bash
>>> send_tx(BTCTEST, Account_BTCTEST, 'n3xdmfgWz8ZvMnqPYxoDS8rtfARNJtDBE2', 0.0000001)
>>> print(priv_key_to_account(BTCTEST, (coins[BTCTEST][0]['privkey'])).get_transactions()[0])
5b37c293e2322f68a0786b8ec4e6a020bbdc061a12a300b6fb3c787ca60c69f1
```

## Confirm BTCTEST transmission on https://tbtc.bitaps.com/
![image](https://github.com/abacella/wallet/blob/main/Screenshots/btc_block.png)

# ETH Example

## Account that will Receive ETH
![image](https://github.com/abacella/wallet/blob/main/Screenshots/eth_address.png)

## Send ETH Formula Example
```bash
>>> send_tx(ETH, Account_ETH, '0xCE4B45cD08Dd665900a70282f0714560Bc8AE38C', 1000)
HexBytes('0x8dac21294a03ff81ed5900af9212a232a658f56f2ee8b9319915434e997378bc')
```

## Confirm ETH transaction on MyCrypto
![image](https://github.com/abacella/wallet/blob/main/Screenshots/eth_mycrypto.png)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
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










