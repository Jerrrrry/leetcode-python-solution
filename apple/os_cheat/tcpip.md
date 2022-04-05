ip
internet protocol (phone number like )

tcp  transmission contorl protocol 
The TCP/IP relationship is similar to sending someone a message written on a puzzle through the mail. The message is written down and the puzzle is broken into pieces. Each piece then can travel through a different postal route, some of which take longer than others. When the puzzle pieces arrive after traversing their different paths, the pieces may be out of order. The Internet Protocol makes sure the pieces arrive at their destination address. The TCP protocol can be thought of as the puzzle assembler on the other side who puts the pieces together in the right order, asks for missing pieces to be resent, and lets the sender know the puzzle has been received. TCP maintains the connection with the sender from before the first puzzle piece is sent to after the final piece is sent.

IP is a connectionless protocol, which means that each unit of data is individually addressed and routed from the source device to the target device, and the target does not send an acknowledgement back to the source. That’s where protocols such as the Transmission Control Protocol (TCP) come in. TCP is used in conjunction with IP in order to maintain a connection between the sender and the target and to ensure packet order.


TCP is a connection-oriented protocol, which means a connection is established and maintained until the applications at each end have finished exchanging messages.

TCP performs the following actions:

determines how to break application data into packets that networks can deliver;
sends packets to, and accepts packets from, the network layer;
manages flow control;
handles retransmission of dropped or garbled packets, as it's meant to provide error-free data transmission; and
acknowledges all packets that arrive.
In the Open Systems Interconnection (OSI) communication model, TCP covers parts of Layer 4, the transport layer, and parts of Layer 5, the session layer.

When a web server sends an HTML file to a client, it uses the hypertext transfer protocol (HTTP) to do so. The HTTP program layer asks the TCP layer to set up the connection and send the file. The TCP stack divides the file into data packets, numbers them and then forwards them individually to the IP layer for delivery.

