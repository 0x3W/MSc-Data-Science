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
