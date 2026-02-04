import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from LibInstruments import fetchAndSaveInstrumentFNOTokens

fetchAndSaveInstrumentFNOTokens()