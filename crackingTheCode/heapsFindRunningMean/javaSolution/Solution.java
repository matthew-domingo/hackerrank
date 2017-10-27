import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    private abstract class Heap {
        Double[] heap;
        int maxSize = 10;
        int currSize = 0;

        public Heap() {
            heap = new Double[maxSize];
        }
        int parent(int pos) {return (int)Math.floor((pos - 1)/2.0);}
        boolean hasParent(int pos) {return parent(pos) > 0;}
        int left(int pos) {return (pos + 1) * 2;}
        int right(int pos) {return (pos + 2) * 2;}
        boolean hasLeft(int pos) {return left(pos) < currSize;}
        boolean hasRight(int pos) {return right(pos) < currSize;}
        abstract void heapUp();
        abstract void heapDown();
        void insert(double val) {
            currSize++;
            if (currSize >= maxSize)
                doubleSize();
            heap[currSize - 1] = val;
            heapUp();
        }
        double pop() {
            if (currSize == 0)
                return 0;
            Double res = heap[0];
            heap[0] = heap[--currSize];
            heap[currSize] = null;
            heapDown();
            return res;
        }
        void doubleSize() {
            maxSize *= 2;
            Double[] tmp = new Double[maxSize];
            for (int i = 0; i < currSize; i++) {
                tmp[i] = heap[i];
            }
        }
    }

    private class MaxHeap extends Heap {
        @Override
        void heapUp() {
            int pos = currSize - 1;
            while (hasParent(pos)) {
                int par = parent(pos);
                if (heap[par] < heap[pos]) {
                    double tmp = heap[par];
                    heap[par] = heap[pos];
                    heap[pos] = tmp;
                    pos = par;
                }
                else
                    break;
            }
        }

        @Override
        void heapDown() {
            int pos = 0;
            int child = 0;
            while (hasLeft(pos)) {
                if (hasRight(pos)) {
                    if (heap[left(pos)] > heap[right(pos)])
                        child = left(pos);
                    else
                        child = right(pos);
                } else {
                    child = left(pos);
                }
                if (heap[child] > heap[pos]) {
                    double tmp = heap[child];
                    heap[child] = heap[pos];
                    heap[pos] = tmp;
                    pos = child;
                } else {
                    break;
                }
            }
        }
    }

    private class MinHeap extends Heap {
        @Override
        void heapUp() {
            int pos = currSize - 1;
            while (hasParent(pos)) {
                int par = parent(pos);
                if (heap[par] > heap[pos]) {
                    double tmp = heap[par];
                    heap[par] = heap[pos];
                    heap[pos] = tmp;
                    pos = par;
                }
                else
                    break;
            }
        }

        @Override
        void heapDown() {
            int pos = 0;
            int child = 0;
            while (hasLeft(pos)) {
                if (hasRight(pos)) {
                    if (heap[left(pos)] < heap[right(pos)])
                        child = left(pos);
                    else
                        child = right(pos);
                } else {
                    child = left(pos);
                }
                if (heap[child] < heap[pos]) {
                    double tmp = heap[child];
                    heap[child] = heap[pos];
                    heap[pos] = tmp;
                    pos = child;
                } else {
                    break;
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] a = new int[n];
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }
    }
}
