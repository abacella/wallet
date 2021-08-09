# Homework Wallet




```bash
$ pip install -r requirements.txt
```
```bash
>>> Account_ETH = priv_key_to_account(ETH, (coins[ETH][0]['privkey']))
>>> Account_BTCTEST = priv_key_to_account(BTCTEST, (coins[BTCTEST][0]['privkey']))
>>> send_tx(ETH, Account_ETH, '0xCE4B45cD08Dd665900a70282f0714560Bc8AE38C', 1000)
HexBytes('0x8dac21294a03ff81ed5900af9212a232a658f56f2ee8b9319915434e997378bc')
>>> send_tx(BTCTEST, Account_BTCTEST, 'n3xdmfgWz8ZvMnqPYxoDS8rtfARNJtDBE2', 0.0000001)
>>> print(priv_key_to_account(BTCTEST, (coins[BTCTEST][0]['privkey'])).get_transactions()[0])
5b37c293e2322f68a0786b8ec4e6a020bbdc061a12a300b6fb3c787ca60c69f1
```





## Derive BTCTEST Accounts from mneumonic phrase
![image](https://github.com/abacella/wallet/blob/main/Screenshots/btc_derive.png)


## Derive ETH Accounts from mneumonic phrase
![image](https://github.com/abacella/wallet/blob/main/Screenshots/eth_derive.png)


## Getting Account Access (BTCTEST, and ETH) using private Key
![image](https://github.com/abacella/wallet/blob/main/Screenshots/Account%20Setting.png)




## Account that will Receive BTCTEST
![image](https://github.com/abacella/wallet/blob/main/Screenshots/btc_address.png)

## Send BTCTEST Formula
![image](https://github.com/abacella/wallet/blob/main/Screenshots/btc_send.png)

## Confirm BTCTEST transmission on 
![image](https://github.com/abacella/wallet/blob/main/Screenshots/btc_block.png)




## Account that will Receive ETH
![image](https://github.com/abacella/wallet/blob/main/Screenshots/eth_address.png)


## Send ETH Formula
![image](https://github.com/abacella/wallet/blob/main/Screenshots/eth_send.png)


## Confirm ETH transaction on MyCrypto
![image](https://github.com/abacella/wallet/blob/main/Screenshots/eth_mycrypto.png)









