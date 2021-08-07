from typing import Callable
from vector import Vector

class IMatrix:
    pass

class Matrix(IMatrix):
    __value: list
    
    @property
    def cols(self) -> int:
        return self.__value[0].length

    @property
    def rows(self) -> int:
        return len(self.__value)

    def __init__(self, value: list): 
        self.__value = []
        if len(value) == 0:
            raise MalformedMatrixException("empty matrix values")
        else: 
            length = 0
            for i in range(len(value)):
                assert isinstance(value[i], list)
                if length == 0:
                    length = len(value[i])
                elif len(value[i]) != length:
                    raise MalformedMatrixException("improper length of rows")
                self.__value.append(Vector(value[i]))
    
    @classmethod
    def zero(self, rows: int, cols: int) -> IMatrix:
        assert cols > 0 and rows > 0
        value = []
        for i in range(rows):
            value.append([0 for i in range(cols)])
        return Matrix(value)

    def __getitem__(self, key: int) -> float:
        return self.__value[key]

    def __setitem__(self, key: int, value: float):
        self.__value[key] = value
    
    def row(self, index: int) -> Vector:
        assert index > -1 and index < self.rows
        return self.__value[index]
    
    def col(self, index: int) -> Vector:
        assert index > -1 and index < self.cols
        result = Vector.zero(self.rows)
        for i in range(result.length):
            result[i] = self[i][index]
        return result

    def __add__(self, matrix: IMatrix) -> IMatrix:
        if self.cols == matrix.cols and self.rows == matrix.rows:
            result = Matrix.zero(self.rows, self.cols)
            for i in range(result.rows):
                result[i] = self[i] + matrix[i]
            return result
        else:
            raise IncompatibleMatrixException("matrices involved are incompatible")

    def __sub__(self, matrix: IMatrix) -> IMatrix:
        if self.cols == matrix.cols and self.rows == matrix.rows:
            result = Matrix.zero(self.rows, self.cols)
            for i in range(result.rows):
                result[i] = self[i] - matrix[i]
            return result
        else:
            raise IncompatibleMatrixException("matrices involved are incompatible")

    def __mul__(self, matrix: IMatrix) -> IMatrix:
        if self.cols == matrix.rows:
            result = Matrix.zero(self.rows, matrix.cols)
            for i in range(result.rows):
                for x in range(result.cols):
                    result[i][x] = self.row(i) * matrix.col(x)
            return result
        else:
            raise IncompatibleMatrixException("matrices involved are incompatible")


    def __eq__(self, matrix: IMatrix) -> bool:
        result = True
        for i in range(self.rows):
            result = result and self[i] == matrix[i]
        return result


    def __ne__(self, matrix: IMatrix) -> bool:
        return not self.__eq__(matrix)

    def transpose(self) -> IMatrix:
        result = Matrix.zero(self.cols, self.rows)
        for i in range(result.rows):
            result[i] = self.col(i)
        return result

    def map(self, function: Callable) -> IMatrix:
        result = Matrix.zero(self.rows, self.cols)
        for i in range(result.rows):
            for x in range(result.cols):
                result[i][x] = function(self[i][x])
        return result

    def __str__(self):
        strings = []
        for vector in self:
            strings.append(vector.__str__())
        return "\n".join(strings)

class MalformedMatrixException(Exception):
    pass

class IncompatibleMatrixException(Exception):
    pass