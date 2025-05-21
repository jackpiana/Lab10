from database.DB_connect import DBConnect
from model.Country import Country


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_all_countries():
        """
        restituisce un dizionario contenente tutte le nazioni del database
        la chiave principale del dizionario è CCode

        uso il codice e non l'abbreviazione univoca perchè la russia da problemi con ussr
        """
        countries = {}
        conn = DBConnect.get_connection()
        if conn is None:
            print("connection failed")
        else:
            cursor = conn.cursor(dictionary=True)
            query = """
            SELECT *
            FROM country
            """
            cursor.execute(query, ())
            res = cursor.fetchall()
            for c in res:
                countries[c["CCode"]] = Country(**c)
            cursor.close()
        conn.close()
        return countries

    @staticmethod
    def get_edges_filtered(year: int):
        edges = []
        conn = DBConnect.get_connection()
        if conn is None:
            print("connection failed")
        else:
            cursor = conn.cursor(dictionary=True)
            query = """
                    select state1no, state2no, year 
                    from contiguity c 
                    where conttype = 1
                    and year < %s
                    order by state1ab
                    """
            cursor.execute(query, (year,))
            res = cursor.fetchall()
            for edge in res:
                edges.append(edge)
                cursor.close()
        conn.close()
        return edges

if __name__ == "__main__":
    print(DAO.get_edges_filtered(1970))
