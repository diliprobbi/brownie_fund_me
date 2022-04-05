from brownie import network, accounts,config, MockV3Aggregator, Wei

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork","mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
DECIMALS = 18
STARTING_PRICE = 200

def get_account():
        if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS 
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS):
                print(accounts)
                return accounts[0]
        else:
                return accounts.add(config["wallets"]["from_key"])

def deploy_mocks(_account):
        print("Deploying Mocks...")
        if len(MockV3Aggregator) <= 0: 
            MockV3Aggregator.deploy(DECIMALS, Wei("{} gwei".format(STARTING_PRICE)), {"from": _account})

        price_feed_address = MockV3Aggregator[-1].address
        print("Mocks Deployed!")
        return price_feed_address