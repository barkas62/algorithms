import java.util.Arrays;

public class MergeSort {
    public static void main(String [] args){
        int[] Arr = new int[]{3,6,1,7,2,5,4};

        int[] sortedArr = mergeSort(Arr);
        for (int a: sortedArr){
            System.out.println(a);
        }
    }

    public static int[] mergeSort(int[] Arr){
        if (Arr.length == 1)
            return Arr.clone();

        int i_mid = Arr.length >> 1;

        int[] Arr1 = mergeSort( Arrays.copyOfRange(Arr, 0, i_mid) );
        int[] Arr2 = mergeSort( Arrays.copyOfRange(Arr, i_mid, Arr.length) );

        int[] ArrN = new int[Arr.length];
        int iN = 0;
        int i1 = 0;
        int i2 = 0;
        while (i1 < Arr1.length || i2 < Arr2.length){
            if (i2 >= Arr2.length){
                ArrN[iN] = Arr1[i1];
                i1 += 1;
            }
            else if (i1 >= Arr1.length){
                ArrN[iN] = Arr2[i2];
                i2 += 1;
            } else if (Arr1[i1] < Arr2[i2]){
                ArrN[iN] = Arr1[i1];
                i1 += 1;
            } else{
                ArrN[iN] = Arr2[i2];
                i2 += 1;
            }
            iN += 1;
        }
        return ArrN;
    }
}
