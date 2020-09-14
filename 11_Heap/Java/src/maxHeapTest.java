import junit.framework.TestCase;
import junit.framework.Assert;

public class maxHeapTest extends TestCase {

    public void testAdd() {
        maxHeap h = new maxHeap(5);
        h.add(3);
        h.add(0);
        h.add(2);
        h.add(1);
        h.add(4);

        Assert.assertTrue("Wrong - It's NOT a heap!", h.is_heap());

        System.out.println("Add test passed OK");
    }

    public void testPop() {
        maxHeap h = new maxHeap(5);
        h.add(3);
        h.add(0);
        h.add(2);
        h.add(1);
        h.add(4);

        Assert.assertEquals(h.pop(), 4);
        Assert.assertEquals(h.pop(), 3);
        Assert.assertEquals(h.pop(), 2);
        Assert.assertEquals(h.pop(), 1);
        Assert.assertEquals(h.pop(), 0);

        System.out.println("Pop test passed OK");
    }

    public void testHeapify() {
        int [] arr = {0,3,2,1,4};
        maxHeap h = new maxHeap(arr);

        Assert.assertTrue("Wrong - It's NOT a heap!", h.is_heap());

        System.out.println("Heapify test passed OK");
    }

    public void testMerge() {
        int[] arr1 = {0,6,2,4};
        maxHeap h1 = new maxHeap(arr1);
        int[] arr2 = {7,3,1,5};
        maxHeap h2 = new maxHeap(arr2);
        h1.merge(h2);

        Assert.assertTrue("Wrong - It's NOT a heap after merge!", h1.is_heap());

        System.out.println("Merge test passed OK");
    }
}