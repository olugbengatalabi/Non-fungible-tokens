import pytest
from brownie import network, SimpleCollectible
from scripts.helpful_scripts import get_account
from scripts.simple_collectible.deploy_and_create import deploy_and_create
def test_can_create_simple_collectible():
  if network.show_active() not in ["development"] or "fork" in network.show_active():
      pytest.skip("Only for local testing")
  simple_collectible = deploy_and_create()
  assert simple_collectible.ownerOf(0) == get_account()