# coding=utf-8
################################################
# Nazomi Plurk bot Project
# Produced by Dephilia
################################################
import logger,logging
logger = logging.getLogger(__name__)
from datetime import datetime
from random import randrange

def randList(list):
    return list[randrange(len(list))]

def wrapExample(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        """Function here"""
        return func(*args, **kwargs)
    return wrapped

def dt2pt(time):
    """Transform datetime to plurk time"""
    return time.strftime("20%y-%m-%dT%H:%M:%S")

class Stack:
  "A container with a last-in-first-out (LIFO) queuing policy."
  def __init__(self):
    self.list = []

  def push(self,item):
    "Push 'item' onto the stack"
    self.list.append(item)

  def pop(self):
    "Pop the most recently pushed item from the stack"
    return self.list.pop()

  def isEmpty(self):
    "Returns true if the stack is empty"
    return len(self.list) == 0

class Queue:
  "A container with a first-in-first-out (FIFO) queuing policy."
  def __init__(self):
    self.list = []

  def push(self,item):
    "Enqueue the 'item' into the queue"
    self.list.insert(0,item)

  def pop(self):
    """
      Dequeue the earliest enqueued item still in the queue. This
      operation removes the item from the queue.
    """
    return self.list.pop()

  def isEmpty(self):
    "Returns true if the queue is empty"
    return len(self.list) == 0
