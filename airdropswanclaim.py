from web3 import Web3, HTTPProvider
from eth_account.messages import encode_defunct
import requests
import json
import time

web3 = Web3(Web3.HTTPProvider("https://rpc-swan-tp.nebulablock.com"))
chainId = web3.eth.chain_id

#connecting web3
if  web3.is_connected() == True:
    print("Web3 Connected...\n")
else:
    print("Error Connecting Please Try Again...")
    exit()

print(f'Airdrop SwanChain Helper Claim | @ylasgamers')
print(f'Make sure you have eth swan for fee claim the airdrop!')
        
claimaddr = web3.to_checksum_address("0x1cdC871919c43e51303e5Ba9aD96691691B9CC36")
claimabi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"address","name":"target","type":"address"}],"name":"AddressEmptyCode","type":"error"},{"inputs":[],"name":"ECDSAInvalidSignature","type":"error"},{"inputs":[{"internalType":"uint256","name":"length","type":"uint256"}],"name":"ECDSAInvalidSignatureLength","type":"error"},{"inputs":[{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"ECDSAInvalidSignatureS","type":"error"},{"inputs":[{"internalType":"address","name":"implementation","type":"address"}],"name":"ERC1967InvalidImplementation","type":"error"},{"inputs":[],"name":"ERC1967NonPayable","type":"error"},{"inputs":[],"name":"EnforcedPause","type":"error"},{"inputs":[],"name":"ExpectedPause","type":"error"},{"inputs":[],"name":"FailedInnerCall","type":"error"},{"inputs":[],"name":"InvalidInitialization","type":"error"},{"inputs":[],"name":"NotInitializing","type":"error"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"OwnableInvalidOwner","type":"error"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"OwnableUnauthorizedAccount","type":"error"},{"inputs":[],"name":"UUPSUnauthorizedCallContext","type":"error"},{"inputs":[{"internalType":"bytes32","name":"slot","type":"bytes32"}],"name":"UUPSUnsupportedProxiableUUID","type":"error"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"claimer","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"AirdropClaimed","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint64","name":"version","type":"uint64"}],"name":"Initialized","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"string","name":"phaseCode","type":"string"},{"indexed":false,"internalType":"uint256","name":"startTimestamp","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"endTimestamp","type":"uint256"}],"name":"PhaseAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"string","name":"phase","type":"string"},{"indexed":true,"internalType":"address","name":"claimer","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"PhaseClaimed","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"implementation","type":"address"}],"name":"Upgraded","type":"event"},{"inputs":[],"name":"UPGRADE_INTERFACE_VERSION","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_admin","type":"address"}],"name":"addAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"phaseCode","type":"string"},{"internalType":"uint64","name":"start","type":"uint64"},{"internalType":"uint64","name":"end","type":"uint64"}],"name":"addPhase","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"phase","type":"string"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"bytes","name":"signature","type":"bytes"}],"name":"claim","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"inToken","type":"address"},{"internalType":"uint64","name":"expiry","type":"uint64"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"isAdmin","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes","name":"","type":"bytes"}],"name":"isSignatureUsed","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"","type":"string"}],"name":"phaseInfo","outputs":[{"internalType":"string","name":"code","type":"string"},{"internalType":"uint64","name":"startTimestamp","type":"uint64"},{"internalType":"uint64","name":"endTimestamp","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"proxiableUUID","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"sweep","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newImplementation","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"upgradeToAndCall","outputs":[],"stateMutability":"payable","type":"function"}]')
claim_contract = web3.eth.contract(address=claimaddr, abi=claimabi)

def claim(sender, key, amount, signature):
    try:
        gasPrice = web3.to_wei(0.000001, 'gwei')
        nonce = web3.eth.get_transaction_count(sender)
        gasAmount = claim_contract.functions.claim('swan_airdrop', amount, signature).estimate_gas({
            'chainId': chainId,
            'from': sender,
            'gasPrice': gasPrice,
            'nonce': nonce
        })
        claimtx = claim_contract.functions.claim('swan_airdrop', amount, signature).build_transaction({
            'chainId': chainId,
            'from': sender,
            'gas': gasAmount,
            'gasPrice': gasPrice,
            'nonce': nonce
        })
        #sign & send the transaction
        tx_hash = web3.eth.send_raw_transaction(web3.eth.account.sign_transaction(claimtx, key).rawTransaction)
        #wait for transaction
        print(f'Wait For Transaction Until Mined...')
        transaction_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        #get transaction hash
        print(f'Claim airdrop swan tokens success!')
        print(f'TX-ID : https://swanscan.io/tx/{str(web3.to_hex(tx_hash))}')
    except Exception as e:
        print(f"Error: {e}")
        pass
        
def get_airdrop(sender, key, token):
    try:
        url = f"https://airdrop-api.swanchain.io/airdrop?airdrop_phase_code=swan_airdrop"
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'Origin': 'https://airdrop.swanchain.io',
            'Referer': 'https://airdrop.swanchain.io/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        }

        response = requests.get(url, headers=headers)
        result = response.json()
        is_elig = result.get('data', {}).get('total_eligible_amount')
        if 0 == is_elig:
            print(f'You not eligible the airdrop! exit...')
            exit()
        else:
            print(f'You eligible the airdrop of {is_elig} swan tokens!')
            is_kyc = result.get('data', {}).get('kyc_status')
            if None == is_kyc:
                print(f'No need kyc! check status claim...')
                is_claimed = result.get('data', {}).get('claim_status')
                if 'Claimed' == is_claimed:
                    tx_hash = result.get('data', {}).get('tx_hash')
                    print(f'You already claimed airdrop!')
                    print(f'TX-ID : https://swanscan.io/tx/{tx_hash}')
                else:
                    amount = float(is_elig) * (10**18)
                    signature = result.get('data', {}).get('signature')
                    print(f'Processing claim the airdrop...')
                    claim(sender, key, int(amount), signature)
            else:
                print(f'You need kyc first, but if still error maybe you need contact swan official. exit...')
                exit()
    except Exception as e:
        print(f"Error: {e}")
        pass
        
def get_token(msg, sender, key):
    try:
        message = encode_defunct(text=msg)
        signed_message =  web3.eth.account.sign_message(message, key)
        signature = web3.to_hex(signed_message['signature'])
        url = f"https://airdrop-api.swanchain.io/login"
        headers = {
            'Content-Type': 'application/json',
            'Origin': 'https://airdrop.swanchain.io',
            'Referer': 'https://airdrop.swanchain.io/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        }
        
        data = [sender, signature]

        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        token = result.get('access_token')
        if None == token:
            print(f'Fail to get auth token! exit...')
            exit()
        else:
            print(f'Success to get auth token! check eligible airdrop...')
            get_airdrop(sender, key, token)
    except Exception as e:
        print(f"Error: {e}")
        pass
        
def sign_claim():
    try:
        sender = web3.eth.account.from_key(input('Input Your Privatekey EVM Swanchain : '))
        url = f"https://airdrop-api.swanchain.io/wallet-register?wallet_address={sender.address}"
        
        headers = {
            'Content-Type': 'application/json',
            'Origin': 'https://airdrop.swanchain.io',
            'Referer': 'https://airdrop.swanchain.io/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        }

        response = requests.post(url, headers=headers)
        result = response.json()
        status = result.get('status')
        if 'success' == status:
            print(f'Success get sign message! get auth token...')
            msg = result.get('data')
            get_token(msg, sender.address, sender.key)
        else:
            print(f'Fail to get sign message! exit...')
            exit()
    except Exception as e:
        print(f"Error: {e}")
        pass

sign_claim()