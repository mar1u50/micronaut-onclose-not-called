## Test project for Micronaut WebSocket @OnClose handler

### Repro steps

```
1. Start the server.
2. Start the client.
3. Configure clumsy to drop 50% of the packets and use filter tcp and (tcp.DstPort == 34242 or tcp.SrcPort == 34242).
4. Press "Start" button on clumsy.
5. Kill the client (python).
```

### Actual Behavior
OnClose handler is NOT called when the python process is killed and the TCP Connection is destroyed.

### Expected behavior
OnClose handler would be called.



