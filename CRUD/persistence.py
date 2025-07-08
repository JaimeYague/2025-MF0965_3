from db import get_connection


class CustomerRepository:
    def fetch_all(self):
        query = """
        SELECT Code, Name, Population
        FROM `world`.`country`;
        SELECT Name, Population 
        FROM `city`.`world`;
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    def delete(self, customer_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM world WHERE Code = %s", (Code,))
        conn.commit()
        cursor.close()
        conn.close()

    # métodos add(id), update(id), etc.
