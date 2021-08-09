# Import dependencies
from bit import Key
from bit import PrivateKeyTestnet
import web3
from bit import wif_to_key
from bit.network import NetworkAPI
import subprocess
import json
from dotenv import load_dotenv
import os
from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account
from pathlib import Path
from getpass import getpass

# Load and set environment variables
load_dotenv("mne.env")
mnemonic = os.getenv("mnemonic")
# Import constants.py and necessary functions from bit and web3
from constants import *

# Create a function called `derive_wallets`
def derive_wallets(Mnemonic, Coin, Numderive, Format):
    command = './derive -g --mnemonic="'+Mnemonic + \
        '" --cols=address,index,path,privkey,pubkey,pubkeyhash,xprv,xpub --numderive=' + \
        Numderive+' --coin='+Coin+' --format='+Format
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = {}
coins = {BTCTEST: derive_wallets(mnemonic, BTCTEST, '3', 'json')}
coins.update({ETH: derive_wallets(mnemonic, ETH, '3', 'json')})
# print(coins, indent=4, sort_keys=True)
print(json.dumps(coins, indent=4, sort_keys=True))

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    else:
        return PrivateKeyTestnet(priv_key)


# This function create the raw, unsigned transaction that contains all metadata needed to transact.
def create_tx(coin, account, to, amount):
    if coin == ETH:
        gasEstimate = w3.eth.estimateGas(
            {"from": account.address, "to": to, "value": amount}
        )
        return {
            "from": account.address,
            "to": to,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address),
            "chainId": w3.eth.chain_id
        }
    else:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])

#This function will call create_tx, sign the transaction, then send it to the designated network
def send_tx(coin, account, recipient, amount):
    tx = create_tx(coin, account, recipient, amount)
    signed = account.sign_transaction(tx)
    if coin == ETH:
        return w3.eth.sendRawTransaction(signed.rawTransaction)
    else:
        return NetworkAPI.broadcast_tx_testnet(signed)
    
    
#Connect to local Ethereum Blockchain
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))


# #Examples cr:
# Account_ETH = priv_key_to_account(ETH, (coins[ETH][0]['privkey']))
# Account_BTCTEST = priv_key_to_account(BTCTEST, (coins[BTCTEST][0]['privkey']))

# 
# send_tx(ETH, Account_ETH, '0xCE4B45cD08Dd665900a70282f0714560Bc8AE38C', 1000)
# send_tx(BTCTEST, Account_BTCTEST, 'n3xdmfgWz8ZvMnqPYxoDS8rtfARNJtDBE2', 0.0000001)
# print(priv_key_to_account(BTCTEST, (coins[BTCTEST][0]['privkey'])).get_transactions()[0])