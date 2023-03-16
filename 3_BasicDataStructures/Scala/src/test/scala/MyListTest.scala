import org.scalatest.GivenWhenThen
import org.scalatest.funsuite.AnyFunSuite
import org.scalatest._

class MyListTest extends AnyFunSuite with GivenWhenThen {

  test("Test MyList Copy") {
    Given("a list of elements 1, 2, 3")
    val t1 = MyList(1,2,3)
    When("copied")
    val t2 = t1.copy
    Then("copied list should be equal to source list")
    assert(t1 == t2)
  }

  test("Test Append") {
    val t1 = MyList(1,2,3)
    val t2 = MyList(4,5,6)
    val t3 = t1 append t2
    assert(t3 == MyList(1,2,3,4,5,6))
  }

  test("Append Empty List") {
    val t1 = MyList(1,2,3)
    val t2 = Empty
    val t3 = t1 append t2
    assert(t3 == MyList(1,2,3))
  }

  test("Append To Empty List") {
    val t1 = MyList(1,2,3)
    val t2 = Empty
    val t3 = t2 append t1
    assert(t3 == MyList(1,2,3))
  }
}
