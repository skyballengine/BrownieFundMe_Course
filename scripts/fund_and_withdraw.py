from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():

    fund_me = FundMe[-1]  # get latest contract created to interact with
    account = get_account()  # get proper account depending on the network
    entrance_fee = (
        fund_me.getEntranceFee()
    )  # call getEntranceFee function from contract to set minimumUSD
    print(entrance_fee)
    print(f"The current entrance fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def check_contract_balance():
    fund_me = FundMe[-1]
    account = get_account()
    contract_balance = fund_me.checkBalance()
    print(contract_balance)


def main():
    print("Checking Contract Balance.........")
    check_contract_balance()
    fund()
    print("Checking Contract Balance.........")
    check_contract_balance()
    withdraw()
    print("Checking Contract Balance.........")
    check_contract_balance()
