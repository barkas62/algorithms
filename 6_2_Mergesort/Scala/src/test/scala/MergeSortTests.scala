
import org.junit._
import org.junit.Assert.assertArrayEquals

import scala.util.Random

class MergeSortTests {
  import MergeSort._

  @Test def `Mergesort_of_a_simple_array`: Unit = {
    val x: Array[Int] = Array(3, 2, 1 ,4 ,5 )
    mergeSort(x)

    assertArrayEquals(x, Array(1, 2, 3 ,4 ,5 ))
  }

  @Test def `Mergesort_of_an empty_array`: Unit = {
    val x: Array[Int] = Array()
    mergeSort(x)
    assertArrayEquals(x, Array[Int]())
  }

  @Test def `Megrgesort_of_a_long_list`: Unit = {
    val x = Seq.fill(5000)(Random.nextInt(50)).toList

    val x_sorted = mergeSortL(x)
    assert( isSorted(x_sorted) )
  }
}

