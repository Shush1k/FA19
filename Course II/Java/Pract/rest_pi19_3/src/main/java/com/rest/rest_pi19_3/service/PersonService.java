package com.rest.rest_pi19_3.service;

import com.rest.rest_pi19_3.entity.Person;
import com.rest.rest_pi19_3.repository.PersonRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class PersonService {

    @Autowired
    private PersonRepository personRepository;
    public List<Person> findAll(){
        return personRepository.findAll();
    }
    public void create(Person person) {
        personRepository.save(person);
    }
}

