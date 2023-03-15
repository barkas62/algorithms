//import main.java.Node;
//import junit.framework.*;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;


public class TreeTraversalTest {
    Node tree = null;

    @BeforeEach
    void setUp() {
        Node root = new Node(1);
        Node n2 = root.leftNode(2);
        Node n3 = root.riteNode(3);
        Node n4 = n2.leftNode(4);
        Node n5 = n2.riteNode(5);
        this.tree = root;
    }

    @Test
    public void testBFS(){
        ArrayList<Integer> acc1 = new ArrayList<>(Arrays.asList(1,2,3,4,5));
        ArrayList<Integer> acc2 = new ArrayList<>();
        TreeTraversal.bfs(this.tree, ((n) -> acc2.add( n.data() )));
        Assertions.assertEquals(acc1,acc2);
    }

    @Test
    public void testPreorder(){
        ArrayList<Integer> acc1 = new ArrayList<>();
        ArrayList<Integer> acc2 = new ArrayList<>();
        TreeTraversal.dfs_preorder(this.tree, ((n) -> acc1.add( n.data() )));
        TreeTraversal.dfs_preorder_iter(this.tree, ((n) -> acc2.add( n.data() )));
        Assertions.assertEquals(acc1,acc2);
    }

    @Test
    public void testPostorder(){
        ArrayList<Integer> acc1 = new ArrayList<>();
        ArrayList<Integer> acc2 = new ArrayList<>();
        TreeTraversal.dfs_postorder(this.tree, ((n) -> acc1.add( n.data() )));
        TreeTraversal.dfs_postorder_iter(this.tree, ((n) -> acc2.add( n.data() )));
        Assertions.assertEquals(acc1,acc2);
    }

    @Test
    public void testInorder(){
        ArrayList<Integer> acc1 = new ArrayList<>();
        ArrayList<Integer> acc2 = new ArrayList<>();
        TreeTraversal.dfs_inorder(this.tree, ((n) -> acc1.add( n.data() )));
        TreeTraversal.dfs_inorder_iter(this.tree, ((n) -> acc2.add( n.data() )));
        Assertions.assertEquals(acc1,acc2);
    }
}
