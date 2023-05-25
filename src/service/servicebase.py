""" Service Base """
import abc
import logging
from util.db_util import connectDButil
# from util.utils import snake_case


class ServiceBase(abc.ABC):
    """ Abstract ServiceBase class """

    def __init__(self):
        self.class_name = type(self).__name__
        self.logger = logging.getLogger(self.class_name)
        # self.collection_name = snake_case(self.class_name)
        self.collection_name = self.class_name
        self.collection = connectDButil().get_collection(self.collection_name)
        print("sssssssssssss")
        # print("sssssssssssss",self.collection)
