import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    // DOESN'T WORK
    private abstract class Heap {
        Double[] heap;
        int maxSize = 10;
        int currSize = 0;

        public Heap() {
            heap = new Double[maxSize];
        }
        int parent(int pos) {return (int)Math.floor((pos - 1)/2.0);}
        boolean hasParent(int pos) {return parent(pos) >= 0;}
        int left(int pos) {return pos*2 + 1;}
        int right(int pos) {return pos*2 + 2;}
        boolean hasLeft(int pos) {return left(pos) < currSize;}
        boolean hasRight(int pos) {return right(pos) < currSize;}
        abstract void heapUp();
        abstract void heapDown();
        void add(double val) {
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
        double peek() {
            if (currSize == 0)
                return 0;
            return heap[0];
        }
        void doubleSize() {
            maxSize *= 2;
            Double[] tmp = new Double[maxSize];
            for (int i = 0; i < currSize; i++) {
                tmp[i] = heap[i];
            }
        }
        void swap(int pos1, int pos2) {
            double tmp = heap[pos2];
            heap[pos2] = heap[pos1];
            heap[pos1] = tmp;
        }
    }

    private class MaxHeap extends Heap {
        @Override
        void heapUp() {
            int pos = currSize - 1;
            while (hasParent(pos)) {
                int par = parent(pos);
                if (heap[pos] > heap[par]) {
                    swap(pos, par);
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
                if (heap[child] < heap[pos]) {
                    swap(pos, child);
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
                if (heap[pos] < heap[par]) {
                    swap(pos, par);
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
                    swap(pos, child);
                    pos = child;
                } else {
                    break;
                }
            }
        }
    }

    public static void balanceHeaps(Solution.MaxHeap smallHeap, Solution.MinHeap bigHeap) {
        if (smallHeap.currSize > bigHeap.currSize) {
            bigHeap.add(smallHeap.pop());
        } else if (smallHeap.currSize + 1 < bigHeap.currSize) {
            smallHeap.add(bigHeap.pop());
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        Solution.MaxHeap smallHeap = new Solution().new MaxHeap();
        Solution.MinHeap bigHeap = new Solution().new MinHeap();
        double median = 0;
        boolean is_even = true;
        for(int a_i=0; a_i < n; a_i++){
            is_even = !is_even;
            int val = in.nextInt();
            if (median < val)
                bigHeap.add(val);
            else
                smallHeap.add(val);
            balanceHeaps(smallHeap, bigHeap);
            if (is_even) {
                median = bigHeap.peek() + smallHeap.peek();
                median /= 2.0;
            } else {
                median = bigHeap.peek();
            }
            System.out.println(String.format("%.1f", median));
        }
    }
}
