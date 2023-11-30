import time
from web3 import Web3
from web3.auto import w3 as w
import os
from dotenv import load_dotenv

load_dotenv()

my_ronin_address = os.getenv("PUBLIC_KEY")

private_key = os.getenv("PRIVATE_KEY")
private_key = bytearray.fromhex(private_key.replace("0x", ""))

atiasblessings = "0x9d3936dbd9a794ee31ef9f13814233d435bd806c"
atiasblessings = w.to_checksum_address(atiasblessings)

w3 = Web3(Web3.HTTPProvider('https://proxy.roninchain.com/free-gas-rpc'))

while True:
    signed_txn = w3.eth.account.sign_transaction(
    {
        'value': Web3.to_wei('0', 'gwei'),
        'chainId': 2020,
        'gas': 300000,
        'gasPrice': Web3.to_wei('0', 'gwei'),
        'nonce': w3.eth.get_transaction_count(w.to_checksum_address(my_ronin_address)),
        'to': atiasblessings,
        'data': '0x56996d45'
        },
    private_key=private_key)

    w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    txn = w3.to_hex(w3.keccak(signed_txn.rawTransaction))
    print(txn)
    time.sleep(87300) # Sleep for 24 H and 15 mins


