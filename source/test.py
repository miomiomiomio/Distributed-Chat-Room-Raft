from threading import Timer
import random
import time

class test():

    def __init__(self):
        self.timeout = 3
        self.heartbeat_timeout = random.uniform(self.timeout, 2 * self.timeout)
        self.heartbeat_timer = None
        print(self.heartbeat_timeout)
        self.heartbeat_timer = Timer(self.heartbeat_timeout, self.sendHeartbeat)
        self.heartbeat_timer.daemon = True
        self.heartbeat_timer.start()

        # self.sendHeartbeat()
        while(1):
            print('click')
            time.sleep(5)

    def sendHeartbeat(self):
        """
        Send heartbeat message to all pears in the latest configuration
        if the latest is a new configuration that is not committed
        go to the join configuration instead
        :type ignore_last: bool
              - this is used for the broadcast immediately after a new
              config is committed. We need to send not only to sites
              in the newly committed config, but also to the old ones
        """

        print('bong')
        self.resetHeartbeatTimeout()

    def resetHeartbeatTimeout(self):
        """z
        reset heartbeat timeout
        """
        print('reset heartbeat')
        if self.heartbeat_timer:
            self.heartbeat_timer.cancel()
        self.heartbeat_timer = Timer(self.heartbeat_timeout, self.sendHeartbeat)
        self.heartbeat_timer.daemon = True
        self.heartbeat_timer.start()

t = test()
