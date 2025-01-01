import org.scalatest.funsuite.AnyFunSuite
import org.scalatest.matchers.should.Matchers

// If you're still writing a test or you effectively want to skip it, you can write "pending"
// it's like "pass" in python
/** @version 1.2.0 */
class TwoferTest extends AnyFunSuite with Matchers {

  test("no name given") {
    Twofer.twofer() should be ("One for you, one for me.")
  }

  test("a name given") {
    Twofer.twofer("Alice") should be ("One for Alice, one for me.")
  }

  test("another name given") {
    Twofer.twofer("Bob") should be ("One for Bob, one for me.")
  }
}
