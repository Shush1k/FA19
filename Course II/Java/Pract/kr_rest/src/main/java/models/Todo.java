package models;


import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.time.LocalDate;

/**
 * Задание имеет следующие атрибуты:
 * 1.	Уникальный идентификатор
 * 2.	Наименование
 * 3.	Описание
 * 4.	Дата выполнения
 * 5.	Выполнено (значение Да/Нет)
 * 6.	Категория
 * 7.	Пользователь
 */

@Entity
public class Todo {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;
    private String topic;
    private String description;
    private LocalDate completeDate;
    private boolean complete;
    private String category;
    private String user;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getTopic() {
        return topic;
    }

    public void setTopic(String topic) {
        this.topic = topic;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public LocalDate getCompleteDate() {
        return completeDate;
    }

    public void setCompleteDate(LocalDate completeDate) {
        this.completeDate = completeDate;
    }

    public boolean isComplete() {
        return complete;
    }

    public void setComplete(boolean complete) {
        this.complete = complete;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }

    @Override
    public String toString() {
        return "Todo{" +
                "id=" + id +
                ", topic='" + topic + '\'' +
                ", description='" + description + '\'' +
                ", completeDate=" + completeDate +
                ", complete=" + complete +
                ", category='" + category + '\'' +
                ", user='" + user + '\'' +
                '}';
    }
}
