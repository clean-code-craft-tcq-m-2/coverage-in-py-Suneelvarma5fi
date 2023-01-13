from Notify import Notify
from constants import COOLING_TYPE

class ManageBattery:

  def __init__(self, alertTarget, batteryChar, temperatureInC):
    self.alertTarget = alertTarget
    self.batteryChar = batteryChar
    self.temperatureInC = temperatureInC

  def classify_and_infer(self):

    #temperatureInC should always be positive else 
    lowerLimit, upperLimit = COOLING_TYPE[self.batteryChar]
    if self.temperatureInC < lowerLimit: return 'TOO_LOW'
    elif self.temperatureInC > upperLimit: return 'TOO_HIGH'
    else: return 'NORMAL'

  def classify_and_infer_and_alert(self):
    #print(self.batteryChar)
    breach_type = self.classify_and_infer()
    NotifyBatteryStatus = Notify(self.alertTarget,breach_type)
    return NotifyBatteryStatus.notify()