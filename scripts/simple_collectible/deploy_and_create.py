from scripts.helpful_scripts import get_account, OPENSEA_URL
from brownie import SimpleCollectible


sample_token_uri = "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"



def deploy_and_create():
  account = get_account()
  simple_collectible = SimpleCollectible.deploy({"from": account})
  tx = simple_collectible.createCollectible(
      sample_token_uri, {"from": account})
  tx.wait(1)
  print(
      f"you can view at {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter() - 1)}"
  )
  print("please wait up to 20 minutes, and hit the refresh metadata button")

def main():
  deploy_and_create()