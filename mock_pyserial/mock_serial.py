"""
Originally came from http://www.science.smith.edu/dftwiki/index.php/PySerial_Simulator
# fakeSerial.py
# D. Thiebaut
# A very crude simulator for PySerial assuming it
# is emulating an Arduino.
"""
from logging import debug,info,warn,error
# a Serial class emulator

#establishes responses to supported input commands
#as {'in command':'out command'}


class Serial(object):

    ## init(): the constructor.  Many of the arguments have default values
    # and can be skipped when calling the constructor.
    def __init__(self, port='COM1', baudrate = 115200, timeout=1,
                 bytesize = 8, parity = 'N', stopbits = 1, xonxoff=0,
                 rtscts = 0):
        self.name     = port
        self.port     = port
        self.timeout  = timeout
        self.parity   = parity
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.stopbits = stopbits
        self.xonxoff  = xonxoff
        self.rtscts   = rtscts
        self._isOpen  = True
        self._in_buffer = ""
        self._out_buffer = ""
        self.communication_dictionary = {}



    ## isOpen()
    # returns True if the port to the Arduino is open.  False otherwise
    def isOpen(self):
        return self._isOpen

    ## open()
    # opens the port
    def open(self):
        self._isOpen = True

    ## close()
    # closes the port
    def close(self):
        self._isOpen = False

    ## write()
    # writes a string of characters to the Arduino
    def write(self, string):
        """
        writes input string into input serial buffer

        Parameters
        ----------
        string:  (string)
            command as a string

        Returns
        -------

        Examples
        --------
        >>> ser.write('serial port command')
        """
        debug("input buffer got value: {}".format(string))
        self._in_buffer += string

    ## read()
    # reads n characters from the fake Arduino. Actually n characters
    # are read from the string _data and returned to the caller.
    def read(self, N=1):
        s = self._out_buffer[0:N]
        self._out_buffer = self._in_buffer[N:]
        debug( "read: now self._data = ", self._out_buffer)
        return s

    ## readline()
    # reads characters from the fake Arduino until a \n is found.
    def readline( self ):
        returnIndex = self._out_buffer.index( "\n" )
        if returnIndex != -1:
            s = self._out_buffer[0:returnIndex+1]
            self._out_buffer = self._out_buffer[returnIndex+1:]
            return s
        else:
            return ""

    def in_waiting(self):
        raise NotImplementedError

    def out_waiting(self):
        raise NotImplementedError

    ## __str__()
    # returns a string representation of the serial class
    def __str__( self ):
        return  "Serial<id=0xa81c10, open=%s>( port='%s', baudrate=%d," \
               % ( str(self.isOpen), self.port, self.baudrate ) \
               + " bytesize=%d, parity='%s', stopbits=%d, xonxoff=%d, rtscts=%d)"\
               % ( self.bytesize, self.parity, self.stopbits, self.xonxoff,
                   self.rtscts )
