Welcome to my sub-repository of blockchain files/projects.

Here's a breakdown of each file:

### tiny_blockchain_obj.py

This Python file contains the "tiny" blockchain class.

Big shout-out to Gerald Nash and his 2017 article "Let's Build the Tiniest Blockchain (in Less Than 50 Lines of Python)" for the tutorial. [Click here to check it out.](https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b) The file is based off of the tutorial in the article, but is heavily annotated for the sake of my own thorough understanding of how it all works.

Finally, this class is the basis of our blockchain for the next two files in this repository: tiniest_blockchain.py & snakecoin_full_server.py.

### tiniest_blockchain.py

This is an incredibly elementary blockchain program that loops through a specified number of desired blocks for the chain, uses the block class found in tiny_blockchain_obj.py to create each block, and logs each block in the console for the user to see.

Once again, Gerald Nash's previously mentioned article served as the basis with its fantastic tutorial, and the file is heavily annotated as a means for my own learning.

### snakecoin_full_server.py

This is a more fully-featured blockchain program that involves mining, proof-of-work, a consensus algorithm, and the use of JSON & Flask.

It builds upon the previous two files, and is based off the tutorial in Gerald Nash's sequal to the above article titled "Let's Make the Tiniest Blockchain Bigger". [Click here to check it out.](https://medium.com/crypto-currently/lets-make-the-tiniest-blockchain-bigger-ac360a328f4d)
