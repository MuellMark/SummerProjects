public class Node{
    public String data;
    private Node left;
    private Node right;

    public Node(String data){
        this.data=data;
        this.left=null;
        this.right=null;
    }

    public void setLeft(Node left){
        this.left=left;
    }

    public void setRight(Node right){
        this.right=right;
    }

    public Node getNextLeft(){
        return this.left;
    }

    public Node getNextRight(){
        return this.right;
    }
}