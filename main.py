from proxy import Proxy
from data import Data

data_list = [0, 1, 3, 4, 2.5, 6, 7.8, 9.9]
object_data = Data(data_list)
object_proxy = Proxy(object_data)
print(object_data.list)
object_proxy.proxy()
print(object_data.list)


