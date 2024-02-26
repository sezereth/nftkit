from nftkit.core import NFTKit

wallet_address = "your_wallet_address"
nft_kit = NFTKit(wallet_address)

owned_nfts = nft_kit.get_owned_nfts()
print(f"Owned NFTs: {owned_nfts}")

nft_metadata = nft_kit.get_nft_metadata("nft_id")
print(f"NFT Metadata: {nft_metadata}")
