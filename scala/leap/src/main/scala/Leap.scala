object Leap {
  def leapYear(year: Int): Boolean = {
    def divisibleByInt(factor: Int): Boolean = year % factor == 0

    // same as divisibleByInt(4) && (!divisibleByInt(100) || divisibleByInt(400))
    divisibleByInt(4) && !(divisibleByInt(100) && !divisibleByInt(400))
  }

  // this solution is not ideal because of the multiple if-else
  def leapYearNaive(year: Int): Boolean = {
    if (year % 4 == 0)
      if (year % 100 == 0)
        year % 400 == 0
      else
        true
    else
      false
  }
}
