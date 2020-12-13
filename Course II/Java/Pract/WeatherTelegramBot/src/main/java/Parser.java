
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;
import com.mashape.unirest.http.exceptions.UnirestException;
import org.json.JSONObject;
import com.mashape.unirest.http.JsonNode;

import java.time.LocalDate;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;


public class Parser {

    public static void main(String[] args) throws UnirestException {
        // Проверка парсинга
        JSONObject data = getTodayData("Самара");
        processTodayData(data);
        System.out.println(data.toString(2));
    }


    public static JSONObject getTodayData(String city) throws UnirestException {
        HttpResponse<JsonNode> jsonResponse = Unirest.get("https://community-open-weather-map.p.rapidapi.com/forecast?q=" +
                city + "%2Cru&units=metric&lang=ru")
                .header("x-rapidapi-key", "af19471729msh67370b1f5c7efdfp1f26f0jsnf82d973c1c62")
                .header("x-rapidapi-host", "community-open-weather-map.p.rapidapi.com")
                .asJson();

        return jsonResponse.getBody().getObject();
    }


    public static JSONObject getCurrentData(String city) throws UnirestException {
        HttpResponse<JsonNode> jsonResponse = Unirest.get("https://community-open-weather-map.p.rapidapi.com/weather?q=" +
                city + "%2Cru&lat=0&lon=0&lang=ru&units=metric&mode=xml%2C%20html")
                .header("x-rapidapi-key", "af19471729msh67370b1f5c7efdfp1f26f0jsnf82d973c1c62")
                .header("x-rapidapi-host", "community-open-weather-map.p.rapidapi.com")
                .asJson();

        return jsonResponse.getBody().getObject();
    }


    public static String processCurrentData(JSONObject data){
        //Обработка полученных данных
        String answer;
        int answerCode = data.getInt("cod");

        if (answerCode == 200) {
            String city = data.getString("name");
            String currentTime = LocalTime.now().format(DateTimeFormatter.ofPattern("HH:mm"));
            String temp = Math.round(data.getJSONObject("main").getInt("temp")) + " C°";
            String info = data.getJSONArray("weather").getJSONObject(0).getString("description");
            info = printable(info);

            answer = city + " " + currentTime +"\n\uD83C\uDF21 " + temp + "\n" + info + "\n";

        } else answer = "Город не был найден";

        return answer;
    }


    public static String processTodayData(JSONObject data){
        String answer;
        int answerCode = data.getInt("cod");

        if (answerCode == 200) {
            String cityName = data.getJSONObject("city").getString("name");
            int currentHour = LocalTime.now().getHour();
            int constraint = ((24 - currentHour) / 3) + 1;
            String currentDate = LocalDate.now().format(DateTimeFormatter.ofPattern("dd.MM.yyyy")) + " — " + LocalTime.now().format(DateTimeFormatter.ofPattern("HH:mm"));
            // Header
            answer = "Город: " + cityName + "\nДата: " + currentDate + "\n\n";

            // Body
            for (int hour = 0; hour < constraint; hour++){
                JSONObject nowHour = data.getJSONArray("list").getJSONObject(hour);
                String time = nowHour.getString("dt_txt").substring(11, 16);
                String temp = Math.round(nowHour.getJSONObject("main").getInt("temp")) + " C°";
                String info = nowHour.getJSONArray("weather").getJSONObject(0).getString("description");
                info = printable(info);

                answer += time + " -> " + temp + "\n" + info + "\n\n";
            }


        } else answer = "Город не был найден";

        return answer;
    }


    public static String printable(String string){
        string = string.toLowerCase();
        if (string.contains("небольшая облачность"))
            string += " ⛅";
        else if (string.contains("облачно"))
            string += " ☁";
        else if (string.contains("снег"))
            string += " ❄️";
        else if (string.contains("ясно"))
            string += " ☀";
        else if (string.contains("небольшой дождь"))
            string += " ☔";
        else if (string.contains("гроз"))
            string += " ⛈";
        else if (string.contains("молн"))
            string += " ⛈";
        else if (string.contains("пасмурно"))
            string += " ☁";

        return string;
    }

}