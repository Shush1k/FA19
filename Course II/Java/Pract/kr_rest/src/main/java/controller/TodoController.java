package controller;

import java.net.URI;
import java.util.List;

import models.Todo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;
import service.TodoServiceImpl;

@RestController
@RequestMapping("/todos")
public class TodoController {
    private final TodoServiceImpl todoServiceImpl;

    @Autowired
    public TodoController(TodoServiceImpl todoServiceImpl) {
        this.todoServiceImpl = todoServiceImpl;
    }


    @GetMapping("{username}/todos")
    public List<Todo> getAllTodos(@PathVariable String username){
        return todoServiceImpl.findByUsername(username);
    }

    @GetMapping("{username}/todos/{id}")
    public Todo getTodo(@PathVariable String username, @PathVariable long id){
        return todoServiceImpl.findById(id).get();
    }

    @DeleteMapping("{username}/todos/{id}")
    public ResponseEntity<Void> deleteTodo(
            @PathVariable String username, @PathVariable long id) {

        todoServiceImpl.deleteById(id);

        return ResponseEntity.noContent().build();
    }


    @PutMapping("{username}/todos/{id}")
    public ResponseEntity<Todo> updateTodo(
            @PathVariable String username,
            @PathVariable long id, @RequestBody Todo todo){
//        todoUpdated

        return new ResponseEntity<Todo>(todoUpdated, HttpStatus.OK);
    }

    @PostMapping("{username}/todos")
    public ResponseEntity<Void> createTodo(
            @PathVariable String username, @RequestBody Todo todo){
//        createdTodo

        URI uri = ServletUriComponentsBuilder.fromCurrentRequest()
                .path("/{id}").buildAndExpand(createdTodo.getId()).toUri();

        return ResponseEntity.created(uri).build();
    }

}
