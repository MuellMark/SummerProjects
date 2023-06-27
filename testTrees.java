import javax.naming.BinaryRefAddr;

public class testTrees{

    public static void main(String[]args){
        Node first = new Node("First");
        BinaryTree tree = new BinaryTree(first);
        tree.setLeft(new Node("Second"));
        tree.setRight(new Node("Third"));
        // tree.moveCurrentLeft();
        // tree.moveCurrentLeft();
        // tree.moveCurrentRight();
        // System.out.println(tree.getCurrent().data);
        tree.printTree();
    }
}