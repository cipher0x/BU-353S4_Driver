from BU343S4Driver import BU343S4Driver

gps = BU343S4Driver("/dev/ttyUSB0")

while 1:
    gps.update_position()
    print("systemFixData: "+gps.get_systemFixData())
    print("utcTime: "+gps.get_utcTime())
    print("latitude: "+gps.get_latitude())
    print("latDirec: "+gps.get_latDirec())
    print("longitude: "+gps.get_longitude())
    print("longDirec: "+gps.get_longDirec())
    print("fixQuality: "+gps.get_fixQuality())
    print("trackedSatellites: "+gps.get_trackedSatellites())
    print("horizontalDilution: "+gps.get_horizontalDilution())
    print("altitudeAboveMeanSea: "+gps.get_altitudeAboveMeanSea())
    print("heightOfGeoid: "+gps.get_heightOfGeoid())
    print("\n\n")