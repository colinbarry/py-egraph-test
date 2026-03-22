from expression import Const, Var, Add, Subtract, Multiply, Divide


def test_eval_constant():
    assert Const(5).eval({}) == 5


def test_eval_variable():
    assert Var("x").eval({"x": 3}) == 3


def test_eval_add():
    assert Add(Const(2), Const(3)).eval({}) == 5


def test_eval_subtract():
    assert Subtract(Const(7), Const(3)).eval({}) == 4


def test_eval_multiply():
    assert Multiply(Const(4), Const(3)).eval({}) == 12


def test_eval_divide():
    assert Divide(Const(10), Const(2)).eval({}) == 5


def test_eval_nested():
    expr = Multiply(Add(Const(1), Const(2)), Const(3))
    assert expr.eval({}) == 9


def test_eval_with_variables():
    expr = Add(Var("x"), Multiply(Var("y"), Const(2)))
    assert expr.eval({"x": 10, "y": 3}) == 16
