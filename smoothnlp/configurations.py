import logging

class Config():
    def __init__(self):
        self.NUM_THREADS = 2
        self.POOL_TYPE = "thread"
        self.LOG_LEVEL = 30
        self.HOST = "http://kong.smoothnlp.com/nlp"
        self.logger = logging.getLogger("SmoothNLP")
        self.setLogLevel(self.LOG_LEVEL)

    def setLogLevel(self,level):
        self.LOG_LEVEL = level
        self.logger.setLevel(self.LOG_LEVEL)
        logging.basicConfig(level=self.LOG_LEVEL)

    def setNumThreads(self,threads):
        self.NUM_THREADS = threads

    def setHost(self,host):
        self.HOST = host

    def setPOOL_TYPE(self,ptype='process'):
        self.POOL_TYPE = ptype

config = Config()