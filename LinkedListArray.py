import java.util.LinkedList;

public class LinkedListArray {

    private LinkedList<Object> list;

    public LinkedListArray() {
        list = new LinkedList<Object>();
    }

    public void add(Object obj) {
        list.add(obj);
    }

    public Object get(int index) {
        if (index < 0 || index >= list.size()) {
            throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + list.size());
        }
        return list.get(index);
    }

    public void remove(int index) {
        if (index < 0 || index >= list.size()) {
            throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + list.size());
        }
        list.remove(index);
    }

    public int size() {
        return list.size();
    }

    public static void main(String[] args) {
        LinkedListArray array = new LinkedListArray();

        array.add("Element 1");
        array.add("Element 2");
        array.add("Element 3");

        System.out.println("Array Size: " + array.size());

        System.out.println("Element at index 1: " + array.get(1));

        array.remove(1);

        System.out.println("Array Size after removal: " + array.size());
    }
}
