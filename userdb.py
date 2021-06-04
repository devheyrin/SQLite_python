import sqlite3

from sql import Sql
from uservo import UserVO


class UserDB:
    def __init__(self, dbName):
        self.__dbName = dbName;  # dbName이라는 이름의 공간을 생성

    def getConn(self):
        con = sqlite3.connect(self.__dbName);  # dbName에 접속
        cursor = con.cursor();
        return {'con': con, 'cursor': cursor};

    def close(self, cc):
        if cc['cursor'] != None:
            cc['cursor'].close();
        if cc['con'] != None:
            cc['con'].close();

    def makeTable(self):
        cc = self.getConn();
        print(cc);
        cc['cursor'].execute(Sql.make_userdb);
        cc['con'].commit();  # 반영시킨다
        self.close(cc);

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
        print('%s 조회 되었습니다' % id);
        result = None;
        cc = self.getConn();
        cc['cursor'].execute(Sql.select_userdb, (id,));  # 요청보내기
        obj = cc['cursor'].fetchone();  # 받아온 것을 obj에 담기(id, pwd, name)
        result = UserVO(obj[0], obj[1], obj[2]);
        self.close(cc);
        return result;

    def selectall(self):
        print('전체가 조회되었습니다');
        results = [];
        cc = self.getConn();
        cc['cursor'].execute(Sql.selectall_userdb);
        all = cc['cursor'].fetchall();  # 여러개를 한꺼번에 가져올때
        for u in all:
            rs = UserVO(u[0], u[1], u[2]);
            results.append(rs);
        self.close(cc);
        return results;

