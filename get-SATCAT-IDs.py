import sys
import requests
import time

NUMBER_SATELLITES = 61389

def main(id, password):
    session = requests.Session()
    session.post('https://www.space-track.org/ajaxauth/login', data={'identity': id, 'password': password})

    sat_ids = [str(satellite_id) for satellite_id in range(1, 61389) if session.get(f'https://www.space-track.org/basicspacedata/query/class/tle_latest/NORAD_CAT_ID/{satellite_id}/orderby/ORDINAL%20desc/limit/1/format/tle').status_code == 200]

    with open('sat_ids.txt', 'w') as f:
        f.write('\n'.join(sat_ids))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 test.py <space-track.org email> <password>")
    else:
        main(sys.argv[1], sys.argv[2])
