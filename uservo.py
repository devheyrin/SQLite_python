class UserVO:
    def __init__(self, id, pwd, name):
        self.__id = id;
        self.__pwd = pwd;
        self.__name = name;
    def __str__(self):
        return '%s, %s, %s' % (self.__id, self.__pwd, self.__name);
    def getId(self):
        return self.__id;
    def setId(self, id):
        self.__id = id;
    def getPwd(self):
        return self.__pwd;
    def setPwd(self, pwd):
        self.__pwd = pwd;
    def getName(self):
        return self.__name;
    def setName(self, name):
        self.__name = name;