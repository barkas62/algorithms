class Node {
    private int data = -1;
    private Node left = null;
    private Node rite = null;

    public Node(int data){
        this.data = data;
    }

    public Node(int data, Node left, Node rite) {
        this.data = data;
        this.left = left;
        this.rite = rite;
    }

    public int data(){
        return data;
    }

    public Node left(){
        return left;
    }

    public Node rite(){
        return rite;
    }

    public Node leftNode(int data) {
        left = new Node(data);
        return left;
    }

    public Node riteNode(int data) {
        rite = new Node(data);
        return rite;
    }
};
