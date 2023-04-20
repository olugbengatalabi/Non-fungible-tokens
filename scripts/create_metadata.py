from brownie import AdvancedCollectible, network
from scripts.helpful_scripts import get_breed
from metadata.sample_metadata import metadata_template
from pathlib import Path

def main():
  advanced_collectible = AdvancedCollectible[-1]
  number_of_advanced_collectible = advanced_collectible.tokenCounter()
  print("you've created {number_of_advanced_collectibles} collection")
  for token_id in range(number_of_advanced_collectible):
    breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
    # advanced collectible.tokenidtobreed returns an integer
    print(breed)
    metadata_file_name = (
      f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
      )
    collectible_metadata = metadata_template
    if Path(metadata_file_name).exists():
      print(f"{metadata_file_name} already exists! Delete it to overwrite")
    else:
      print(f"creating metadata file: {metadata_file_name}")
      collectible_metadata["name"] = breed
      collectible_metadata["description"] = f"An adorable {breed} pup!"
      
      collectible_metadata["image_uri"]
