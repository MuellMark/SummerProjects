import java.util.*;

public class BinaryTree{
    private Node root;
    private Node current;

    public BinaryTree(Node root){
        this.root=root;
        this.current=root;
    }

    // Need: getters, setters, moving current

    public Node getCurrent(){
        return current;
    }

    public Node getLeft(){
        return this.current.getNextLeft();
    }

    public Node getRight(){
        return this.current.getNextRight();
    }

    public void setLeft(Node node){
        current.setLeft(node);
    }

    public void setRight(Node node){
        current.setRight(node);
    }

    public void resetCurrent(){
        this.current=root;
    }

    //make right
    public void moveCurrentLeft(){
        if(current.getNextLeft()!=null) this.current=current.getNextLeft();
        else System.out.println("Not moved, left it null!");
    }

    public void moveCurrentRight(){
        if(current.getNextRight()!=null) this.current=current.getNextRight();
        else System.out.println("Not moved, right it null!");
    }

    public void printTree(){
        int count=1;
        Node node = this.root;
        ArrayList<String> elements = new ArrayList<>();
        printRecc(elements, node);
        for(String i:elements){
            System.out.println(count+": "+i);
            count++;
        }

    }

    private void printRecc(ArrayList<String> elements,Node node){
        if(node ==null) return;

        printRecc(elements,node.getNextRight());

        elements.add(node.data);
        printRecc(elements,node.getNextLeft());
    }

    public boolean isLeaf(){
        return (current.getNextLeft()==null && current.getNextRight()==null);
    }

}