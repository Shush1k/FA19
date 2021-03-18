package com.rest.rest_pi19_3.controller;

import com.rest.rest_pi19_3.entity.Person;
import com.rest.rest_pi19_3.service.PersonService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class RestApiController {
    private final PersonService personService;

    @Autowired
    public RestApiController(PersonService personService) {
        this.personService = personService;
    }

    @PostMapping(value = "api/person")
    private ResponseEntity<?> create(@RequestBody Person person) {
        personService.create(person);
        return new ResponseEntity<>(HttpStatus.CREATED);
    }

    @GetMapping(value = "api/persons")
    private ResponseEntity<List<Person>> readAll() {
     final List<Person> personList = personService.findAll();
        return personList != null && !personList.isEmpty()
                ? new ResponseEntity<>(personList, HttpStatus.OK)
                : new ResponseEntity<>(HttpStatus.NOT_FOUND);
    }
}
