# Group_Key_Gen_Reconciliation
Unlike conventional public key cryptography, dynamic wireless private key generation relies on the random characteristics of wireless channels. Key generation typically operates in a pairwise mode between two users, such as Alice and Bob, and is based on three principles: temporal variation, channel reciprocity and spatial decorrelation. Pairwise (Alice-and-Bob) key generation protocols are not directly extendable to group key generation scenarios. 
For this reason, over time, several solutions have been proposed to address this problem. Some solutions  first apply pairwise key generation schemes to generate a secure channel between each pair of nodes and then exchange some information to agree on the same group key.
Other solutions utilize a common shared features by all nodes as a random information source to generate group keys between different nodes.

In this paper we present a novel solution, that eliminates the need to generate pairwise keys for each channel before sharing the group key or to have a common source shared by all nodes to create the group key. In our scheme, we turn into a spanning tree the network topology. The spanning tree will have as root a leader node  chosen from the network. The leader node chooses the secret key and by using the fuzzy vault algorithm (a cryptographic construct) share it to the other nodes. By using the common shared characteristics of the channel and through fuzzy vault algorithm; starting from the root node the fuzzy vault is sent in each tree's branches. Our findings demonstrate that each node non leader belonging to the network can reconstruct with a high probability a 128-bit key. At the end of the process, all nodes will possess the same key, which can be used as the group key. On the contrary, we will show that Eve can determine the value of the key only with a probability close to epsilon
