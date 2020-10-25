package package_one;

public class Main {
    public static void main(String[] args) {
        UndoableStringBuilder undoableStringBuilder = new UndoableStringBuilder();

        System.out.println(undoableStringBuilder.insert(0, "Таааск."));
        System.out.println(undoableStringBuilder.insert(undoableStringBuilder.length(), ".."));
        System.out.println(undoableStringBuilder.deleteCharAt(1));
        System.out.println("До undo: "+undoableStringBuilder);
        undoableStringBuilder.undo();
        undoableStringBuilder.reverse();
        System.out.println("После undo и reverse: "+undoableStringBuilder);
        undoableStringBuilder.undo();
        System.out.println("После undo: "+undoableStringBuilder);
        System.out.println(undoableStringBuilder.replace(0, 3, "М"));
        System.out.println(undoableStringBuilder.insert(1, new char[]{'и', 'н', 'и', 'т'}, 0, 4));

    }
}
