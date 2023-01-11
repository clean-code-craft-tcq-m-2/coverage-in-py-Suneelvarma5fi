import unittest
from typewise_infer import ManageBattery

class ManageBatteryTest(unittest.TestCase):
  def test_classify_managebattery(self):
    BatteryStatusTest10 = ManageBattery("TO_CONTROLLER","HI_ACTIVE_COOLING",32)
    self.assertTrue(BatteryStatusTest10.classify_and_infer_and_alert())

    BatteryStatusTest11 = ManageBattery("TO_EMAIL","HI_ACTIVE_COOLING",46)
    self.assertTrue(BatteryStatusTest11.classify_and_infer_and_alert())

    BatteryStatusTest12 = ManageBattery("TO_CONTROLLER","HI_ACTIVE_COOLING",-32)
    self.assertTrue(BatteryStatusTest12.classify_and_infer_and_alert())

    BatteryStatusTest13 = ManageBattery("TO_EMAIL","PASSIVE_COOLING",32)
    self.assertTrue(BatteryStatusTest13.classify_and_infer_and_alert())

    BatteryStatusTest14 = ManageBattery("TO_CONTROLLER","PASSIVE_COOLING",46)
    self.assertTrue(BatteryStatusTest14.classify_and_infer_and_alert())

    BatteryStatusTest15 = ManageBattery("TO_EMAIL","PASSIVE_COOLING",-32)
    self.assertTrue(BatteryStatusTest15.classify_and_infer_and_alert())

    BatteryStatusTest16 = ManageBattery("TO_CONTROLLER","MED_ACTIVE_COOLING",32)
    self.assertTrue(BatteryStatusTest16.classify_and_infer_and_alert())

    BatteryStatusTest17 = ManageBattery("TO_CONTROLLER","MED_ACTIVE_COOLING",46)
    self.assertTrue(BatteryStatusTest17.classify_and_infer_and_alert())
    
    BatteryStatusTest18 = ManageBattery("TO_EMAIL","MED_ACTIVE_COOLING",-32)
    self.assertTrue(BatteryStatusTest18.classify_and_infer_and_alert())

if __name__ == '__main__':
  unittest.main()
