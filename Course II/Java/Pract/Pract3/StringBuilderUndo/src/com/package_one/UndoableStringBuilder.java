package src.com.package_one;

import java.util.Stack;

class UndoableStringBuilder  {
    // Стек
    private Stack<Action> actions = new Stack<>();

    private StringBuilder stringBuilder;

    public UndoableStringBuilder() {
        stringBuilder = new StringBuilder();
    }
    public UndoableStringBuilder insert(int index, char[] str, int offset, int len) {
        /*Вставка символов по индексам*/
        stringBuilder.insert(index, str, offset, len);
        actions.add(() -> stringBuilder.delete(index, len));
        return this;
    }

    public UndoableStringBuilder insert(int offset, String str) {
        /*Вставка строки по индексу*/
        stringBuilder.insert(offset, str);
        actions.add(() -> stringBuilder.delete(offset, str.length()));
        return this;
    }

    public UndoableStringBuilder reverse() {
        /*Переворачивает всю строку
          Добавляем в стек команду reverse
         */
        stringBuilder.reverse();

        Action action = new Action(){
            public void undo() {
                stringBuilder.reverse();
            }};
        actions.add(action);
        return this;
    }


    public UndoableStringBuilder append(String str) {
        stringBuilder.append(str);

        Action action = new Action(){
            public void undo() { stringBuilder.delete(stringBuilder.length() - str.length() -1,
                        stringBuilder.length()); }
        };
        actions.add(action);
        return this;
    }


    public UndoableStringBuilder appendCodePoint(int codePoint) {
        int lenBefore = stringBuilder.length();
        stringBuilder.appendCodePoint(codePoint);
        actions.add(new DeleteAction(stringBuilder.length() - lenBefore));
        return this;
    }

    public UndoableStringBuilder delete(int start, int end) {
        /*Удаляет элемент с начальной по конечную позицию не включительно*/
        String deleted = stringBuilder.substring(start, end);
        stringBuilder.delete(start, end);
        actions.add(() -> stringBuilder.insert(start, deleted));
        return this;
    }

    public UndoableStringBuilder deleteCharAt(int index) {
        /*Удаление символа по индексу*/
        char deleted = stringBuilder.charAt(index);
        stringBuilder.deleteCharAt(index);
        actions.add(() -> stringBuilder.insert(index, deleted));
        return this;
    }

    public UndoableStringBuilder replace(int start, int end, String str) {
        /*То*/
        String deleted = stringBuilder.substring(start, end);
        stringBuilder.replace(start, end, str);
        actions.add(() -> stringBuilder.replace(start, end, deleted));
        return this;
    }
    // undo, length, toString

    public void undo(){ if(actions.isEmpty() == false){ actions.pop().undo(); } }

    public int length(){ return stringBuilder.length(); }

    public String toString() {
        return stringBuilder.toString();
    }
}