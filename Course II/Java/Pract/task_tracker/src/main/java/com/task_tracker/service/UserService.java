package com.task_tracker.service;

import com.task_tracker.entity.User;
import com.task_tracker.repository.UserRepository;
import org.springframework.beans.BeanUtils;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
public class UserService {
    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }


    public List<User> findAll(){
        return userRepository.findAll();
    }


    @Transactional
    public User create(User user) {
        if (userRepository.findUserByLogin(user.getLogin()).isPresent()) {
            throw new RuntimeException();
        }
        return userRepository.save(user);
    }

    public User update(User user, User userFromDB) {
        BeanUtils.copyProperties(user, userFromDB, "id");
        return userRepository.save(userFromDB);
    }

    public boolean delete(User user) {
        if (user != null){
            userRepository.delete(user);
            return true;
        }
        return false;
    }
}