/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package pkg482project;

import java.util.Stack;
import java.util.ArrayList;

/**
 *
 * @author mateu
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    private int V; //n# of non-zero entries
    private static int index = 0;
    private Stack<Integer[][]> S; //stack where all non-zero entries will be pushed into

    public static void main(String[] args) {
        // TODO code application logic here
        int[][] sparse = {{0, 1, 0, 0}, {0, 0, 1, 0}, {1, 0, 0, 0}, {0, 0, 0, 1}};
        int V = 4;
        tarjan(sparse, V);
    }

    public static void tarjan(int[][] sparse, int V) {
        int[] sc = new int[V];

        int disc[][] = new int[V][V]; //using a 2D array is the only/best way I thought to on how to keep track of lowlink
        int low[][] = new int[V][V];

        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                disc[i][j] = -1;
                low[i][j] = -1;
            }
        }

        boolean[][] inStack = new boolean[V][V];
        Stack<int[]> st = new Stack<int[]>();

        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (disc[i][j] == -1 && sparse[i][j] == 1) {//sparse == 1 is just may way of making it less horrible 
                    strongConnect(i, j, inStack, sparse, V, low, disc, st);
                }
            }
        }
    }

    public static void strongConnect(int i, int j, boolean[][] inStack, int[][] sparse, int V, int low[][], int disc[][], Stack<int[]> st) {
        disc[i][j] = index;
        low[i][j] = index;
        index = +1;
        inStack[i][j] = true;
        int[] a = {i, j}; //array to push into the stack
        st.push(a);
        
        int z = 0;
        while(z < V){
            z = z+1; //I am not sure if this is correct
            
            //TODO: Find how to integrate n in this array/matrix thing
            //n = i.next();
            // low[u] = Math.min(low[u], low[n]);
            
            if(disc[i][j] == -1){
//                i = i+1;
//                j = j+1;
                strongConnect(i, j, inStack, sparse, V, low, disc, st);
                //low[i][j] = Math.min(low[i][j])
            }
            else if(inStack[i][j] == true){
                
            }
            
        }
    }
}
