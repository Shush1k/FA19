package service;

import models.Person;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import repository.PersonRepository;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

@Service
public class PersonServiceImpl implements PersonService {

    private static final AtomicInteger PERSON_ID = new AtomicInteger();

    @Autowired
    PersonRepository personRepo;

    @Override
    public Person create(Person person) {

        final int personId = PERSON_ID.incrementAndGet();
        person.setId((long) personId);
        personRepo.save(person);
        return person;
    }

    @Override
    public List<Person> readAll() {
        return new ArrayList<>(personRepo.findAll());
    }

    @Override
    public Person read(int id) {
        return personRepo.findById(id);
    }

    @Override
    public boolean update(Person person, int id) {
        Person buff = personRepo.findById(id);
        if (buff == null){
            return false;
        }
        personRepo.delete(buff);
        personRepo.save(person);
        return true;
    }

    @Override
    public boolean delete(int id) {
        Person buff = personRepo.findById(id);
        if (buff != null) {
            personRepo.delete(buff);
            return true;
        }
        return false;
    }
}
