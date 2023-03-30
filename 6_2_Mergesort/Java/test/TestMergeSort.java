import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.*;

public class TestMergeSort {
    @Test
    public void testMergeSort(){
        int[] Arr0 = new int[]{3,6,1,7,2,5,4};
        int[] Arr1 = new int[]{1,2,3,4,5,6,7};

        int[] sortedArr0 = MergeSort.mergeSort(Arr0);

        Assertions.assertArrayEquals(sortedArr0, Arr1);
    }

}
