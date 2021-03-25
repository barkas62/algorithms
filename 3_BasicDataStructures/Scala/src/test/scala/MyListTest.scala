import org.scalatest.FunSuite
//import MyList._

class MyListTest extends FunSuite {

  test("Test MyList Copy") {
    val t1 = MyList(1,2,3)
    val t2 = t1.copy
    assert(t1 == t2)
  }

  test("testAppend") {
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
