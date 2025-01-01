import scala.util.Try

object Twofer {
  def twofer(name: String): String = s"One for $name, one for me."
  def twofer(): String = "One for you, one for me."
  // another possible solution is
  // def twofer(name: String = "you"): String = s"One for $name, one for me."
}
