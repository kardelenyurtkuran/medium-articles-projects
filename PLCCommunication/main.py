import snap7

PRESSURE_VALUE_OK = 0
VACUUM_VALUE_OK = 0

_Plc = snap7.client.Client()

def connectPlc():
    try:
        try:
            _Plc.disconnect()
        except:
            pass
        _Plc.connect('192.168.2.1', 0, 1)
    except:
        pass

def readValue(variable):
    if (variable == PRESSURE_VALUE_OK):
        return (_Plc.db_read(200, 2, 1)[0])
    elif (variable == VACUUM_VALUE_OK):
        return (_Plc.db_read(200, 2, 1)[0])

def writeValue():
    _Plc.db_write(100, 288, b'\x00\x01')

def checkConnection():
    if (_Plc.get_connected()):
        try:
            print("Connection Successful")
        except:
            print("Connection Failed")


