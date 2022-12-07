package com.example.demo.domain.db2;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

@Setter
@Getter
@ToString
@Entity
@AllArgsConstructor
@NoArgsConstructor
@Table(name="dept2")
public class Dept2 { // dept 엔티티 정보
	@Id
	private Integer deptno;
	private String dname;
	private String loc;
}