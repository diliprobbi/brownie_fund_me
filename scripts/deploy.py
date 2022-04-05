from brownie import FundMe, network, config
from scripts.helpful_scripts import (deploy_mocks, get_account,LOCAL_BLOCKCHAIN_ENVIRONMENTS)



def deploy_fund_me():
    account =   get_account() ##"0xED4Fd1dC37d649dBFB67ACD921a08182f184d5B0"
    print("Account no. to fund: ", account)
    print(f"Active network is {network.show_active()}")

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        price_feed_address = deploy_mocks(account)

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify")
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
