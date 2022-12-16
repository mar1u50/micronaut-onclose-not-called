## Test project for Micronaut WebSocket server

### Repro steps

Start the server.

Start the client.

Configure clumsy to drop 50% of the packets and use filter tcp and (tcp.DstPort == 34242 or tcp.SrcPort == 34242).

Kill the client (python).

### Actual Behavior
OnClose handler is NOT called when the python process is killed and the TCP Connection is destroyed.

### Expected behavior
OnClose handler would be called.



