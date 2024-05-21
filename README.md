# Group_Key_Gen_Reconciliation

Key generation usually works in a pairwise mode between two users, say Alice and Bob, and is based on three principles, i.e., temporal variation, channel reciprocity, and spatial decorrelation. 
Without loss of generality, assume that Alice is selected as the initiator and Bob is a trusted/authorized user. The process takes place in four stages, namely channel probing, quantization, information reconciliation, and privacy amplification. Pairwise (Alice-and-Bob)  key generation protocols are not directly extendable to group key generation scenarios.


A naive solution is first to apply pairwise key generation schemes to generate a secure channel between each pair of nodes and then exchange some information to agree on the same group key.
However, the computation and communication overhead of this approach increases exponentially with the group size and so does the risk of information exposure to eavesdroppers.

In this research, we propose to develop new theory and design new protocols for group key generation and reconciliation for three types of communication networks: 

    1. the three-node network;
    2. the multi-node ring network; 
    3. the multi-node mesh network.
