import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

/**
 * https://www.hackerrank.com/challenges/ctci-find-the-running-median/problem
 */
public class Solution {

    private abstract class Heap {
        protected int size;
        protected int capacity;
        protected int[] heap;

        public Heap() {
            this.size = 0;
            this.capacity = 10;
            this.heap = new int[capacity];
        }

        public int parentIndex(int index) {return (index - 1) / 2;}
        public boolean hasParent(int index) {return parentIndex(index) >= 0;}
        public int parentValue(int index) {return heap[parentIndex(index)];}

        public int leftIndex(int index) {return 2 * index + 1;}
        public boolean hasLeft(int index) {return leftIndex(index) < size;}
        public int leftValue(int index) {return heap[leftIndex(index)];}

        public int rightIndex(int index) {return 2 * index + 2;}
        public boolean hasRight(int index) {return rightIndex(index) < size;}
        public int rightValue(int index) {return heap[rightIndex(index)];}

        public void add(int val) {
            ensureCapcity();
            heap[size++] = val;
            heapUp();
        }

        public int pop() {
            isEmpty("pop");
            int res = heap[0];
            heap[0] = heap[--size];
            heapDown();
            return res;
        }

        public int peek() {
            isEmpty("peek");
            return heap[0];
        }

        private void isEmpty(String methodName) {
            if (size == 0)
                throw new IllegalStateException("You cannot perform '" + methodName + "' on an empty Heap.");
        }

        private void ensureCapcity() {
            if (size >= capacity)
                doubleSize();
        }
        private void doubleSize() {
            capacity *= 2;
            int[] tmp = new int[capacity];
            for (int i = 0; i < size; i++) {
                tmp[i] = heap[i];
            }
            heap = tmp;
        }

        protected void swap(int index1, int index2) {
            int tmp = heap[index2];
            heap[index2] = heap[index1];
            heap[index1] = tmp;
        }

        abstract void heapUp();
        abstract void heapDown();
    }

    private class MaxHeap extends Heap {
        @Override
        void heapDown() {
            int index = 0;
            while (hasLeft(index)) {
                int indexChild = leftIndex(index);
                if (hasRight(index) && (leftValue(index) < rightValue(index))) {
                    indexChild = rightIndex(index);
                }
                if (heap[index] < heap[indexChild]) {
                    swap(index, indexChild);
                    index = indexChild;
                } else {
                    break;
                }
            }
        }

        @Override
        void heapUp() {
            int index = size - 1;
            while (hasParent(index) && (parentValue(index) < heap[index])) {
                swap(index, parentIndex(index));
                index = parentIndex(index);
            }
        }
    }

    private class MinHeap extends Heap {
        @Override
        void heapDown() {
            int index = 0;
            while (hasLeft(index)) {
                int indexChild = leftIndex(index);
                if (hasRight(index) && (leftValue(index) > rightValue(index))) {
                    indexChild = rightIndex(index);
                }
                if (heap[index] > heap[indexChild]) {
                    swap(index, indexChild);
                    index = indexChild;
                } else {
                    break;
                }
            }
        }

        @Override
        void heapUp() {
            int index = size - 1;
            while (hasParent(index) && (parentValue(index) > heap[index])) {
                swap(index, parentIndex(index));
                index = parentIndex(index);
            }
        }
    }

    public static void balanceHeaps(Solution.MaxHeap smallHeap, Solution.MinHeap bigHeap) {
        while (smallHeap.size > bigHeap.size)
            bigHeap.add(smallHeap.pop());
        while (smallHeap.size < bigHeap.size - 1)
            smallHeap.add(bigHeap.pop());
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
