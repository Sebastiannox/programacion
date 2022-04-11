
import MySQLdb
import sys
from datetime import datetime as dt
import datetime


try:
    conn = MySQLdb.connect(
        user = "root",
        password="123456",
        host="localhost",
        port=3306,
        database="agenda2"
        )
except MySQLdb.Error as e:
    print(f"Error connecting to mysql Platform: {e}")
    sys.exit(1)
cur = conn.cursor()
cur.execute("select agenda.agenda_horaI, agenda.agenda_horaT, paciente.nombre, paciente.apellido from agenda, paciente where paciente.rut=agenda.pac_rut");
