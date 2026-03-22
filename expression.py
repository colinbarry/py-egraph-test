from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import override


class Node(ABC):
    @abstractmethod
    def eval(self, context):
        pass

    @abstractmethod
    def key(self, children):
        pass

    @abstractmethod
    def children(self):
        pass


@dataclass
class Const(Node):
    value: float

    @override
    def eval(self, context):
        return self.value

    @override
    def key(self, children):
        return 'Const', self.value

    @override
    def children(self):
        return []


@dataclass
class Var(Node):
    symbol: str

    @override
    def eval(self, context):
        return context[self.symbol]

    @override
    def key(self, children):
        return 'Var', self.symbol

    @override
    def children(self):
        return []

@dataclass
class BinaryOp(Node):
    lhs: Node
    rhs: Node

    @override
    def key(self, children):
        return type(self).__name__, *children

    @override
    def children(self):
        return [self.lhs, self.rhs]


@dataclass
class Add(BinaryOp):
    @override
    def eval(self, context):
        return self.lhs.eval(context) + self.rhs.eval(context)


@dataclass
class Subtract(BinaryOp):
    @override
    def eval(self, context):
        return self.lhs.eval(context) - self.rhs.eval(context)


@dataclass
class Multiply(BinaryOp):
    @override
    def eval(self, context):
        return self.lhs.eval(context) * self.rhs.eval(context)


@dataclass
class Divide(BinaryOp):
    @override
    def eval(self, context):
        return self.lhs.eval(context) / self.rhs.eval(context)



