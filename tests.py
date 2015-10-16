import jisx410


def test_convert_dms_to_decimal():
    assert round(
        jisx410.convert_dms_to_decimal((30, 15, 50)), 9) == 30.263888889


def test_convert_decimal_to_dms():
    assert jisx410.convert_decimal_to_dms(30.263888889) == (30, 15, 50)
    assert jisx410.convert_decimal_to_dms(35.95) == (35, 57, 0)


def test_get_mesh_one():
    assert jisx410.get_mesh_one(35.59, 139.71) == '5339'


def test_get_mesh_boundaries():
    assert jisx410.get_mesh_boundaries("5339") == ((35, 20, 00),
                                                   (139, 0, 0))
    assert jisx410.get_mesh_boundaries("533980") == ((36, 0, 0),
                                                     (139, 0, 0))
    assert jisx410.get_mesh_boundaries("533907") == ((35, 20, 0),
                                                     (139, 52, 30))


def test_get_diff_dms():
    assert jisx410.get_diff_dms((35, 20, 0), (35, 35, 24)) == 924
    assert jisx410.get_diff_dms((139, 0, 0), (139, 42, 36)) == 2556


def test_get_mesh_two():
    assert jisx410.get_mesh_two(35.59, 139.71) == '533935'
    assert jisx410.get_mesh_two(35.883333, 139.55) == '533964'
    assert jisx410.get_mesh_two(35.95, 139.983333) == '533977'
    assert jisx410.get_mesh_two(35.3375, 139.883333) == '533907'


def test_get_mesh_three():
    assert jisx410.get_mesh_three(35.3375, 139.883333) == '53390700'
