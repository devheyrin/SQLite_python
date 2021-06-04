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

