from ..config.mysqlconnection import connectToMySQL
class Dojo:
    def __init__(self, data):
        self.id  = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        print(results)
        dojos = []
        
        for row in results:
            dojos.append(Dojo(row))
        return dojos