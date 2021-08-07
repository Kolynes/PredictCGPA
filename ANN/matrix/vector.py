class IVector:
    pass
        

class Vector(IVector):
    __value: list

    def __init__(self, value: list): 
        self.__value = value

    @property
    def length(self) -> int:
        return len(self.__value)
    
    @classmethod
    def zero(self, length: int) -> IVector:
        assert length > 0
        value = []
        for x in range(length):
            value.append(0)
        return Vector(value)

    def __getitem__(self, key: int) -> float:
        return self.__value[key]

    def __setitem__(self, key: int, value: float):
        self.__value[key] = value

    def __add__(self, vector: IVector) -> IVector:
        if self.length == vector.length:
            result = Vector.zero(self.length)
            for i in range(result.length):
                result[i] = self[i] + vector[i]
            return result
        else:
            raise IncompatibleVectorException("vectors do not have equal number of elements")

    def __sub__(self, vector: IVector) -> IVector:
        if self.length == vector.length:
            result = Vector.zero(self.length)
            for i in range(result.length):
                result[i] = self[i] - vector[i]
            return result
        else:
            raise IncompatibleVectorException("vectors do not have equal number of elements")

    def __mul__(self, vector: IVector) -> float:
        if self.length == vector.length:
            value = 0
            for i in range(vector.length):
                value += self[i] * vector[i]
            return value
        else:
            raise IncompatibleVectorException("vectors do not have equal number of elements")

    def __eq__(self, vector: IVector) -> bool:
        if self.length != vector.length:
            return False
        else:
            result = True
            for i in range(vector.length):
                result = result and self[i] == vector[i]
            return result

    def __ne__(self, vector: IVector) -> bool:
        return not self.__eq__(vector)

    def __str__(self):
        return str(self.__value)


class IncompatibleVectorException(Exception):
    pass