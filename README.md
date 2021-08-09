# Homework Wallet


## Installation

## geth - nodes creation

```bash
./geth --datadir node1 account new
./geth --datadir node2 account new
```

## puppeth

```python
./puppeth
```


![image](https://github.com/abacella/wallet/blob/main/Screenshots/Account%20Setting.png)
![image](https://github.com/abacella/wallet/blob/main/Screenshots/btc_address.png)
![image](https://github.com/abacella/wallet/blob/main/Screenshots/btc_block.png)
![image](https://github.com/abacella/wallet/blob/main/Screenshots/btc_derive.png)
![image](https://github.com/abacella/wallet/blob/main/Screenshots/btc_send.png)
![image](https://github.com/abacella/wallet/blob/main/Screenshots/eth_address.png)
![image](https://github.com/abacella/wallet/blob/main/Screenshots/eth_derive.png)
![image](https://github.com/abacella/wallet/blob/main/Screenshots/eth_mycrypto.png)
![image](https://github.com/abacella/wallet/blob/main/Screenshots/eth_send.png)

### Using geth, initialize each node with the new networkname.json.


```python
./geth --datadir node1 init block.json
./geth --datadir node2 init block.json
```




### Now the nodes can be used to begin mining blocks.

### Run the nodes in separate terminal windows with the commands:

```python
./geth --datadir node1 --unlock "SEALER_ONE_ADDRESS" --mine --rpc --allow-insecure-unlock
./geth --datadir node2 --unlock "SEALER_TWO_ADDRESS" --mine --port 30304 --bootnodes "enode://SEALER_ONE_ENODE_ADDRESS@127.0.0.1:30303" --ipcdisable --allow-insecure-unlock
```


NOTE: Type your password and hit enter - even if you can't see it visually!


# MyCrypto

## Connecting to new Network


Click "Add Custom Node", then add the custom network information that you set in the genesis.



### Set up Custom Node
1) Make sure that you scroll down to choose Custom in the "Network" column to reveal more options like Chain ID:
2) Add the chain id written in the block.json file



On the next screen, click Select Wallet File, then navigate to the keystore directory inside your node1 directory, select the file located there, provide your password when prompted and then click Unlock.



Go to MyCrypto Account and transfer money betweeen node1 and node2 by:
1) Addding the node2 public key information to the address field
2) Amount
3) Click on the Send transation Button



Check if the transmission was succesfull. (It might take a while nad you might have to reboot MyCrypto)








