import datetime

class Person (object):
  def __init__(self, name):
    """ Create a person with a name and birthday"""
    self.name = name
    self.birthday = None
    self.lastName = name.split(' ')[-1]
  
  def __str__(self):
    """ returns self's full name as a string"""
    return self.name

  def __lt__(self, other):
    if self.lastName == other.lastName:
      return self.name < other.name
    return self.lastName < other.lastName

  def getLastName(name):
    """ return self's last name"""
    return self.lastName

  def setBirthday(self, month, day, year):
    self.birthday = datetime.date(year, month, day)

  def getAge(age):
    """ Returns self's birthday in days"""
    if self.birthday == None:
      raise ValueError
    return (datetime.date.today() - self.birthday).days

class MITPerson(Person):
  nextIDnum = 0
  
  def __init__(self, name):
    Person.__init__(self, name)
    self.IDNum = MITPerson.nextIDnum
    MITPerson.nextIDnum += 1

  def getIDNum(self):
    return self.IDNum

  def __lt__(self, other):
    return self.IDNum < other.IDNum

  def speak(self, utterance):
    return (self.getLastName() + " says: " + utterance)


a = Person('James Smith')
b = Person('John Smith')

personList = [b, a, a]

print(personList)