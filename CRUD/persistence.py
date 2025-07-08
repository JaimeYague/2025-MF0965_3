from db import get_connection


class CustomerRepository:
    def fetch_all(self):
        query = """
        SELECT country.Code, country.Name, country.Population, city.Name, city.Population
        FROM `world`.`country`
        LEFT JOIN `city`
        ON country.Code=city.CountryCode;
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
