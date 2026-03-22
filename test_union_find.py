from union_find import UnionFind


def test_create_instance():
    uf = UnionFind()
    assert uf


def test_unique_ids():
    uf = UnionFind()
    e0 = uf.make_set()
    e1 = uf.make_set()
    e2 = uf.make_set()
    assert e0 != e1
    assert e0 != e2
    assert e1 != e2


def test_new_elements_are_representative():
    uf = UnionFind()
    e0 = uf.make_set()
    assert uf.find(e0) == e0


def test_find_and_merge():
    uf = UnionFind()
    e0 = uf.make_set()
    e1 = uf.make_set()
    e2 = uf.make_set()

    assert uf.find(e0) == e0
    assert uf.find(e1) == e1
    assert uf.find(e2) == e2

    s01 = uf.merge(e0, e1)
    assert uf.find(e0) == s01
    assert uf.find(e1) == s01

    s012 = uf.merge(e0, e2)
    assert uf.find(e0) == s012
    assert uf.find(e1) == s012
    assert uf.find(e2) == s012


def test_merge_self_is_idempotent():
    uf = UnionFind()
    e0 = uf.make_set()
    assert uf.merge(e0, e0) == e0
