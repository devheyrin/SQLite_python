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