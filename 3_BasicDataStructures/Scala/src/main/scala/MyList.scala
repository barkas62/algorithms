

object List extends App {
  val t1 = MyList(1,2,3)
  val t2 = MyList(4,5,6)
  val t3 = t1 append t2
  println("t3: " + t3)

}

sealed trait MyList[+T] {

  def copy: MyList[T] = this match {
    case Empty => Empty
    case Node(head, tail) => Node(head, tail.copy)
  }

  def append[U >:T](that: MyList[U]): MyList[U] = this match {
    case Empty => that.copy
    case Node(head, tail) => Node(head, tail.append(that))
  }

}

case class Node[T] (val head: T, val tail: MyList[T] ) extends MyList[T]
case object Empty extends MyList[Nothing]

// Companion object
object MyList{
  def apply[T](items: T*) : MyList[T] =
    if (items.isEmpty)
      Empty
    else
      Node(items.head, apply(items.tail : _*))
}


