from typewise_infer import ManageBattery

if __name__ == '__main__':
  BatteryStatusTest1 = ManageBattery("TO_CONTROLLER","HI_ACTIVE_COOLING",32)
  BatteryStatusTest1.classify_and_infer_and_alert()
  BatteryStatusTest2 = ManageBattery("TO_EMAIL","HI_ACTIVE_COOLING",32)
  BatteryStatusTest2.classify_and_infer_and_alert()