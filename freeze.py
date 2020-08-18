# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 22:33:48 2020

@author: deeeo
"""

from flask_frozen import Freezer
from submitter import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()