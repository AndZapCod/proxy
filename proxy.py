class Proxy:
    def __init__(self, instance):
        self.instance = instance

    def proxy(self):
        object_instance = self.instance
        new_instance_list = []
        print('Proxy...')
        for element in object_instance.list:
            if type(element) == float:
                new_instance_list.append(element)
            else:
                new_instance_list.append(float(element))
        self.instance.list = new_instance_list
        print('Done.')
