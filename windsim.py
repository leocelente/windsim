#!venv/bin/python3
from pyhwm2014 import HWM14
import numpy as np
from matplotlib import pyplot as plt
import argparse
import datetime


def main(args):
    # lat = #-22.0295#-11.4
    # lon = #-47.8793#-41.28
    # lat, lon = 37.428229, -122.168858 # stanford

    lat, lon = args.coordinate
    day = args.time.timetuple().tm_yday
    ut = args.time.hour*60
    year = args.time.year

    day = time.timetuple().tm_yday
    ut = time.hour * 60
    year = time.year

    wind = HWM14(altlim=args.altitudes, altstp=1e-2, glat=lat, glon=lon, day=day, option=1, ut=ut, verbose=False, year=year)
        

    wind = HWM14(
        altlim=args.altitudes,
        altstp=1e-2,
        glat=lat,
        glon=lon,
        day=day,
        option=1,
        ut=ut,
        verbose=False,
        year=year,
    )

    plt.figure(figsize=(5, 8))
    plt.plot(wind.Uwind, wind.altbins, wind.Vwind, wind.altbins)
    plt.title(f"Atmospheric Wind Model by Altitude\nat {lat}, {lon} @ {args.time}")
    plt.legend(["Zonal", "Meridional"])
    plt.ylabel("Altitude (km)")
    plt.xlabel("Wind Speed (m/s)")
    plt.xlim([-20, 20])
    plt.grid()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Graph Wind speed by altitude at location", prog="wind"
    )
    parser.add_argument(
        "--coordinate",
        metavar=("LAT", "LON"),
        type=float,
        nargs=2,
        help="decimal coordinates latitude and longitude ",
        default=[-22.029, -47.8793],
    )

    parser.add_argument(
        "--altitudes",
        metavar=("START", "END"),
        type=float,
        nargs=2,
        help="range of altitudes in km",
        default=[0.850, 30.0],
    )

    parser.add_argument(
        "--time",
        metavar="DATETIME",
        type=datetime.datetime.fromisoformat,
        nargs=1,
        help="ISO format date-time",
        default=datetime.datetime(2021, 10, 17, hour=8),
    )

    args = parser.parse_args()

    main(args)
