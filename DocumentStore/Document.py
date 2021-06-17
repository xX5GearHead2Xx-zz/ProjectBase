import sys
from uuid import uuid4
from File import FileManager
from Data import Sqlite

connection_string = '/Users/joshuaparsons/PycharmProjects/ProjectBase/DocumentStore/Documents/Document.db'


class Document:
    def __init__(self, extension, name, path, content):
        self.document_id = uuid4()
        self.extension = extension
        self.name = name
        self.path = path
        self.content = content

    def SaveFile(self):
        try:
            sql = (
                ' insert into Document '
                ' Document_ID,'
                ' DOC_Name,'
                ' DOC_Extension,'
                ' DOC_Path,'
                ' DOC_Deleted'
                ' ) values ('
                ' "'+str(self.document_id)+'",'
                ' "' + str(self.name) + '",'
                ' "' + str(self.extension) + '",'
                ' "'+str(self.path)+'",'
                ' 0'
                ' )'
            )

            sql_provider = Sqlite.SqliteProvider(connection_string)
            if sql_provider.ExecuteNonQuery(sql):
                document_full_path = str(self.path + self.name + self.document_id + self.extension)
                FileManager.WriteFile(document_full_path, self.content)
                return True
            else:
                return False
        except:
            print(sys.exc_info())
            return False

    def SearchFile(self):
        pass