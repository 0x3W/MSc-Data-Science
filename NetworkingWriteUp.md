## Lecture 1 - TCP/IP protocol stack
What is internet? Milions of connected computing devices (hosts, end-systems which are pcs, phones, servers) running network apps
Network devices are: routers, switches, hubs, modem
Communication links: fiber, copper, radio, satellite
Protocols control sending and receiving of msgs: eg. TCP, IP, HTTP, FTP, PPP
Internet standards: RFC: Request for comments and IETF: Internet Engineering Task Force
Internet protocol stack: Application (SMTP, FTP, HTTP) > Transport (TCP, UDP) > Network (IP, Routing protocols) > Link (Ethernet) > Physical (bits on wirte)
Each layers of stack is distributed, interacts with neighbor layers, and exchanges messages with same layer of different node.
Each layer takes data from above, adds header info to create new data unit, and passes data to unit below.
Application : Message > Transport : segment > Network : datagram / IP packet > Link : frame

## Lecture 2 - Communication services: Transport Layer
The network structures consists of network edges (apps&hosts), network core (routers, networks of networks), access network/physical media (communication links).
- Network edge > end systems (hosts) runs apps (www, email) in either client/server (http,email) or peer-peer (file sharing) mode.
- Network core > Links (bandwidth: bit/sec, multiplexing: sharing same link by different flows) and Nodes (processing capability, switching: forward data to adequate output)
-- Link Multiplexing: 
    a) Static: link bandwidth divided into channels, each channel allocated single flow, either time (TDM) or frequency (FDM) division multiplexing
    b) Dynamic: when using link whole bandwidth available, resource used as needed, data packets to identify flow into the network.
-- Node Forwarding:
    a) Direct: static multiplexing, fixed delay, forwarding pre-defined no processing needed
    b) Store and forward: dynamic multiplexing, variable delay, nodes process all packets
How is data transfered through the network?
- Circuit switching: static multiplexing, direct forwarding, reservation procedure. eg. old telephony network
- Packet switching: dynamic multiplexing, store and forward, packet header needed. eg. internet
-- Resources demand may exceed bandwidth hence packets que, store and forward means packets move one hop at the time
-- Delay caused by: transmission, propagation, nodal processing (check bit errors, determine output), queing
--- Transmission: R=link bandwidth (bps), L=packet length (bits), time to send bits into link = L/R
--- Propagation: d=length of physical link, s=propagation speed (~2x10^8 m/sec), propagation delay = d/s
--- Queing: a = average packet arrival rate, traffic intensity = La/R. eg. La/R > 1 more work arrive then proccessed, queing forever.
Curcuit switching vs Packet switching on 1 Mbit Link each user has 100Kbps when active, and its active 10% of time.
- Curcuit: 10 users vs Packet: 35 users (prob > 10 active less than 0.004)
Transport layer
Network applications
Network application - communicating distributed processes: running in network hosts in "user space", implement messages to implement app, eg email, the Web, file transfer
Application-layer protocol: one piece of an app, defines messages exchanged by apps and actions taken, user services provided by lower protocol
A process is a program that is running within host. Within the same host, two processes communicate with interprocess communication defined by OS. Processes running in different hosts communicate with application-layer protocol.
A user agent is an interface between the user and the network application. Web:browser, Email: mail reader, etc..
Client-server paradigm: Network app has two pieces client and server.
Client initiates contact with the server, typically requests a service, for web client is implement in browser, for email in mail reader.
Server provides requests service to client. eg Webserver sends requested Web page, mail server delivers email.
Transport services and protocols
Provide logical communication between app processes running on different hosts, transport protocols run in end systems, transport (data transfer between processes) vs network layer (data transfer between end systems)
Transport layer protocols: User Datagram Protocol (UDP) which is unordered and unreliable data delivery, Transmission Control Protocol which is relible in order data delivery (congestion, flow control, connection setup)
Multiplexing is gathering data from multiple processes, enveloping data with header(later used for demultiplexing).
Demultiplexing is delivering received segments to correct app layer processes.
Multiplexing/demultiplexing is based on sender, receiver port numbers, IP addresses: source, dest ports #s in each segment, the port number identifies the process, well-known port numbers for specific applications (16 bit, 0-1023 well known, 1024-65535).
UDP is "best effort" service, and its segments may be lost or delivered out of order. Its connection-less as there is no hand-shaking between sender and receiver, each UDP segment handled independently of others. Why is there UDP? No connection means less delay, simple as there is no state at either sender or receiver, small segment format, no congestion control, UDP may blast as fast as desired. Its often used for streaming multimedia apps (loss tolerant, rate sensitive), relible transfer over UDP: add relibility at application layer.
UDP checksum exists to detect errors (eg. flipped bits) in transmitted segment. Sender treat segment context as sequence of 16-bit integers, checksum: addition (1's complement sum) of segment contents, sender puts checksum value in UDP checksum field. Receiver computes checksum of received segment, check if computed sum equals checksum value in field, means error detected, yes means no error detected.

## Lecture 3 - Transport Control Protocol (TCP)
