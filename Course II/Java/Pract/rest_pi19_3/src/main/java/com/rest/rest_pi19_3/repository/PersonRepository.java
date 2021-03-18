package com.rest.rest_pi19_3.repository;

import com.rest.rest_pi19_3.entity.Person;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PersonRepository extends JpaRepository<Person, Long> {
}
