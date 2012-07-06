import time
import pymongo
from capsulemq.local.message import Message
from capsulemq.local.queue import Queue


class Publisher(object):

	def __init__(self, database, queue):
		self.queue = Queue(database=database, queue=queue)

	def push(self, method='PING', arguments={}, topic=None, expire=-1.0):
		message = Message()
		message.method = method
		message.arguments = arguments
		self.queue.write(message, routing_key=topic, expire=expire)



class Subscriber(object):

	def __init__(self, database, queue, callback, topic=None, check_interval=1.0):
		self.queue = Queue(database=database, queue=queue)
		self.topic = topic
		self.callbacks = [callback]
		self.check_interval = check_interval
		self.messages = None
		# todo : est-ce que ça marche ce qui suit ?
		matching = {'topic':topic}
		# direct access to the DB, so we can get a "tailable" cursor on the queue collection
		self.cursor = self.queue[database][queue].find(matching, tailable=True)

	def _get_all_messages(self):
		self.messages = self.queue.read(routing_key=self.topic)

	def register(self, callback):
		self.callbacks.append(callback)

	def listen(self, since=None):
		self._get_all_messages()
		for record_available in self.steps():
			if not record_available:
				time.sleep(self.check_interval)

	def steps(self):
		while self.cursor.alive:
			try:
				record = self.cursor.next()
				self.callback(record)
				yield True
			except StopIteration:
				yield False

				#todo: pas dit que ça marche ça...