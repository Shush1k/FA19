import java.util.*;


public class Main {

    public static void main(String[] args) {
        //Первая задача
        System.out.println("Первая задача");
        Main.buildDictWithMap("яаывоыоаоыфарыфаоыфдвдцциклмно");

        //Вторая задача
        System.out.println("Вторая задача");
        ArrayList<Integer> intList = new ArrayList<>();
        ArrayList<Character> charList = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            intList.add(i);
        }
        // Список из 10 элементов
        System.out.println(intList.size());

        ArrayList<Integer> intList2 = new ArrayList<>();
        for (int i = 0; i < 15; i++) {
            intList.add(i);
        }

        ArrayList<Integer> intList3 = new ArrayList<>();
        intList3.addAll(intList);
        intList3.addAll(intList2);
        // Список из 25 элементов
        System.out.println(intList3.size());
        Collection<Integer> collection = Main.removeDuplications(intList);
        System.out.println(collection.size());
    }

    /**
     * метод принимает строку, возвращает частотный словарь
     * Реализовано массивом
     *
     * @param text - передаем строку
     */
    public static void buildDict(String text) {
        text = text.toLowerCase();
        // Массив в который добавляем новую букву
        int[] result = new int['я' - 'а' + 1];
        // Цикл в котором переводим
        for (int i = 0; i < text.length(); i++) {
            char ch = text.charAt(i);
            if (ch >= 'a' && ch <= 'я') {
                result[ch - 'а']++;
            }

        }
        // Выводим полученный частотный словарь
        for (int i = 0; i < result.length; i++) {
            System.out.println((char) (i + 'а') + " = " + result[i]);
        }
    }

    /**
     * метод принимает сторку, возвращает частотный словарь
     * Реализовано словарем
     *
     * @param text - передаем строку
     */
    public static void buildDictWithMap(String text) {
        text = text.toLowerCase();
        //Map - словарь
        Map<Character, Integer> map = new HashMap<>();

        for (int i = 0; i < text.length(); i++) {
            char ch = text.charAt(i);
            // Проверка на русские буквы
            if ((ch >= 'а' && ch <= 'я') || ch == 'ё') {
                // передаем символ получаем пару ключ значение (буква - кол-во встретившихся)
                // Используем тернарный оператор
                map.compute(ch, ((character, integer) -> integer == null ? 1 : integer + 1));
            }
        }
        //Набор элементов коллекции(Map.Entry) .entrySet - возвращает множество пар ключ значение
        ArrayList<Map.Entry<Character, Integer>> entries = new ArrayList<>(map.entrySet());
        // o1, o2 - объекты. compare сравнивание двух символов(ключей объектов)
        entries.sort(((o1, o2) -> Character.compare(o1.getKey(), o2.getKey())));
        // Получаем отсортированный ArrayList

        // Выводим полученный частотный словарь
        for (Map.Entry<Character, Integer> enter : entries) {
            System.out.println(enter.getKey() + " = " + enter.getValue());
        }
    }

    /**
     * Метод меняет ключ и значение словаря местами
     *
     * @param map - словарь
     * @param <K> - ключ
     * @param <V> - значение
     * @return resultMap - словарь
     */
    public static <K, V> Map<V, Collection<K>> revertMap(Map<? extends K, ? extends V> map) {
        Map<V, Collection<K>> resultMap = new HashMap<>();

        Set<K> keys = (Set<K>) map.keySet();
        for (K key : keys) {
            //получаем значение из словаря map по ключу
            V value = map.get(key);
            resultMap.compute(value, (v, ks) -> {
                if (ks == null) {
                    //создаем множество, если ничего нет
                    ks = new HashSet<>();
                }
                ks.add(key);
                return ks;
            });
        }
        return resultMap;
    }

    /**
     * Метод удаляет дубликаты в коллекции
     *
     * @param coll - передаем коллекцию
     * @param <T>  - тип данных
     * @return HashSet - множество переданной коллекции
     */
    public static <T> Collection<T> removeDuplications(Collection<T> coll) {
        return new HashSet<>(coll);
    }
}
