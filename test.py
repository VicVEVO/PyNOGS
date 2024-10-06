import sys
import requests, time
from skyfield.api import EarthSatellite, load, wgs84, utc
from datetime import datetime


def main(id, password):
    credentials = {
        'identity': id,
        'password': password
    }

    id = 25544

    login_url = 'https://www.space-track.org/ajaxauth/login'
    tle_url = f'https://www.space-track.org/basicspacedata/query/class/tle_latest/NORAD_CAT_ID/{id}/orderby/ORDINAL%20desc/limit/1/format/tle'

    session = requests.Session()
    session.post(login_url, data=credentials)

    resp = session.get(tle_url)

    tle_1, tle_2 = resp.text.splitlines()

    ts = load.timescale()
    sat = EarthSatellite(tle_1, tle_2, 'ISS', ts)

    last_pos = None

    while True:
        t = ts.utc(datetime.utcnow().replace(tzinfo=utc))
        subpt = sat.at(t).subpoint()
        lat, lon, alt = subpt.latitude.degrees, subpt.longitude.degrees, subpt.elevation.km
        current_pos = (lat, lon, alt)
        if current_pos != last_pos:
            print(f"lat={lat:.6f}, lon={lon:.6f}, alt={alt:.6f}km")
            last_pos = current_pos
        time.sleep(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 test.py <email> <password>")
    else:
        main(sys.argv[1], sys.argv[2])