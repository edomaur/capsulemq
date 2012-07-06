CapsuleMQ
=========

A simple message queuing system, built on top of MongoDB and based upon B.Coe's Karait source code.

Tribute
-------

CapsuleMQ is the Python part of Benjamin Coe's Karait ( http://github.com/bcoe/karait ) with additional code for
inter-host communication and routing. I did not directly contribute to Karait so I can ignore Node.js and Ruby
implementation, but anyone is free to take it back :-)


Usage
-----

_Writing to a queue_

```python
from capsulemq import Message, Queue

queue = Queue(
    host='localhost', # MongoDB host. Defaults to localhost.
    port=27017, # MongoDB port. Defaults to 27017.
    database='capsulemq', # Database that will store the capsulemq queue. Defaults to capsulemq.
    queue='messages', # The capped collection that capsulemq writes to. Defaults to messages.
    average_message_size=8192, # How big do you expect the messages will be in bytes? Defaults to 8192.
    queue_size=4096 # How many messages should be allowed in the queue. Defaults to 4096.
)

queue.write({
	'name': 'Benjamin',
	'action': 'Rock'
})

# or

message = Message()
message.name = 'Benjamin'
message.action = 'Rock!'

queue.write(message, routing_key='my_routing_key', expire=3.0)
```

_Reading from a queue_

```python
from capsulemq import Message, Queue

queue = Queue()

message = queue.read()[0]
print "%s" % (message.name)

message.delete()

# or

message = queue.read(routing_key='my_routing_key')[0]
print "%s" % (message.action)

message.delete()
```

See unit tests for more documentation.

Copyright
---------

Copyright (c) 2011 Attachments.me. See LICENSE.txt for
further details.
