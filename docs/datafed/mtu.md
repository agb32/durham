# Message Transfer Unit sizes

Default MTUs are 1500.  There can be significant advantage to setting the MTU to 9000, allowing larger packets to traverse the network - assuming all hops inbetween also have the larger MTU size set.

We would advise all data transfer nodes to have this set.

This can be non-trivial to achieve, as all intermediate switches between the node and JANET need to be set - this can take longer than expected to achieve.

