import fiona


def test_shpfile():
    shp = fiona.open('static_data/england_wa_2011_clipped.shp')
    assert shp.schema['properties']['name'] == 'str:56'
