
import unittest
from car_client_base import CarClient
from car_client_control import CarBroadcast
import random
import threading
from time import sleep

global broadcasted
broadcasted = list()


"""
    quick utility for threading the broadcast of random integer
    then saving that integer in a backlog of integers that have been broadcast
"""
def broadcast():
    br = CarBroadcast()
    sleep(0.1)
    value1 = '{0}'.format(random.randint(0,10))
    br.broadcast(value1)
    global broadcasted
    broadcasted.append(value1)
    return

"""
    The model of this server code is a persistent socket connection.
    This gets messy for unit tests, but the same basic mechanism is used here - the
    difference being that within the unit tests, a function has been written to get one
    value and then stop the subscription so that the code can continue.
"""
    
class TestTraditionalNetwork(unittest.TestCase):
    """
        set up the unit test by initializing the broadcast client,
        then initializing the consumer
    """
    
    def setUp(self):
        self.broadcast = CarBroadcast()
        self.viewer = CarClient()
        pass
    
    """
        send 10 digits via the broadcast mechanism
        verify that 10 digits were recieved
    """
    def test_sendTenDigits(self):
        
        global broadcasted
        broadcasted = list()
        
        threads = list()
        caughtDigits = list()
        for i in range(10):
            t = threading.Thread(target=broadcast)
            threads.append(t)
            t.start()
            caughtDigits.append(self.viewer.getOne())
        
        self.assertEqual(len(caughtDigits),len(broadcasted))
        
        
    """
        send 10 digits via the broadcast mechanism
        verify that the same 10 digits that were sent got recieved
    """
    def test_sameDigits(self):
        
        global broadcasted
        broadcasted = list()
        self.assertEqual( len(broadcasted), 0)
        
        threads = list()
        caughtDigits = list()
        
        for i in range(10):
            t = threading.Thread(target=broadcast)
            threads.append(t)
            t.start()
            caughtDigits.append(self.viewer.getOne())
            
        self.assertEqual(len(caughtDigits),len(broadcasted))
        for i in range(10):
            self.assertEqual(caughtDigits[i],broadcasted[i])
            
            
class TestENSNetwork(unittest.TestCase):

    def test_sendTenDigits(self):
        self.assertFalse(True)

    def test_sameDigits(self):
        self.assertFalse(True)


if __name__ == '__main__':
    unittest.defaultTestLoader.sortTestMethodsUsing = None
    unittest.main(verbosity=2)
