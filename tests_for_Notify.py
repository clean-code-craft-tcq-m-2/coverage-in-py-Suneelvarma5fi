import unittest
from Notify import Notify

class NotifyTest(unittest.TestCase):
  def test_notify_to_controller(self):
    NotifyTest1 = Notify("TO_CONTROLLER","TOO_LOW")
    NotifyTest2 = Notify("TO_CONTROLLER","TOO_HIGH")
    NotifyTest3 = Notify("TO_CONTROLLER","NORMAL")
    self.assertTrue(NotifyTest1.notify())
    self.assertTrue(NotifyTest2.notify())
    self.assertTrue(NotifyTest3.notify())

  def test_notify_to_email(self):
    NotifyTest4 = Notify("TO_EMAIL","TOO_LOW")
    NotifyTest5 = Notify("TO_EMAIL","TOO_HIGH")
    NotifyTest6 = Notify("TO_EMAIL","NORMAL")
    self.assertTrue(NotifyTest4.notify())
    self.assertTrue(NotifyTest5.notify())
    self.assertTrue(NotifyTest6.notify())

if __name__ == '__main__':
  unittest.main()