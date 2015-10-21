import math

M2_STEP_LAT = 300  # 5min
M2_STEP_LON = 450  # 7min30sec
M3_STEP_LAT = 30  # sec
M3_STEP_LON = 45  # sec


def convert_dms_to_decimal(elem):
    """Convert latitude/ longitude dms form to dms form

    Keyword arguments:
    elem -- latitude or longitude : (degree, min, sec)
    """
    return elem[0] + elem[1]/60 + elem[2]/3600


def convert_decimal_to_dms(elem):
    """Convert latitude/ longitude decimal form to dms form

    Keyword arguments:
    elem -- latitude or longitude in decimal form
    """
    d = int(elem)
    m = int((elem - d) * 60)
    s = int((elem - d - m/60) * 3600)

    return (d, m, s)


def get_mesh_one(lat, lon):
    """ Get Mesh 1
    Latitude to decimal * 1.5 and Longitude - 100
    """
    return str(int(lat*1.5)) + str(int(lon - 100))


def get_mesh_boundaries(mesh):
    """Get the south latitude boundary and the west longitude boundary of the
    given mesh
    """
    # mesh1 boundaries
    lat = convert_decimal_to_dms(int(mesh[0:2])/1.5)
    lon = convert_decimal_to_dms(int(mesh[2:4]) + 100)

    # mesh2 boundaries
    if len(mesh) >= 6:

        lat_m = int(mesh[4]) * 5
        lat_m = lat_m + lat[1]
        if lat_m >= 60:
            lat = (lat[0]+1, lat_m - 60, lat[2])
        else:
            lat = (lat[0], lat_m, lat[2])

        lon_s = int(mesh[5]) * 450
        lon_s = lon_s + lon[2]
        if lon_s >= 60:
            lon = (lon[0], lon[1] + lon_s//60, lon_s % 60)
        else:
            lon = (lon[0], lon[1], lon_s)

        if len(mesh) == 8:
            lat_s = int(mesh[6]) * 30
            lat_s = lat[2] + lat_s
            if lat_s >= 60:
                lat = (lat[0], lat[1] + lat_s//60, lat_s % 60)
            else:
                lat = (lat[0], lat[1], lat_s)

            lon_s = int(mesh[7]) * 45
            lon_s = lon[2] + lon_s
            if lon_s >= 60:
                lon = (lon[0], lon[1] + lon_s//60, lon_s % 60)
            else:
                lon = (lon[0], lon[1], lon_s)

    return (lat, lon)


def get_diff_dms(a, b):
    """Get difference in second between latitude or longitude in (d,m,s)form"""
    return (b[0]*3600 + b[1]*60 + b[2]) - (a[0]*3600 + a[1]*60 + a[2])


def get_mesh_two(lat, lon):
    """Get Mesh 2
    Latitude 0 to 7 : 40m, step : 5m
    Longitude 0 to 7 : 1 degree, step : 7m30s
    """
    mesh_one = get_mesh_one(lat, lon)
    boundaries = get_mesh_boundaries(mesh_one)

    lat_diff = get_diff_dms(boundaries[0], convert_decimal_to_dms(lat))
    lon_diff = get_diff_dms(boundaries[1], convert_decimal_to_dms(lon))

    lat_position = math.floor(lat_diff / M2_STEP_LAT)
    lon_position = math.floor(lon_diff / M2_STEP_LON)

    return mesh_one + str(lat_position) + str(lon_position)


def get_mesh_three(lat, lon):
    """Get Mesh 3
    Latitude 0 to 9 : 5m, step : 30sec
    Longitude 0 to 9 : 7m30s, step : 45sec
    """
    mesh_two = get_mesh_two(lat, lon)
    boundaries = get_mesh_boundaries(mesh_two)

    lat_diff = get_diff_dms(boundaries[0], convert_decimal_to_dms(lat))
    lon_diff = get_diff_dms(boundaries[1], convert_decimal_to_dms(lon))

    lat_position = math.floor(lat_diff / M3_STEP_LAT)
    lon_position = math.floor(lon_diff / M3_STEP_LON)

    return mesh_two + str(lat_position) + str(lon_position)


def get_mesh_middle(mesh):
    """Gets a middle point for a mesh
    Send back a tuple (lat, lon)"""

    if len(mesh) == 4:
        return get_mesh_boundaries(mesh+'44')
    elif len(mesh) == 6:
        return get_mesh_boundaries(mesh+'55')
    else:
        boundaries = get_mesh_boundaries(mesh)
        lat = boundaries[0]
        lon = boundaries[1]

        lat_s = lat[2] + 15
        lat = (lat[0], lat[1], lat_s)

        lon_s = lon[2] + 22
        if lon_s >= 60:
            lon = (lon[0], lon[1] + lon_s//60, lon_s % 60)
        else:
            lon = (lon[0], lon[1], lon_s)

        return (lat, lon)
