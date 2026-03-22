from egraph import EGraph
from expression import Const, Add


def test_add_returns_id():
    eg = EGraph()
    id = eg.add(Const(42))
    assert id is not None


def test_add_same_const_returns_same_id():
    eg = EGraph()
    id1 = eg.add(Const(42))
    id2 = eg.add(Const(42))
    assert id1 == id2


def test_add_different_consts_returns_different_ids():
    eg = EGraph()
    id1 = eg.add(Const(1))
    id2 = eg.add(Const(2))
    assert id1 != id2


def test_add_expression_shares_children():
    eg = EGraph()
    id_const1 = eg.add(Const(1))
    id_const2 = eg.add(Const(2))
    id_add = eg.add(Add(Const(1), Const(2)))
    assert id_add != id_const1
    assert id_add != id_const2
