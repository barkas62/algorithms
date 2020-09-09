public class DisjointSets{
    int[] parent;
    int[] weight;

    public DisjointSets(int size){
        this.parent = new int[size];
        this.weight = new int[size];
        for(int i = 0; i < size; i++){
            this.parent[i] = i;
            this.weight[i] = 1;
        }
    }

    public int find(int i){
        if(this.parent[i] != i)
            this.parent[i] = find(this.parent[i]);
        return this.parent[i];
    }

    public void union(int i1, int i2)
    {
        int p1 = find(i1);
        int p2 = find(i2);
        if(p1 != p2) {
            if (this.weight[p1] < this.weight[p2]) {
                this.parent[p1] = p2;
                this.weight[p2] += this.weight[p1];
            } else {
                this.parent[p2] = p1;
                this.weight[p1] += this.weight[p2];
            }
        }
    }

    public boolean same_set(int i1, int i2){
        return find(i1) == find(i2);
    }

}

