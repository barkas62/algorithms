import scala.reflect.ClassTag


object Try extends App {
  import MergeSort._

  val x: Array[Int] = Array(3, 2, 1 ,4 ,5 )

  mergeSort(x)

  println(x mkString " // ")
}

object MergeSort {

  def mergeSort[T <% Ordered[T] : ClassTag](x: Array[T]): Unit ={
    val y = new Array[T](x.length)
    mSort(x, y, 0, x.length-1 )
  }

  def mSort[T <% Ordered[T]](x: Array[T], y: Array[T], beg: Int, end: Int): Unit ={

    if (end - beg > 0){
      val mid = (beg + end) / 2
      mSort(x, y, beg,   mid)
      mSort(x, y, mid+1, end)

      merge(x, y, beg, mid, end)
      Array.copy(y, beg, x, beg, end-beg+1)
    }

  }

  def merge[T <% Ordered[T]](src: Array[T], dst: Array[T], beg: Int, mid: Int, end: Int): Unit ={
    var i0 = beg
    var i1 = beg
    var i2 = mid+1

    while (i1 <= mid || i2 <= end){
      if (i1 <= mid && i2 <= end){
        if (src(i1) < src(i2)) {
          dst(i0) = src(i1)
          i1 += 1
        } else {
          dst(i0) = src(i2)
          i2 += 1
        }
      }
      else if (i1 <= mid){
        dst(i0) = src(i1)
        i1 += 1
      }
      else {
        dst(i0) = src(i2)
        i2 += 1
      }
      i0 += 1
    }
  }

}
