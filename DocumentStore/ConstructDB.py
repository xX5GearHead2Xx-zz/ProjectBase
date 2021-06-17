from Data import Sqlite


def ConstructDocumentStore():
    connection_string = '/Users/joshuaparsons/PycharmProjects/ProjectBase/DocumentStore/Documents/Document.db'
    sqlite_provider = Sqlite.SqliteProvider(connection_string)
    if sqlite_provider.ExecuteNonQuery(''):
        print('database created successfully...creating tables...')
        sql = (
            ' create table Document ( '
            ' Document_ID varchar(36),'
            ' DOC_Name varchar(200),'
            ' DOC_Extension varchar(50),'
            ' DOC_Path varchar(1000),'
            ' DOC_Deleted bit'
            ' )'
        )
        if sqlite_provider.ExecuteNonQuery(sql):
            print('Documents table created successfully')