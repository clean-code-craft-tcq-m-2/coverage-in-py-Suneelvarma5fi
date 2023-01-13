class Notify:

  def __init__(self,notification_type, breach_type):
    self.notification_type = notification_type
    self.breach_type = breach_type

  def notify_mail(self, recepient_alias):

    recepient = recepient_alias
    print(f'To: {recepient}')

    if self.breach_type == 'TOO_LOW':
      print('Hi, the temperature is too low')
    elif self.breach_type == 'TOO_HIGH':
      print('Hi, the temperature is too high')
    else:
      print('Hi, temperature is Normal')

  def notify_controller(self):
    print(f'{self.breach_type}')

  def notify(self):
    if self.notification_type == "TO_CONTROLLER":
      self.notify_controller()
      return True
    elif self.notification_type == "TO_EMAIL":
      self.notify_mail("a.b@c.com")
      return True
    else:
      return False