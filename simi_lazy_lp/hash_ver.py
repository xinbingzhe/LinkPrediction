
class HashVertex():
    def __init__(self):
        self.__hash_dict = {}
        self.i = 0
    def hash(self,vertex_name):
        if vertex_name not in self.__hash_dict:
            self.__hash_dict[vertex_name] = self.i
            self.i += 1
        return self.__hash_dict[vertex_name]
    def get_hash_dict(self):
        return self.__hash_dict
    def get_hash_dict_len(self):
        return len(self.__hash_dict)


'''Hash = HashVertex()

a = "ajsg"
b = "asfasf"
c = "safsafsf"
Hash.hash(a)
Hash.hash(b)
Hash.hash(c)
hd = Hash.get_hash_dict()


print(hd)'''