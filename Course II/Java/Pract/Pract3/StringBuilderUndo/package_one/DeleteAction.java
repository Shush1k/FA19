package package_one;

public class DeleteAction implements Action{
    private int size;
    private StringBuilder stringBuilder;
    public DeleteAction(int size) {
        this.size = size;
    }

    public void undo(){
        stringBuilder.delete(
                stringBuilder.length() - size, stringBuilder.length());
    }
}
