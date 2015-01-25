#!/usr/bin/env python
"""
.. module:: leicatca1800.py
   :platform: Unix, Windows
   :synopsis: Ulyxes - an open source project to drive total stations and publish observation results. GPL v2.0 license Copyright (C) 2010-2013 Zoltan Siki <siki@agt.bme.hu>
.. moduleauthor:: Zoltan Siki <siki@agt.bme.hu>, Daniel Moka <mokadaniel@citromail.hu>

"""

from leicameasureunit import LeicaMeasureUnit

class LeicaTPS1200(LeicaMeasureUnit):
    """ This class contains the Leica TCA1800 robotic total station specific functions
    """

    def __init__(self, name = 'Leica TPS1200', typ = 'TPS'):
        """ Constructor to leica generic ts

            :param name: name of ts (str), default=TPA1800
            :param type: type od ts (str), default=TPS
        """
        # call super class init
        super(LeicaTPS1200, self).__init__(name, typ)

    # Constants for message codes
    codes = {
        'SETATR': 18005,
        'GETATR': 18006,
        'SETLOCK': 18007,
        'GETLOCK': 18008,
        'SETATMCORR': 2028,
        'GETATMCORR': 2029,
        'SETREFCORR': 2030,
        'GETREFCORR': 2031,
        'GETSTN': 2009,
        'SETSTN': 2010,
        'SETEDMMODE': 2020,
        'GETEDMMODE': 2021,
        'SETORI': 2113,
        'MOVE': 9027,
        'MEASURE': 2008,
        'GETMEASURE': 2108,
        'MEASUREANGDIST': 17017,
        'COORDS': 2082,
        'GETANGLES': 2003,
        'CHANGEFACE': 9028,
        'CLEARDIST': 2082,
        'POWERSEARCH': 9052,
        'SEARCHNEXT': 9051
    }

    # Constants for EMD modes
    # TODO check codes
    edmMode = {'STANDARD': 0, 'PRECISE': 1, 'FAST': 2, 'TRACKING': 3,
        'AVERAGING': 4, 'FASTTRACKING': 5}

    @staticmethod
    def GetCapabilities():
        """ Get instrument specialities

            :returns: List of specialities
        """
        return ['ROBOT', 'ANGLE', 'EDM', 'ATR', 'LOCK', 'RL', 'POWERSEARCH', \
            'POSITION']

    def GetPowerSearchMsg(self):
        """ Power search
        
            :returns: Power search message
        """
        return '%R1Q,{0:d}'.format(self.codes['POWERSEARCH'])
