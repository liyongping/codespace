drop table MSC.v_student;
drop table MSC.v_class;
drop table MSC.v_score;

CREATE TABLE MSC.v_student (
sid   number,
name  VARCHAR2(10)
);

CREATE TABLE MSC.v_class (
cid   number,
name  VARCHAR2(10)
);


CREATE TABLE MSC.v_score (
sid   number,
cid   number,
point number
);


select s.name student_name, 
c.name class_name,
sc.point point
from MSC.v_student s,
MSC.v_class c,
MSC.v_score sc
where sc.sid = s.sid
and sc.cid = c.cid;


select s.name student_name, 
sc.point point
from MSC.v_student s,
MSC.v_score sc
where sc.sid (+)= s.sid;

select s.name student_name, 
sc.point point
from MSC.v_student s,
MSC.v_score sc
where sc.sid = s.sid(+);

INSERT INTO MSC.v_student VALUES(1,'studentA');
INSERT INTO MSC.v_student VALUES(2,'studentB');
INSERT INTO MSC.v_student VALUES(3,'studentC');
INSERT INTO MSC.v_student VALUES(4,'studentD');
INSERT INTO MSC.v_student VALUES(5,'studentE');
INSERT INTO MSC.v_student VALUES(6,'studentF');

INSERT INTO MSC.v_class VALUES(0,'default');
INSERT INTO MSC.v_class VALUES(1,'chinese');
INSERT INTO MSC.v_class VALUES(2,'english');
INSERT INTO MSC.v_class VALUES(3,'japan');
INSERT INTO MSC.v_class VALUES(4,'indian');
INSERT INTO MSC.v_class VALUES(5,'Korean');

INSERT INTO MSC.v_score VALUES(1,1,90);
INSERT INTO MSC.v_score VALUES(1,2,80);
INSERT INTO MSC.v_score VALUES(1,3,85);
INSERT INTO MSC.v_score VALUES(1,4,60);

INSERT INTO MSC.v_score VALUES(2,1,92);
INSERT INTO MSC.v_score VALUES(2,2,82);
INSERT INTO MSC.v_score VALUES(2,3,85);
INSERT INTO MSC.v_score VALUES(2,4,62);

INSERT INTO MSC.v_score VALUES(3,1,93);
INSERT INTO MSC.v_score VALUES(3,2,83);
INSERT INTO MSC.v_score VALUES(3,3,83);
INSERT INTO MSC.v_score VALUES(3,4,63);

INSERT INTO MSC.v_score VALUES(4,1,94);
INSERT INTO MSC.v_score VALUES(4,2,84);
INSERT INTO MSC.v_score VALUES(4,3,84);
INSERT INTO MSC.v_score VALUES(4,4,64);

INSERT INTO MSC.v_score VALUES(5,1,95);
INSERT INTO MSC.v_score VALUES(5,2,85);
INSERT INTO MSC.v_score VALUES(5,3,85);
INSERT INTO MSC.v_score VALUES(5,4,65);
INSERT INTO MSC.v_score VALUES(10,11,10000);