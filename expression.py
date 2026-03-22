from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import override


class Node(ABC):
    @abstractmethod
    def eval(self, context):
        pass


@dataclass
class Const(Node):
    value: float

    @override
    def eval(self, context):
        return self.value


@dataclass
class Add(Node):
    lhs: Node
    rhs: Node

    @override
    def eval(self, context):
        return self.lhs.eval(context) + self.rhs.eval(context)


@dataclass
class Subtract(Node):
    lhs: Node
    rhs: Node

    @override
    def eval(self, context):
        return self.lhs.eval(context) - self.rhs.eval(context)


@dataclass
class Multiply(Node):
    lhs: Node
    rhs: Node

    @override
    def eval(self, context):
        return self.lhs.eval(context) * self.rhs.eval(context)


@dataclass
class Divide(Node):
    lhs: Node
    rhs: Node

    @override
    def eval(self, context):
        return self.lhs.eval(context) / self.rhs.eval(context)


@dataclass
class Var(Node):
    symbol: str

    @override
    def eval(self, context):
        return context[self.symbol]

