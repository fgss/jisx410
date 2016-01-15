import jisx410


def test_convert_dms_to_decimal():
    assert round(
        jisx410.convert_dms_to_decimal((30, 15, 50)), 9) == 30.263888889


def test_convert_decimal_to_dms():
    assert jisx410.convert_decimal_to_dms(30.263888889) == (30, 15, 50)
    assert jisx410.convert_decimal_to_dms(35.95) == (35, 57, 0)


def test_get_mesh_one():
    assert jisx410.get_mesh_one(35.59, 139.71) == '5339'


def test_move_up():
    assert jisx410.move_up("5339") == '5439'

    assert jisx410.move_up("533910") == '533920'
    assert jisx410.move_up("533970") == '543900'
    assert jisx410.move_up("533977") == '543907'

    assert jisx410.move_up("53391010") == '53391020'
    assert jisx410.move_up("53391090") == '53392000'

    assert jisx410.move_up("53397010") == '53397020'
    assert jisx410.move_up("53397090") == '54390000'


def test_move_left():
    assert jisx410.move_left("5339") == '5340'

    assert jisx410.move_left("533910") == '533911'
    assert jisx410.move_left("533917") == '534010'

    assert jisx410.move_left("53391010") == '53391011'
    assert jisx410.move_left("53391019") == '53391110'

    assert jisx410.move_left("53391710") == '53391711'
    assert jisx410.move_left("53391719") == '53401010'


def test_get_mesh_sw():
    assert jisx410.get_mesh_sw("5339") == ((35, 20, 00), (139, 0, 0))
    assert jisx410.get_mesh_sw("533980") == ((36, 0, 0), (139, 0, 0))
    assert jisx410.get_mesh_sw("533907") == ((35, 20, 0), (139, 52, 30))

    assert jisx410.get_mesh_sw("53390700") == ((35, 20, 0), (139, 52, 30))

    assert jisx410.get_mesh_sw("53390711") == ((35, 20, 30), (139, 53, 15))

    assert jisx410.get_mesh_sw("53390732") == ((35, 21, 30), (139, 54, 00))


def test_get_mesh_ne():
    assert jisx410.get_mesh_ne("5339") == jisx410.get_mesh_sw("5440")

    assert jisx410.get_mesh_ne("533910") == jisx410.get_mesh_sw("533921")
    assert jisx410.get_mesh_ne("533970") == jisx410.get_mesh_sw("543901")
    assert jisx410.get_mesh_ne("533977") == jisx410.get_mesh_sw("544000")

    assert jisx410.get_mesh_ne("53391010") == jisx410.get_mesh_sw("53391021")
    assert jisx410.get_mesh_ne("53391090") == jisx410.get_mesh_sw("53392001")
    assert jisx410.get_mesh_ne("53391099") == jisx410.get_mesh_sw("53392100")

    assert jisx410.get_mesh_ne("53397010") == jisx410.get_mesh_sw("53397021")
    assert jisx410.get_mesh_ne("53397090") == jisx410.get_mesh_sw("54390001")
    assert jisx410.get_mesh_ne("53397099") == jisx410.get_mesh_sw("54390100")

    assert jisx410.get_mesh_ne("53397710") == jisx410.get_mesh_sw("53397721")
    assert jisx410.get_mesh_ne("53397790") == jisx410.get_mesh_sw("54390701")
    assert jisx410.get_mesh_ne("53397799") == jisx410.get_mesh_sw("54400000")


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


def test_get_mesh_middle():
    assert jisx410.get_mesh_middle('5339') == jisx410.get_mesh_sw("533944")
    assert jisx410.get_mesh_middle('533933') == jisx410.get_mesh_sw("53393355")
    assert jisx410.get_mesh_middle('53390732') == ((35, 21, 45),
                                                   (139, 54, 22))
    assert jisx410.get_mesh_middle("53390703") == ((35, 20, 15),
                                                   (139, 55, 7))
