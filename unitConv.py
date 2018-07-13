"""Programming for Biochemists, lessons for Python programming.
Copyright (C) 2013, Charles McAnany. This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details. You should have received a copy of the GNU Affero General Public License along with this program. If not, see <http://www.gnu.org/licenses/>."""
#Unit conversion program. 
#Author: Donald Teffers, Ph.D
#
#Takes a value and a list of unit conversion tuples. Returns the value
#in new units
#
#Example:
#convUnits(1.1, [("meter", "mile"),("hour", "second")])
#2.460636037133235
#converts 1.1 m/s to mi/hr
#(the second conversion is switched because the time is in
#the denominator.)
#

def convUnits(initialVal, unitConversions):
    accum = initialVal
    for conversionFactor in unitConversions:
        accum = accum * getConversionFactor(conversionFactor[0],
                                            conversionFactor[1])
    return accum

def getConversionFactor(oldUnit, newUnit):
    timeUnits = {"second":1, "minute":60, "hour":3600}
    lengthUnits={"meter":1, "foot":0.3048, "mile":1609.34,
                 "lightyear":9.4605284E15, "centimeter":0.01}
    massUnits = {"kilogram":1, "pound":0.453592, "gram":0.001}
    unitTypes = (timeUnits, lengthUnits, massUnits)
    convFactor = 1
    for utype in unitTypes:
        if oldUnit in utype:
            convFactor *= utype[oldUnit]
        if newUnit in utype:
            convFactor /= utype[newUnit]
    return convFactor
