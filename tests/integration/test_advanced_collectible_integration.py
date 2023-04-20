import pytest
from brownie import network, AdvancedCollectible
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_contract
from scripts.advanced_collectible.deploy_and_create import deploy_and_create
import time

def test_can_create_advanced_collectible_integrations():
  """
  deploy the contract
  create and nft
  get a random breed back
  """
  # arrange
  if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
      pytest.skip("Only for local testing")
  # act
  advanced_collectible, creation_transaction = deploy_and_create()
  time.sleep(60)
  # assert
  assert advanced_collectible.tokenCounter() == 1
  # passed
