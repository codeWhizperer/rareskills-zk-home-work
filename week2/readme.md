# Reference:

## Steps
- choose a private key
-  generate the public key using that private key (not the eth address, the public key) 
- pick message m and hash it to produce h (h can be thought of as a 256 bit number)
- sign m using your private key and a randomly chosen nonce k. produce (r, s, h, PubKey)
-  verify (r, s, h, PubKey) is valid

## Sign Signature
- https://cryptobook.nakov.com/digital-signatures/ecdsa-sign-verify-messages#ecdsa-sign


## Verify Signature  
- https://cryptobook.nakov.com/digital-signaturesecdsa-sign-verify-messages#ecdsa-verify-signature


