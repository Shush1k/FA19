package package_two;


class ObservableStringBuilder {

    private ChangeListener ChangeListener;

    private final StringBuilder stringBuilder;

    public void setChangeListener(ChangeListener changeListener) {
        this.ChangeListener = changeListener;
    }

    public ObservableStringBuilder() {
        stringBuilder = new StringBuilder();
    }

    private void notifyListener(){
        if(ChangeListener != null){
            ChangeListener.Change(this);
        }
        else {
            System.out.println("Уведомления выключены");
        }
    }
    public ObservableStringBuilder deleteCharAt(int index) {
        stringBuilder.deleteCharAt(index);
        notifyListener();
        return this;
    }

    public ObservableStringBuilder delete(int start, int end) {
        stringBuilder.delete(start,end);
        notifyListener();
        return this;
    }

    public ObservableStringBuilder append(Object obj) {
        stringBuilder.append(obj);
        notifyListener();
        return this;
    }
    public ObservableStringBuilder reverse() {
        stringBuilder.reverse();
        notifyListener();
        return this;
    }

    public ObservableStringBuilder replace(int start, int end, String str) {
        stringBuilder.replace(start, end, str);
        notifyListener();
        return this;
    }

    public ObservableStringBuilder insert(int index, char[] str, int offset, int len) {
        stringBuilder.insert(index, str, offset, len);
        notifyListener();
        return this;
    }


    public String toString() {
        return stringBuilder.toString();
    }
}



