#!/usr/bin/python3
from brownie import SimpleCollectible, AdvancedCollectible, accounts, network, config
from metadata import sample_metadata
from scripts.helpful_scripts import get_breed, OPENSEA_FORMAT


dog_metadata_dic = {
    "PUG": "https://gateway.pinata.cloud/ipfs/QmQuN7E64LZX2NWVDhkqzd7ZKR7K5Wwdork8wopZyCVf6N/PUG.json",
    "SHIBA_INU": "https://gateway.pinata.cloud/ipfs/QmQaaruwLNxPJV5bcnvvu9Cbk8nQwZK81iW9n3FyyxSt9Q/SHIBA_INU.json",
    "ST_BERNARD": "https://gateway.pinata.cloud/ipfs/QmWD8x8bpS6szs8tUFHvaojQXNVYMEeBV88ncZcPzvACvy/ST_BERNARD.json",
}

def main():
    print("Working on " + network.show_active())
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(
        "The number of tokens you've deployed is: "
        + str(number_of_advanced_collectibles)
    )
    for token_id in range(number_of_advanced_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        if not advanced_collectible.tokenURI(token_id).startswith("https://"):
            print("Setting tokenURI of {}".format(token_id))
            set_tokenURI(token_id, advanced_collectible,
                         dog_metadata_dic[breed])
        else:
            print("Skipping {}, we already set that tokenURI!".format(token_id))


def set_tokenURI(token_id, nft_contract, tokenURI):
    dev = accounts.add(config["wallets"]["from_key"])
    nft_contract.setTokenURI(token_id, tokenURI, {"from": dev})
    print(
        "Awesome! You can view your NFT at {}".format(
            OPENSEA_FORMAT.format(nft_contract.address, token_id)
        )
    )
    print('Please give up to 20 minutes, and hit the "refresh metadata" button')
