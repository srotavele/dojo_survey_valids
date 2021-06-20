from ..config.mysqlconnections import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self, data):
        self.id  = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojo_survey_schema').query_db(query)

        dojos = []

        for row in results:
            dojos.append(cls(row))
        return dojos
    
    @classmethod
    def create(cls,data):
        query = "INSERT INTO dojos (name, location, language, comment, created_at, updated_at ) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"

        results = connectToMySQL('dojo_survey_schema').query_db(query,data)
      
        return results

    @classmethod
    def get_results(cls):
        query = "SELECT * FROM dojos ORDER BY id DESC LIMIT 1;"
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        return results
    
    @staticmethod
    def validate_survey(post_data):
        is_valid = True
        
        if len(post_data['name']) < 2:
            flash("Name must be at least two characters.")
            is_valid = False
            
        if len(post_data['location']) < 3:
            flash("Please enter a valid location.")
            is_valid = False
            
        if len(post_data['language']) < 1:
            flash("Please enter a Language.")
            is_valid =  False
            
        if len(post_data['comment']) < 1:
            flash("Please enter a comment.")
            is_valid = False
            
        return is_valid