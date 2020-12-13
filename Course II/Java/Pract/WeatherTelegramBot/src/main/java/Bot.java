import org.json.JSONObject;
import org.telegram.telegrambots.ApiContextInitializer;
import org.telegram.telegrambots.TelegramBotsApi;
import org.telegram.telegrambots.api.methods.send.SendMessage;
import org.telegram.telegrambots.api.objects.Update;
import org.telegram.telegrambots.api.objects.replykeyboard.ReplyKeyboardMarkup;
import org.telegram.telegrambots.api.objects.replykeyboard.buttons.KeyboardButton;
import org.telegram.telegrambots.api.objects.replykeyboard.buttons.KeyboardRow;
import org.telegram.telegrambots.bots.TelegramLongPollingBot;
import org.telegram.telegrambots.exceptions.TelegramApiException;
import org.telegram.telegrambots.exceptions.TelegramApiRequestException;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.*;

public class Bot extends TelegramLongPollingBot {
    String city;
    String directory = System.getProperty("user.dir");
    String file = "idCity.txt";
    String path = directory + File.separator + file;


    public static void main(String[] args) {
        ApiContextInitializer.init();
        TelegramBotsApi telegramBotsApi = new TelegramBotsApi();
        try {
            telegramBotsApi.registerBot(new Bot());
        } catch (TelegramApiRequestException e) {
            e.printStackTrace();
        }
        Thread subscription = new Subscription();
        subscription.start();
    }


    public synchronized void setButtons(SendMessage sendMessage) {

        ReplyKeyboardMarkup replyKeyboardMarkup = new ReplyKeyboardMarkup();
        sendMessage.setReplyMarkup(replyKeyboardMarkup);
        replyKeyboardMarkup.setSelective(true);
        replyKeyboardMarkup.setResizeKeyboard(true);
        replyKeyboardMarkup.setOneTimeKeyboard(false);

        List<KeyboardRow> keyboard = new ArrayList<>();
        KeyboardRow keyboardFirstRow = new KeyboardRow();
        KeyboardRow keyboardSecondRow = new KeyboardRow();

        keyboardFirstRow.add(new KeyboardButton("Выбрать город"));
        keyboardFirstRow.add(new KeyboardButton("Погода сейчас"));
        keyboardSecondRow.add(new KeyboardButton("Погода на сегодня"));

        keyboard.add(keyboardFirstRow);
        keyboard.add(keyboardSecondRow);

        replyKeyboardMarkup.setKeyboard(keyboard);
    }

    public Map<String, String> read() throws IOException {
        // Получаем chatId и city из файла
        Map<String, String> chatIdHistory = new HashMap<>();
        FileReader fileReader = new FileReader(path);
        BufferedReader bufReader = new BufferedReader(fileReader);
        String line = bufReader.readLine();
        while (line != null) {
            String key = line.split(" ")[0];
            String value = line.split(" ")[1];
            chatIdHistory.put(key, value);
            line = bufReader.readLine();
        }
        fileReader.close();
        return chatIdHistory;
    }


    public void write(String chatId, String city) throws IOException {
        // Записываем chatId и city в файл
        FileWriter fileWriter = new FileWriter(path, true);
        String chatHistory = chatId + " " + city + "\n";
        fileWriter.write(chatHistory);
        fileWriter.close();
    }


    public void remove(String chatId) throws IOException {
        // Удаляем запись из словаря по chatId и файла
        Map<String, String> chatIdHistory = read();
        chatIdHistory.remove(chatId);
        FileWriter fileWriter = new FileWriter(path);
        fileWriter.write("");
        fileWriter.close();
        FileWriter fileWr = new FileWriter(path, true);
        for (Map.Entry<String, String> line : chatIdHistory.entrySet()) {
            String chatHistory = line.getKey() + " " + line.getValue() + "\n";
            fileWr.append(chatHistory);
        }
        fileWr.close();
    }


    public synchronized void sendMsg(String chatId, String s) {
        SendMessage sendMessage = new SendMessage();
        setButtons(sendMessage);
        sendMessage.enableMarkdown(true);
        sendMessage.setChatId(chatId);
        sendMessage.setText(s);
        try {
            execute(sendMessage);
        } catch (TelegramApiException e) {
            e.printStackTrace();
        }
    }


    @Override
    public void onUpdateReceived(Update update) {
        String message = update.getMessage().getText();
        String chadId = update.getMessage().getChatId().toString();

        try {
            switch (message) {

                case "/start":
                    sendMsg(chadId, "Данный бот выводит погоду по России на текущий момент и сегодняшний день, можете подписаться на ежедневную рассылку погоды");
                    break;
                case "Выбрать город":
                    sendMsg(chadId, "Введите название города и выберите необходимую опцию");
                    break;
                case "Погода сейчас": {
                    JSONObject data = Parser.getCurrentData(city);
                    String answer = Parser.processCurrentData(data);
                    sendMsg(chadId, answer);
                    break;
                }
                case "Погода на сегодня": {
                    JSONObject data = Parser.getTodayData(city);
                    String answer = Parser.processTodayData(data);
                    sendMsg(chadId, answer);
                    break;
                }

                case "/subscribe": {
                    try {
                        if (city != null) {
                            write(chadId, city);
                            sendMsg(chadId, "Вы подписались на ежедневную рассылку города " + city +
                                "\nв 10:00 будет приходить уведомление");
                        }
                        else
                            sendMsg(chadId, "Укажите город, прежде чем подписываться");
                    }
                    catch (Exception e) {
                        e.printStackTrace();
                    }
                    break;
                }
                case "/unsubscribe": {
                    try {
                        remove(chadId);
                        sendMsg(chadId, "Подписка на город отменена!");
                    }
                    catch (Exception e) {
                        e.printStackTrace();
                    }
                    break;
                }

                default:
                    city = message;
                    sendMsg(chadId, "Введен город, " + city);
                    break;
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

    }


    @Override
    public String getBotUsername() {
        return "Weather_Shush1k";
    }


    @Override
    public String getBotToken() {
        return "1465429676:AAE8_nZOkELdsiWkHlFdoZBSC50q3XUCgx8";
    }

}
