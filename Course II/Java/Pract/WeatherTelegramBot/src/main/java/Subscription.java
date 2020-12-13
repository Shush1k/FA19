import org.json.JSONObject;

import java.time.LocalTime;
import java.util.Map;

public class Subscription extends Thread {
    @Override
    public void run() {
        Bot bot = new Bot();

        try {
            while (true)
            {
                // Время отправки погоды
                if (LocalTime.now().getHour() == 10) {
                    Map<String, String> subInfo = bot.read();

                    for (Map.Entry<String, String> user : subInfo.entrySet()) {
                        JSONObject data = Parser.getTodayData(user.getValue());
                        String answer = "Подписка\n";
                        answer += Parser.processTodayData(data);
                        bot.sendMsg(user.getKey(), answer);
                    }
                    sleep(1000 * 60 * 60);

                } else sleep(20000);

            }
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }
}