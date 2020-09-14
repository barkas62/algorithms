import org.jetbrains.annotations.NotNull;

public class maxHeap {
    int cur_size = 0;
    int[] data;

    public maxHeap(int _max_size) {
        data = new int[_max_size];
        cur_size = 0;
    }

    public maxHeap (int @NotNull [] arr) {
        data = arr.clone();
        cur_size = arr.length;
        heapify();
    }


    public int add(int val) {
        if( cur_size >= data.length )
            return -1;

        data[cur_size] = val;
        sift_up(cur_size);
        cur_size++;

        return this.cur_size;
    }

    public int pop() {
        if(cur_size == 0)
            throw new IndexOutOfBoundsException("Heap is empty.");
        int max_val = data[0];
        data[0] = data[cur_size-1];
        cur_size--;
        sift_dn(0);

        return max_val;
    }

    public void merge( maxHeap h ) {
        // Merge this heap with heap h
        int[] merged_data = new int[data.length + h.data.length];
        System.arraycopy (data,   0, merged_data, 0,   cur_size);
        System.arraycopy (h.data, 0, merged_data,  cur_size, h.cur_size);
        data = merged_data;
        cur_size += h.cur_size;
        heapify();
    }

    protected static int parent(int i) {
        return i > 0 ? (int)(i-1)/2 : 0;
    }

    protected static int l_child(int i) {
        return (2*i + 1);
    }

    protected static int r_child(int i) {
        return (2*i + 2);
    }

    protected void heapify() {
        int i_last = parent(cur_size -1);  // last id that has any children
        for (int i = i_last; i >= 0; i--)
            sift_dn(i);
    }

    protected void sift_up( int i ) {
        int ip = parent(i);
        while (i > 0 && ip >= 0 && data[ip] < data[i]) {
            int tmp = data[ip];
            data[ip] = data[i];
            data[i] = tmp;
            i = ip;
            ip = parent(i);
        }
    }

    protected void sift_dn( int i ) {
        while( i < cur_size ) {
            int i_dn = i;

            int i_l = l_child(i);
            if (i_l < cur_size && data[i_l] > data[i_dn])
                i_dn = i_l;

            int i_r = r_child(i);
            if (i_r < cur_size && data[i_r] > data[i_dn])
                i_dn = i_r;

            if (i_dn == i)
                break;

            int tmp = data[i_dn];
            data[i_dn] = data[i];
            data[i] = tmp;

            i = i_dn;
        }
    }

    public boolean is_heap(){
        for(int i = 0; i < cur_size; i++){
            int il = l_child(i);
            int ir = r_child(i);
            if (il < cur_size && data[il] > data[i])
                return false;
            if (ir < cur_size && data[ir] > data[i])
                return false;
            if (il >= cur_size && ir >= cur_size){
                break;
            }
        }
        return true;
    }
}


