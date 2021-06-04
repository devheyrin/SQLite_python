# SQLite 30분 완성 

회원 CRUD 구현하기

 

## 1. 프로젝트 생성 및 개발 환경 세팅

File > New project 로 새 프로젝트를 생성한다. 

![image-20210605015138389](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210605015138389.png)

프로젝트 이름 위에서 우클릭후 new > python file 을 눌러 app.py, userdb.py, uservo.py, sql.py를 만든다. 

각각의 파이썬 파일들이 하게 될 역할은 다음과 같다. 

- app.py : view역할. 이 프로젝트에서는 터미널창에서 insert, delete, update, select, select all 등의 명령을 입력해 그에 따라 CRUD가 처리되도록 만들 것이다. 
- uservo.py : Model 역할을 하는 class. UserVO라는 이름의 class를 생성해, 외부에서 필요에 따라 활용할 수 있는 model을 만들 것이다. 
- userdb.py : Control 역할을 하는 class. UserDB라는 이름의 class를 생성해 DB와 연동해 CRUD 명령을 처리한다. 
- sql.py : SQL문을 모아 놓은 class 



## 2. view 역할의 app.py 구성하기 

기본 구조는 다음과 같다. app.py가 실행되면 사용자는 i, s, sa, u, d, 중 하나를 입력해 회원가입, 회원조회, 모든회원조회, 회원정보수정, 회원정보삭제의 기능을 선택할 수 있다. 

```python
print('Start');

while True:
    cmd = input('다음 중 하나를 입력하세요.\n i: 회원가입\n s: 회원조회\n d: 회원삭제\n u: 회원정보수정\n sa: 모든 회원 조회\n');
    if cmd == 'q':
        print('프로그램을 종료합니다.');
        break;
    elif cmd == 'i':
        print('회원가입');
    elif cmd == 's':
        print('회원조회');
    elif cmd == 'sa':
        print('모든회원조회');
    elif cmd == 'u':
        print('회원정보수정');
    elif cmd == 'd':
        print('회원삭제');

print('End');
```

터미널에 i, s, sa, u, d 를 입력했을때 내용이 잘 출력되는지 확인한다. 



## 3. VO 만들기 

'회원'이 가질 속성은 id, name, pwd 이다. 이렇게 세 가지 속성을 가진 class 를 만들고, get&set 함수를 만들어 둔다. 

```python
class UserVO:
    def __init__(self, id, pwd, name):
        self.__id = id;
        self.__pwd = pwd;
        self.__name = name;
    def __str__(self):
        return '%s, %s, %s' % (self.__id, self.__pwd, self.__name); 
    def getId(self):
        return self.__id;
    def setId(self, id):
        self.__id = id;
    def getPwd(self):
        return self.__pwd;
    def setPwd(self, pwd):
        self.__pwd = pwd;
    def getName(self):
        return self.__name;
    def setName(self, name):
        self.__name = name;
```

파이썬의 class는  `__init__`, `__str__`이라는 내장 함수를 가지고 있다. 

`__init__` 함수는 생성자라고 할 수 있다. 이 클래스를 이용해서 객체를 만들고자 할 때 필요한 속성(변수)들을 정의하는 역할을 한다. UserVO클래스의 경우 id, pwd, name이라는 세 개의 값을 넣어주어야만 UserVO를 객체로 만들어 사용할 수 있다. 

이 때, `self.__id`처럼 변수 앞에 `__`를 붙이는 것은 **캡슐화**를 의미한다. 변수 앞에 언더바 두 개를 붙임으로써 외부에서 변수 값을 직접 변화시킬 수 없도록 만들 수 있다. 이렇게 캡슐화를 해 두었다면 변수 값에 접근하기 위해서는 get, set 함수를 통해야만 한다. get함수는 해당 변수의 값을 얻어올 때, set함수는 해당 변수의 값을 변화시킬 때 사용한다. 

`__str__` 함수는 객체를 String 형태로 출력할 수 있도록 하는 함수이다. 클래스에서 이 함수를 정의해두지 않으면 print()함수를 사용해 객체를 출력하려고 할 때, String 형태가 아니라 그 객체가 저장된 주소값이 출력된다. 

```
from uservo import UserVO

user1 = UserVO('id01', 'pwd01', 'name01');
print(user1);
```

객체를 만들고 출력하는 동일한 코드를 실행할 때, `__str__` 함수가 있는 경우와 없는 경우에 결과는 다르게 출력된다. 

1) `__str__` 함수가 없는 경우 

```
<uservo.UserVO object at 0x0000013A13C4F9E8>
```

2) `__str__` 함수가 있는 경우 - 다음과 같이 return에 명시한 형태('%s, %s, %s')로 userVO가 출력된다. 

```
id01, pwd01, name01
```



## 4. SQL 문 작성

DB와 연동하기 위해 필요한 SQL문은 Controller에 직접 입력해도 되지만, 여기에서는 class를 만들어 SQL문만 따로 분리해 두었다. 

```python
class Sql:
    make_userdb = '''
    CREATE TABLE IF NOT EXISTS USERDB 
    (
    ID TEXT PRIMARY KEY,
    PWD TEXT,
    NAME TEXT
    ) ''';
    insert_userdb = '''INSERT INTO USERDB VALUES (?,?,?)''';
    update_userdb = '''UPDATE USERDB SET PWD = ?, NAME = ? WHERE ID = ?''';
    delete_userdb = '''DELETE FROM USERDB WHERE ID = ?''';
    select_userdb = '''SELECT * FROM USERDB WHERE ID = ?''';
    selectall_userdb = '''SELECT * FROM USERDB''';
```

- make_userdb : 테이블 생성 구문이다. id를 primary key로 하고, id, pwd, name을 각각 열로 가지되 userdb라는 이름의 테이블이 없을 때만 생성하도록 만들었다. 
- insert_userdb : 테이블에 행을 삽입하는 구문이다. (?,?,?) 에는 사용자가 입력한 값을 넣어줄 수 있도록 controller에서 적절히 mapping하게 될 것이다. 
- update_userdb : 행을 수정하는 구문이다. 여기서는 id를 입력했을 때 pwd와 name을 수정할 수 있도록 작성했다. 
- delete_userdb : 행 삭제 구문이다. id를 입력하면 해당 행이 삭제되도록 작성했다. 
- select_userdb : 행 조회 구문이다. id를 입력하면 해당 행이 조회되도록 작성했다. 
- selectall_userdb : 모든 행을 조회하는 구문이다. 



## 5. app.py 수정

SQL문에 작성한대로 데이터를 받아올 수 있도록 view 역할을 하는 app.py를 수정한다. 

회원가입, 회원정보수정의 경우 값을 input을 통해 입력받아 id, pwd, name에 저장해 userVO객체로 만들어 둔다. 

회원조회의 경우 id만 입력받아 id라는 변수로 저장한다. 

```python
from uservo import UserVO

print('Start');

while True:
    cmd = input('다음 중 하나를 입력하세요.\n i: 회원가입\n s: 회원조회\n d: 회원삭제\n u: 회원정보수정\n sa: 모든 회원 조회\n');
    if cmd == 'q':
        print('프로그램을 종료합니다.');
        break;
    elif cmd == 'i':
        print('회원가입');
        id = input('id를 입력하세요');
        pwd = input('pwd를 입력하세요');
        name = input('이름을 입력하세요');
        user = UserVO(id, pwd, name);
        print(user, '회원가입되었습니다');
    elif cmd == 's':
        print('회원조회');
        id = input('조회할 회원의 id를 입력하세요');
        print(id, '님의 정보 조회');
    elif cmd == 'sa':
        print('모든회원조회');
    elif cmd == 'u':
        print('회원정보수정');
        id = input('수정할 회원의 id를 입력하세요');
        pwd = input('새로운 pwd를 입력하세요');
        name = input('새로운 이름을 입력하세요');
        user = UserVO(id, pwd, name);
        print(user, '수정되었습니다')
    elif cmd == 'd':
        print('회원삭제');

print('End');
```



## 6. DB(controller) 작성 

이제 본격적으로 SQLite와 연동해 데이터를 저장, 조회, 수정, 삭제해 보자. 

1. 가장 먼저 sqlite3 를 import한다. 

```
import sqlite3 
```

2. 다음으로 생성자를 만든다. userDB객체는 dbName을 입력해야 생성할 수 있도록 만든다. sqlite라는 DB 안에 dbName이라는 이름의 공간을 하나 생성한다고 생각하면 된다. 

```python
def __init__(self, dbName):
     self.__dbName = dbName;
```

3. dbName에 접속하는 getConn 함수를 만든다. 이 함수는 dictionary 형태로 con 객체와 cursor 객체를 리턴한다. 

```python
def getConn(self):
    con = sqlite3.connect(self.__dbName);  # dbName에 접속
    cursor = con.cursor();
    return {'con': con, 'cursor': cursor};
```

- con : sqlite 의 connect 함수를 사용해 dbName에 접속한다. 
- cursor: sql문을 실행하고, 쿼리 결과 집합에서 데이터를 가져오는 메서드를 호출할 수 있는 인스턴스 

4. 연결을 닫는 close함수를 만든다. 

```python
def close(self, cc):
    if cc['cursor'] != None:
    cc['cursor'].close();
    if cc['con'] != None:
    cc['con'].close();
```

- 연결이 존재할 경우에만 close한다. 

5. daName이라는 공간 안에 테이블을 만드는 makeTable 함수를 만든다. 

```python
def makeTable(self):
    cc = self.getConn(); # 연결 생성 
    print(cc);
    cc['cursor'].execute(Sql.make_userdb); # 테이블 생성 구문 실행 
    cc['con'].commit();  # 변경 내용을 반영시킨다
    self.close(cc); # 연결 닫기 
```

6. insert, delete, update, select 내용을 구현한다. 

```python
def insert(self, u):
    cc = self.getConn();
    cc['cursor'].execute(Sql.insert_userdb,  # 이 SQL문에
    (u.getId(),
    u.getPwd(),
    u.getName()));  # 이 내용을 매핑한다
    cc['con'].commit();
    self.close(cc);
    print('%s 등록 되었습니다' % u);

def delete(self, id):
    cc = self.getConn();
    cc['cursor'].execute(Sql.delete_userdb, (id,));
    cc['con'].commit();
    self.close(cc);
    print('%s 삭제 되었습니다' % id);

def update(self, u):
    pwd = u.getPwd();
    name = u.getName();
    cc = self.getConn();
    cc['cursor'].execute(Sql.update_userdb,
                         (u.getPwd(),
                          u.getName(),
                          u.getId()));
    cc['con'].commit();
    self.close(cc);
    print('%s 수정 되었습니다' % u);

def select(self, id):
    result = None;
    cc = self.getConn();
    cc['cursor'].execute(Sql.select_userdb, (id,));  # 요청보내기
    obj = cc['cursor'].fetchone();  # 받아온 것을 obj에 담기(id, pwd, name)
    result = UserVO(obj[0], obj[1], obj[2]);
    self.close(cc);
    return result;

def selectall(self):
    results = [];
    cc = self.getConn();
    cc['cursor'].execute(Sql.selectall_userdb);
    all = cc['cursor'].fetchall();  # 여러개를 한꺼번에 가져올때
    for u in all:
    rs = UserVO(u[0], u[1], u[2]);
    results.append(rs);
    self.close(cc);
    return results;
```



## 7. userDB를 호출하도록 app.py를 수정한다. 

```python
from userdb import UserDB
from uservo import UserVO

print('Start');

udb = UserDB('Shop');
udb.makeTable();

while True:
    cmd = input('다음 중 하나를 입력하세요.\n i: 회원가입\n s: 회원조회\n d: 회원삭제\n u: 회원정보수정\n sa: 모든 회원 조회\n');
    if cmd == 'q':
        print('프로그램을 종료합니다.');
        break;
    elif cmd == 'i':
        print('회원가입');
        id = input('id를 입력하세요');
        pwd = input('pwd를 입력하세요');
        name = input('이름을 입력하세요');
        user = UserVO(id, pwd, name);
        udb.insert(user); # insert
        #print(user, '회원가입되었습니다');
    elif cmd == 's':
        print('회원조회');
        id = input('조회할 회원의 id를 입력하세요');
        #print(id, '님의 정보 조회');
        user = udb.select(id); # select
        print(user);
    elif cmd == 'sa':
        print('모든회원조회');
        users = udb.selectall(); # select all
        for u in users:
            print(u);
    elif cmd == 'u':
        print('회원정보수정');
        id = input('수정할 회원의 id를 입력하세요');
        pwd = input('새로운 pwd를 입력하세요');
        name = input('새로운 이름을 입력하세요');
        user = UserVO(id, pwd, name);
        udb.update(user); # update
        #print(user, '수정되었습니다');
    elif cmd == 'd':
        print('회원삭제');
        id = input('삭제할 회원의 id를 입력하세요');
        udb.delete(id);
        #print(id,'님 삭제되었습니다');

print('End');
```

