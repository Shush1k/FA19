package service;

import models.Todo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import repository.TodoRepository;

import java.util.ArrayList;
import java.util.List;

@Service
public class TodoServiceImpl {
    @Autowired
    private TodoRepository todoRepository;

    public List<Todo> getTodoList() {
        List<Todo> todoList = new ArrayList<>();
        todoRepository.findAll().forEach(todoList::add);

        return todoList;
    }


    public int addItemTodoList(Todo todo) {
        int todoId = 0;
        todoRepository.save(todo);

        return todoId;

    }

}
