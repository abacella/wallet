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
![image](https://user-images.githubusercontent.com/80563790/127590946-4d921bfb-db9c-43e1-a0a9-30094a2c2f72.png)

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

![image](https://user-images.githubusercontent.com/80563790/127590808-b32b6ec8-df86-40f1-a966-daeddcbd5193.png)

### Set up Custom Node
1) Make sure that you scroll down to choose Custom in the "Network" column to reveal more options like Chain ID:
2) Add the chain id written in the block.json file

![image](https://user-images.githubusercontent.com/80563790/127591231-dfdbdf0b-53e6-4dbd-b4e2-7db1204107bc.png)

On the next screen, click Select Wallet File, then navigate to the keystore directory inside your node1 directory, select the file located there, provide your password when prompted and then click Unlock.

![image](https://user-images.githubusercontent.com/80563790/127591320-d05bf285-d5f8-4db0-8dc3-5d2c519894a6.png)


Go to MyCrypto Account and transfer money betweeen node1 and node2 by:
1) Addding the node2 public key information to the address field
2) Amount
3) Click on the Send transation Button

![image](https://user-images.githubusercontent.com/80563790/127591475-6758f1d8-08c5-4851-bc0d-1598016165b2.png)

Check if the transmission was succesfull. (It might take a while nad you might have to reboot MyCrypto)


![image](https://user-images.githubusercontent.com/80563790/127592356-07ab8023-cb29-4163-9fbb-16fe34bec67c.png)


![image](https://user-images.githubusercontent.com/80563790/127591060-ef0dae4a-7649-4e04-a01c-eb8eed101275.png)


