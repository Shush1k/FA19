package com.task_tracker.repository;

import com.task_tracker.entity.StatusTask;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface StatusTaskRepository extends JpaRepository<StatusTask, Long> {
}
