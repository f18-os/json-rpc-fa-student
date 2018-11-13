# minimalistic client example from 
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket
import json
from bsonrpc import JSONRpc
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)
from node import *

leaf1 = node("leaf1")
leaf2 = node("leaf2")

root = node("root", [leaf1, leaf1, leaf2])
increment(root)

# Cut-the-corners TCP Client:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50001))

rpc = JSONRpc(s,framing_cls=JSONFramingNone)
server = rpc.get_peer_proxy()
# Execute in server:
result = server.swapper('Hello World!')
# "!dlroW olleH"
print(result)

nowJSON = json.dumps(root, default=lambda n: n.__dict__)

print("")
print(nowJSON)
print("")
print(server.nop(nowJSON))

rpc.close() # Closes the socket 's' also


