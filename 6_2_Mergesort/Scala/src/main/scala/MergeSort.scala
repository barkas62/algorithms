import scala.annotation.tailrec
import scala.reflect.ClassTag
import scala.util.Random

object MergeSort {

  // Traditional mergesort of arrays
  def mergeSort[T <% Ordered[T] : ClassTag](x: Array[T]): Unit ={
    val y = new Array[T](x.length)
    mSort(x, y, 0, x.length-1 )

    def mSort(x: Array[T], y: Array[T], beg: Int, end: Int): Unit ={

      if (end - beg > 0){
        val mid = (beg + end) / 2
        mSort(x, y, beg,   mid)
        mSort(x, y, mid+1, end)

        merge(x, y, beg, mid, end)
        Array.copy(y, beg, x, beg, end-beg+1)
      }

    }

    def merge(src: Array[T], dst: Array[T], beg: Int, mid: Int, end: Int): Unit ={
      var i0 = beg
      var i1 = beg
      var i2 = mid+1

      while (i1 <= mid && i2 <= end) {
        if (src(i1) < src(i2)) {
          dst(i0) = src(i1)
          i1 += 1
          i0 += 1
        } else {
          dst(i0) = src(i2)
          i2 += 1
          i0 += 1
        }
      }

      if (i1 <= mid)
        Array.copy(src, i1, dst, i0, mid-i1+1)

      if (i2 <= end)
        Array.copy(src, i2, dst, i0, end-i2+1)
    }

  }


  def mergeSortL[T <% Ordered[T]](xs: List[T]) : List[T] = xs match {
    case Nil => Nil
    case x :: Nil => List(x)
    case _ => {

      @tailrec
      def mergeL( xs1: List[T], xs2: List[T], acc: List[T]) : List[T] = (xs1, xs2) match {
        case (Nil, _) => acc ++ xs2
        case (_, Nil) => acc ++ xs1
        case(x1::_xs1, x2::_xs2) =>
          if (x1 < x2) mergeL(_xs1, xs2, acc :+ x1)
          else mergeL(xs1, _xs2, acc :+ x2)
      }

      val (xs1, xs2) = xs splitAt (xs.length / 2)
      mergeL( mergeSortL(xs1), mergeSortL(xs2), Nil)
    }

  }

  @tailrec
  def isSorted[T <% Ordered[T]](xs: List[T]) : Boolean = xs match {
    case x1 :: x2 ::_xs => { x1 <= x2 && isSorted(x2::_xs) }
    case _ => true
  }

}


object Try extends App {
  import MergeSort._

  val x: Array[Int] = Array(3, 2, 1 ,4 ,5 )

  val x1 = Seq.fill(50)(Random.nextInt(50)).toList
  val len = x1.length
  val xx = mergeSortL(x1)

  println(xx mkString " ")
}