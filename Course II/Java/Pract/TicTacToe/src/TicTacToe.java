import java.util.*;

public class TicTacToe {
    static ArrayList<Integer> playerPositions = new ArrayList<>();
    static ArrayList<Integer> compPositions = new ArrayList<>();
    public static void main(String[] args) {
        char [][] gameBoard = {{' ', '|', ' ', '|', ' '},
                {'-', '+', '-', '+', '-'},
                {' ', '|', ' ', '|', ' '},
                {'-', '+', '-', '+', '-'},
                {' ', '|', ' ', '|', ' '}};

        printGameBoard(gameBoard);

        while (true){
            Scanner scan = new Scanner(System.in);
            System.out.print("Введите ячейку: ");
            try {
                int playerPos = scan.nextInt();

                while (0>playerPos || playerPos> 9){
                    System.out.println("Вводите числа от 1 до 9!");
                    playerPos = scan.nextInt();
                }

                while (playerPositions.contains(playerPos) || compPositions.contains(playerPos)){
                    System.out.println("Ячейка занята!");
                    playerPos = scan.nextInt();
                    while (0>playerPos || playerPos> 9){
                        System.out.println("Вводите числа от 1 до 9!");
                        playerPos = scan.nextInt();
                    }
                }
                setPlace(gameBoard, playerPos, "player");
                String res = checkWinner();
                if (res.length() > 0){
                    printGameBoard(gameBoard);
                    System.out.println(res);
                    break;
                }

                Random random = new Random();
                int compPos = random.nextInt(9) +1;
                while (playerPositions.contains(compPos) || compPositions.contains(compPos)){
                    compPos = random.nextInt(9) +1;
                }
                setPlace(gameBoard, compPos, "comp");
                printGameBoard(gameBoard);
                res = checkWinner();
                if (res.length() > 0){
                    printGameBoard(gameBoard);
                    System.out.println(res);
                    break;
                }
            }
            catch (InputMismatchException exc){
                System.out.println("Вы ввели не число!");
            }
        }

    }
    public static void printGameBoard(char[][] gameBoard){
        for(char[] row : gameBoard){
            for (char c : row){
                System.out.print(c);

            }
            System.out.println();
        }
    }
    public static void setPlace(char[][] gameBoard, int pos, String user){
        char symbol = ' ';
        if (user.equals("player")) {
            symbol = 'X';
            playerPositions.add(pos);
        }
        else if(user.equals("comp")){
            symbol = 'O';
            compPositions.add(pos);
        }
        switch (pos) {
            case 1 -> gameBoard[0][0] = symbol;
            case 2 -> gameBoard[0][2] = symbol;
            case 3 -> gameBoard[0][4] = symbol;
            case 4 -> gameBoard[2][0] = symbol;
            case 5 -> gameBoard[2][2] = symbol;
            case 6 -> gameBoard[2][4] = symbol;
            case 7 -> gameBoard[4][0] = symbol;
            case 8 -> gameBoard[4][2] = symbol;
            case 9 -> gameBoard[4][4] = symbol;
        }
    }
    public static String checkWinner(){
        List topRow = Arrays.asList(1, 2, 3);
        List midRow = Arrays.asList(4, 5, 6);
        List botRow = Arrays.asList(7, 8, 9);
        List leftCol = Arrays.asList(1, 4, 7);
        List midCol = Arrays.asList(2, 5, 8);
        List rightCol = Arrays.asList(3, 6, 9);
        List leftCross = Arrays.asList(1, 5, 9);
        List rightCross = Arrays.asList(3, 5, 7);

        List<List> winning = new ArrayList<>();
        winning.add(topRow);
        winning.add(midRow);
        winning.add(botRow);
        winning.add(leftCol);
        winning.add(midCol);
        winning.add(rightCol);
        winning.add(leftCross);
        winning.add(rightCross);
        for(List line : winning){
            if (playerPositions.containsAll(line)) {
                return "Ты победил!";
            }
            else if (compPositions.containsAll(line)){
                return "Выиграл компьютер";
            }
        }
        if (playerPositions.size() + compPositions.size() == 9){
            return "Ничья!";
        }
        return "";
    }
}
