
class SingleObject(object):
    def init(self):
        self.instance = SingleObject()

    def get_instance(self):
        return self.instance

    def show_message(self):
        print 'Hello'


class SingletonPattern():

    def __init__(self, obj):
        try:
            self.single = obj.get_instance()
        except:
            self.single = obj()

        single.show_message()



if __name__ == '__main__':
    obj = SingleObject()
    obj.init()
    S = SingletonPattern(obj)