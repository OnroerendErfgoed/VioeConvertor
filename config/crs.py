import pyproj

wgs84 = pyproj.Proj('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')
lambert72 = pyproj.Proj('+proj=lcc +lat_1=51.16666723333333' +
                        ' +lat_2=49.8333339 +lat_0=90 +lon_' +
                        '0=4.367486666666666 +x_0=150000.013' +
                        ' +y_0=5400088.438 +ellps=intl ' +
                        '+towgs84=-106.869,52.2978,-103.724,0.33657,' +
                        '-0.456955,1.84218,-1.2747 +units=m +no_defs ')
