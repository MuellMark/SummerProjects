import java.util.*;
public class testTrees{

    public static void main(String[]args){
        ArrayList<String> fastFood = new ArrayList<String> (Arrays.asList("McDonald's","Burger King", "Taco Bell","Wendy's"));
        // Node first = new Node("First");
        // BinaryTree tree = new BinaryTree(first);
        // tree.setLeft(new Node("Second"));
        // tree.setRight(new Node("Third"));
        // // tree.moveCurrentLeft();
        // // tree.moveCurrentLeft();
        // // tree.moveCurrentRight();
        // // System.out.println(tree.getCurrent().data);
        // tree.printTree();

        runFavorites(fastFood);
        
    }

    public static void runFavorites(ArrayList<String> list){
        Random rand = new Random();
        int start = rand.nextInt(list.size());
        String root = (list.get(start));
        list.remove(start);

        // Start for Binarytree with random node
        BinaryTree tree = new BinaryTree(new Node(root));
        System.out.println("Your starting point is "+root);
        System.out.println("Type \"y\" for yes and \"n\" for no");
        

        Scanner scan = new Scanner(System.in);
        while(list.size()>0){
            int nextRand = rand.nextInt(list.size());
            String temp = (list.get(nextRand));
            list.remove(nextRand);

            boolean placed = false;
            tree.resetCurrent();
            while(!placed){
                System.out.print("Do you like "+temp+ " better than "+tree.getCurrent().getData()+"? ");
                boolean scanBool = false;
                while(!scanBool){
                    String response = scan.next();
                    switch (response){
                        case "Y":
                        case "y":
                            if(tree.getRight()==null){
                                tree.getCurrent().setRight(new Node(temp));
                                placed =true;
                            }else{
                                tree.moveCurrentRight();
                            }
                            //System.out.println("yes");
                            scanBool=true;
                            break;
        
                        case "N":
                        case "n":
                            //System.out.println("no");
                            if(tree.getLeft()==null){
                                tree.getCurrent().setLeft(new Node(temp));
                                placed =true;
                            }else{
                                tree.moveCurrentLeft();
                            }
                            scanBool=true;
                            break;
                        default:
                            System.out.println("Invalid input, please try again");
                            break;
                    }
                }
            }


            
            
            
        }
        scan.close();
        //tree.printTree();
        //System.out.println(list.get(start));
        tree.printTree();
    }


}