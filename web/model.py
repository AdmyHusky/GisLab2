import pyodbc
class read_files:
    def read(self,qurey_country):
        conn = pyodbc.connect(
            driver ='{SQL Server Native Client 11.0}',
            Server = 'DESKTOP-R8HODAT',
            Database= 'project2',
            Trusted_Connection='yes'
            )
        Country = qurey_country
        SQL = "SELECT NAME,geom.MakeValid().STArea() as Area FROM world WHERE NAME = '%s'"
        cursor = conn.cursor()
        cursor.execute(SQL%(Country)) 
        for row in cursor:
            return row