
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Stack;
import java.util.function.Consumer;

public class TreeTraversal {
    public static void main(String [] args){
        Node root = new Node(1);
        Node n2 = root.leftNode(2);
        Node n3 = root.riteNode(3);
        Node n4 = n2.leftNode(4);
        Node n5 = n2.riteNode(5);

        System.out.println("Bfs:");
        bfs(root, ((n) -> System.out.print(n.data() + " ")));

        System.out.println("\n\nDfs preorder recursive:");
        dfs_preorder(root, ((n) -> System.out.print(n.data() + " ")));
        System.out.println("\n\nDfs preorder iterative:");
        dfs_preorder_iter(root, ((n) -> System.out.print(n.data() + " ")));

        System.out.println("\n\nDfs postorder recursive:");
        dfs_postorder(root, ((n) -> System.out.print(n.data() + " ")));
        System.out.println("\n\nDfs postorder iterative:");
        dfs_postorder_iter(root, ((n) -> System.out.print(n.data() + " ")));

        System.out.println("\n\nDfs inorder recursive:");
        dfs_inorder(root, ((n) -> System.out.print(n.data() + " ")));
        System.out.println("\n\nDfs inorder iterative:");
        dfs_inorder_iter(root, ((n) -> System.out.print(n.data() + " ")));

        System.out.println("\n\nFinished");
    }

    public static void bfs(Node root, Consumer<Node> func){
        if (root == null)
            return;
        Deque<Node> q = new ArrayDeque<>();
        q.add(root);
        while (!q.isEmpty()){
            Node n = q.poll();
            //System.out.println(" " + n.data());
            func.accept(n);
            if(n.left() != null)
                q.addLast(n.left());
            if(n.rite() != null)
                q.addLast(n.rite());
        }
    }

    public static void dfs_preorder(Node root, Consumer<Node> func){
        if (root == null) return;
        func.accept(root);
        dfs_preorder(root.left(), func);
        dfs_preorder(root.rite(), func);
    }

    public static void dfs_preorder_iter(Node root, Consumer<Node> func) {
        if (root == null || func == null) return;
        Stack<Node> stack = new Stack<Node>();
        stack.push(root);
        while (!stack.isEmpty()) {
            Node node = stack.pop();
            func.accept(node);
            if (node.rite() != null)
                stack.push(node.rite());
            if (node.left() != null)
                stack.push(node.left());
        }
    }

    public static void dfs_postorder(Node root, Consumer<Node> func){
        if (root == null) return;
        dfs_postorder(root.left(), func);
        dfs_postorder(root.rite(), func);
        func.accept(root);
    }

    public static void dfs_postorder_iter(Node root, Consumer<Node> func) {
        if (root == null || func == null) return;
        Stack<Node> stack1 = new Stack<Node>();
        Stack<Node> stack2 = new Stack<Node>();
        stack1.push(root);
        while (!stack1.isEmpty()) {
            Node node = stack1.pop();
            stack2.push(node);
            if (node.left() != null)
                stack1.push(node.left());
            if (node.rite() != null)
                stack1.push(node.rite());
        }
        while (!stack2.isEmpty()) {
            Node node = stack2.pop();
            func.accept(node);
        }
    }


    public static void dfs_inorder(Node root, Consumer<Node> func){
        if (root == null) return;
        dfs_inorder(root.left(), func);
        func.accept(root);
        dfs_inorder(root.rite(), func);
    }

    public static void dfs_inorder_iter(Node root, Consumer<Node> func) {
        if (root == null || func == null) return;
        Stack<Node> stack = new Stack<Node>();
        Node curr = root;
        while(true){
            if (curr != null){
                stack.push(curr);
                curr = curr.left();
            } else {
                if (!stack.isEmpty()){
                    curr = stack.pop();
                    func.accept(curr);
                    curr = curr.rite();
                } else {
                    break;
                }
            }

        }
    }
}
