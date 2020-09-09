

public class DisjointSetsTest {
    public static void main(String [] args){

        int size = 5;
        DisjointSets DS = new DisjointSets(size);

        DS.union(0,2);
        DS.union(2,4);
        DS.union(1,3);

        if(DS.same_set(0,4))
            System.out.println("OK1");
        else
            System.out.println("Bad1");

        if(DS.same_set(1,3))
            System.out.println("OK2");
        else
            System.out.println("Bad2");

        if(!DS.same_set(0,1))
            System.out.println("OK3");
        else
            System.out.println("Bad3");
    }
}
