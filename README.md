# Group_Key_Gen_Reconciliation

Unlike conventional public key cryptography, dynamic wireless private key generation is based on the random characteristics of wireless channels.
Key generation usually works in a pairwise mode between two users, say
Alice and Bob, and is based on three principles, i.e., temporal variation,channel reciprocity, and spatial decorrelation. Without loss of generality,assume that Alice is selected as the initiator and Bob is a trusted/authorized
user. 
The process takes place in four stages, namely channel probing, quantization, information reconciliation, and privacy amplification. Pairwise
(Alice-and-Bob) key generation protocols are not directly extendable to group
key generation scenarios.
A naive solution is first to apply pairwise key generation schemes to generate
a secure channel between each pair of nodes and then exchange some information
to agree on the same group key.
However, the computation and communication overhead of this approach
increases exponentially with the group size and so does the risk of information
exposure to eavesdroppers.
We propose a solution that employs the correlation degree between coefficients of the same channel and by doing a quantization by indexes condense the information reconciliation, privacy amplification, and group key distribution
phase into a single step. To achieve this, we will use a cryptographic algorithm
called the fuzzy vault algorithm. 
To summarize: Channel probing → Quantization → Fuzzy vault