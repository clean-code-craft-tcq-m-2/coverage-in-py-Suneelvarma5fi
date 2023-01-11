import unittest
from typewise_infer import ManageBattery

class ManageBatteryTest(unittest.TestCase):
  def test_classify_breachtype(self):
    BatteryStatusTest1 = ManageBattery("TO_CONTROLLER","HI_ACTIVE_COOLING",32)
    self.assertTrue(BatteryStatusTest1.classify_and_infer_and_alert())

    BatteryStatusTest2 = ManageBattery("TO_EMAIL","HI_ACTIVE_COOLING",46)
    self.assertTrue(BatteryStatusTest2.classify_and_infer_and_alert())

    BatteryStatusTest3 = ManageBattery("TO_CONTROLLER","HI_ACTIVE_COOLING",-32)
    self.assertTrue(BatteryStatusTest3.classify_and_infer_and_alert())

    BatteryStatusTest4 = ManageBattery("TO_EMAIL","PASSIVE_COOLING",32)
    self.assertTrue(BatteryStatusTest4.classify_and_infer_and_alert())

    BatteryStatusTest5 = ManageBattery("TO_CONTROLLER","PASSIVE_COOLING",46)
    self.assertTrue(BatteryStatusTest5.classify_and_infer_and_alert())

    BatteryStatusTest6 = ManageBattery("TO_EMAIL","PASSIVE_COOLING",-32)
    self.assertTrue(BatteryStatusTest6.classify_and_infer_and_alert())

    BatteryStatusTest7 = ManageBattery("TO_CONTROLLER","MED_ACTIVE_COOLING",32)
    self.assertTrue(BatteryStatusTest7.classify_and_infer_and_alert())

    BatteryStatusTest8 = ManageBattery("TO_CONTROLLER","MED_ACTIVE_COOLING",46)
    self.assertTrue(BatteryStatusTest8.classify_and_infer_and_alert())
    
    BatteryStatusTest9 = ManageBattery("TO_EMAIL","MED_ACTIVE_COOLING",-32)
    self.assertTrue(BatteryStatusTest9.classify_and_infer_and_alert())

if __name__ == '__main__':
  unittest.main()