package com.example.demo.parallel;

import java.util.ArrayList;
import java.util.List;

import javax.transaction.Transactional;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.annotation.Commit;

import com.example.demo.parallel.domain.Dept;
import com.example.demo.parallel.domain.DeptRepository;

@Commit
@SpringBootTest
public class TestDept3Repository {
	
	@Autowired
	DeptRepository deptRepository;
	
	@Test
	@Transactional
	void deptSave() {
		List<Dept> deptList = new ArrayList<Dept>();
		for(int i = 0; i<10000; i++) {
			deptList.add(new Dept(i, String.valueOf(i), String.valueOf(i)));
		}
		deptRepository.saveAll(deptList); // db에 저장
	}
	
//	@Test
//	@Transactional
//	void deptDel() {deptRepository.deleteAll();}
}
