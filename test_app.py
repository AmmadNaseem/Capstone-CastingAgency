import unittest
import json
import os
from datetime import date
from models import setup_db,Actor, Movie
from flask_sqlalchemy import SQLAlchemy
from app import create_app



class CapStoneCastingAppTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client

        DB_HOST = os.getenv('DB_HOST', 'localhost:5432')
        DB_USER = os.getenv('DB_USER', 'postgres')
        DB_PASSWORD = os.getenv('DB_PASSWORD', '134256')
        DB_NAME = os.getenv('DB_NAME', 'test_capstone')
        self.database_path = "postgresql://{}:{}@{}/{}".format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)

        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass


    executive_producer = {
             'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFCWnZGSzAzdDVWcXBPWEtmSmJwUCJ9.eyJpc3MiOiJodHRwczovL2Z1bGxzdGFja25hbm9kZWdyZWVhYW1hZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjQyM2YzZjg5MzZjYzA0MWNmYzM0YjczIiwiYXVkIjoiY2FzdGluZ0FwaSIsImlhdCI6MTY4MDE2ODY3NiwiZXhwIjoxNjgwMTc1ODc2LCJhenAiOiJmaUFHSFdLdEVGOGVJak15c1VxWVFwdlZqclNCME1taCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.PrRffDmv-YsFflULciGxqya2Txdmf8tO5_IZnSjxKhYncgZ7szt-pLJaOoERTafEy6sAzaucwUwvqjuG0hp72hkkACi_hIfTixtcT7heJdjfbSxCpi2cKHH7z1OWCbiR-soiFR-aFCAnCpqpRSD3sIn8NzifoRFyHQ2HOdT1JNN4QOd5K6O2vPL2_AHLFLF5ECU0U8HQxznScdEpDFiSBCQirURy15fMtvCDapZIjSypcl5AqWtGQGhAqQ_lwSpbqpzkwALO4EXLQGC-hl3RB9fdQwU5QEoFmmVYPvNlv8oJT_zACiFvij_N0FpftZCkh3e5YZx8D-DRuF5B1KYwIQ"
        }
        
    casting_assisitant= {
             'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFCWnZGSzAzdDVWcXBPWEtmSmJwUCJ9.eyJpc3MiOiJodHRwczovL2Z1bGxzdGFja25hbm9kZWdyZWVhYW1hZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjQyM2YzYTNlMTExOGRhODNmZjFhNGZlIiwiYXVkIjoiY2FzdGluZ0FwaSIsImlhdCI6MTY4MDE2OTA4MSwiZXhwIjoxNjgwMTc2MjgxLCJhenAiOiJmaUFHSFdLdEVGOGVJak15c1VxWVFwdlZqclNCME1taCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsInBvc3Q6YWN0b3JzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.DC4GE1mvpmxkVHnM2hog_3AZyrUI7xWTESOF0OPZg7VkXC5YoG9ea6JH2WPuRMn8yJcAFCtB1sWJ56C2NMVJThqN9b1k9yIHV84jARvbgnQ8CYpwcgogmt_PGfhE8N6IoyhR_flw3ZIiXJcnEYhl65OMV4O9kIldJMak1_yl7d5J0IZz3c34zxxKvRXh3g-YA52QTKCiQ-bruMFOwKXzegW8s4-l-QlEQLFt3tgK0g81H36O5fM8l4iVm0cVzrXTmQCLBcqCGccp5k0_XWny5ufWvSqdhZtZ8vih4ASTaXCnqIf9uQxkOy-LM4jeoIyLv5Z-IAcjGmxcke8UeUXj0A"
        }
 

    def test_index(self):
        tester = self.client(self)
        response = tester.get('/')
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])

    def test_get_athors(self):    
        casting_assisitant= {
             'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFCWnZGSzAzdDVWcXBPWEtmSmJwUCJ9.eyJpc3MiOiJodHRwczovL2Z1bGxzdGFja25hbm9kZWdyZWVhYW1hZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjQyM2YzYTNlMTExOGRhODNmZjFhNGZlIiwiYXVkIjoiY2FzdGluZ0FwaSIsImlhdCI6MTY4MDE2OTA4MSwiZXhwIjoxNjgwMTc2MjgxLCJhenAiOiJmaUFHSFdLdEVGOGVJak15c1VxWVFwdlZqclNCME1taCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsInBvc3Q6YWN0b3JzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.DC4GE1mvpmxkVHnM2hog_3AZyrUI7xWTESOF0OPZg7VkXC5YoG9ea6JH2WPuRMn8yJcAFCtB1sWJ56C2NMVJThqN9b1k9yIHV84jARvbgnQ8CYpwcgogmt_PGfhE8N6IoyhR_flw3ZIiXJcnEYhl65OMV4O9kIldJMak1_yl7d5J0IZz3c34zxxKvRXh3g-YA52QTKCiQ-bruMFOwKXzegW8s4-l-QlEQLFt3tgK0g81H36O5fM8l4iVm0cVzrXTmQCLBcqCGccp5k0_XWny5ufWvSqdhZtZ8vih4ASTaXCnqIf9uQxkOy-LM4jeoIyLv5Z-IAcjGmxcke8UeUXj0A"
        }
        tester = self.client(self)
        res = tester.get('/actors', headers=casting_assisitant)
        data = json.loads(res.data)

        if res.status_code == 200:
            # movies were found
            self.assertTrue(data['success'])
            self.assertIsInstance(data['actors'], list)
        elif res.status_code == 401:
            self.assertFalse(data['success'])
        else:
            # no movies were found
            self.assertFalse(data['success'])
        
    def test_401_get_athors(self):
        
        tester = self.client(self)
        res = tester.get('/actors')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message']['description'], 'Authorization header is expected.') 
      
    def test_add_actor(self):
        
        executive_producer = {
             'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFCWnZGSzAzdDVWcXBPWEtmSmJwUCJ9.eyJpc3MiOiJodHRwczovL2Z1bGxzdGFja25hbm9kZWdyZWVhYW1hZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjQyM2YzZjg5MzZjYzA0MWNmYzM0YjczIiwiYXVkIjoiY2FzdGluZ0FwaSIsImlhdCI6MTY4MDE2ODY3NiwiZXhwIjoxNjgwMTc1ODc2LCJhenAiOiJmaUFHSFdLdEVGOGVJak15c1VxWVFwdlZqclNCME1taCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.PrRffDmv-YsFflULciGxqya2Txdmf8tO5_IZnSjxKhYncgZ7szt-pLJaOoERTafEy6sAzaucwUwvqjuG0hp72hkkACi_hIfTixtcT7heJdjfbSxCpi2cKHH7z1OWCbiR-soiFR-aFCAnCpqpRSD3sIn8NzifoRFyHQ2HOdT1JNN4QOd5K6O2vPL2_AHLFLF5ECU0U8HQxznScdEpDFiSBCQirURy15fMtvCDapZIjSypcl5AqWtGQGhAqQ_lwSpbqpzkwALO4EXLQGC-hl3RB9fdQwU5QEoFmmVYPvNlv8oJT_zACiFvij_N0FpftZCkh3e5YZx8D-DRuF5B1KYwIQ"
        }

        actor = {
            'name' : 'Critiano randoldo',
            'age' : 45
        } 
        
        tester = self.client(self)
        res =  tester.post('/actors', json = actor, headers = executive_producer)
        data = json.loads(res.data)
        if res.status_code == 200:
            self.assertEqual(res.status_code, 200)
            self.assertTrue(data['success'])
            self.assertEqual(data['created'], 1)
        elif res.status_code == 401:
            self.assertFalse(data['success'])
        else:
            self.assertFalse(data['success'])
        
      

    def test_error_401_add_actor(self):
        actor = {
            'name' : 'Critiano randoldo',
            'age' : 45
            }  
        tester = self.client(self)
        res =  tester.post('/actors', json = actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message']['description'], 'Authorization header is expected.')

    def test_update_actor(self):
            
            executive_producer = {
                'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFCWnZGSzAzdDVWcXBPWEtmSmJwUCJ9.eyJpc3MiOiJodHRwczovL2Z1bGxzdGFja25hbm9kZWdyZWVhYW1hZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjQyM2YzZjg5MzZjYzA0MWNmYzM0YjczIiwiYXVkIjoiY2FzdGluZ0FwaSIsImlhdCI6MTY4MDE2ODY3NiwiZXhwIjoxNjgwMTc1ODc2LCJhenAiOiJmaUFHSFdLdEVGOGVJak15c1VxWVFwdlZqclNCME1taCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.PrRffDmv-YsFflULciGxqya2Txdmf8tO5_IZnSjxKhYncgZ7szt-pLJaOoERTafEy6sAzaucwUwvqjuG0hp72hkkACi_hIfTixtcT7heJdjfbSxCpi2cKHH7z1OWCbiR-soiFR-aFCAnCpqpRSD3sIn8NzifoRFyHQ2HOdT1JNN4QOd5K6O2vPL2_AHLFLF5ECU0U8HQxznScdEpDFiSBCQirURy15fMtvCDapZIjSypcl5AqWtGQGhAqQ_lwSpbqpzkwALO4EXLQGC-hl3RB9fdQwU5QEoFmmVYPvNlv8oJT_zACiFvij_N0FpftZCkh3e5YZx8D-DRuF5B1KYwIQ"
            }

            actor = {
                'name' : 'Leon Messi',
            } 
            
            tester = self.client(self)
            res =  tester.patch('/actors/1', json = actor, headers = executive_producer)
            data = json.loads(res.data)
            if res.status_code == 200:
                self.assertEqual(res.status_code, 200)
                self.assertTrue(data['success'])
                self.assertEqual(data['updated'], 1)
            elif res.status_code == 401:
                self.assertFalse(data['success'])
            else:
              self.assertEqual(res.status_code, 404)
              self.assertFalse(data['success'])
                

        
         

    def test_error_400_update_actor(self):
            
            executive_producer = {
                'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFCWnZGSzAzdDVWcXBPWEtmSmJwUCJ9.eyJpc3MiOiJodHRwczovL2Z1bGxzdGFja25hbm9kZWdyZWVhYW1hZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjQyM2YzZjg5MzZjYzA0MWNmYzM0YjczIiwiYXVkIjoiY2FzdGluZ0FwaSIsImlhdCI6MTY4MDE2ODY3NiwiZXhwIjoxNjgwMTc1ODc2LCJhenAiOiJmaUFHSFdLdEVGOGVJak15c1VxWVFwdlZqclNCME1taCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.PrRffDmv-YsFflULciGxqya2Txdmf8tO5_IZnSjxKhYncgZ7szt-pLJaOoERTafEy6sAzaucwUwvqjuG0hp72hkkACi_hIfTixtcT7heJdjfbSxCpi2cKHH7z1OWCbiR-soiFR-aFCAnCpqpRSD3sIn8NzifoRFyHQ2HOdT1JNN4QOd5K6O2vPL2_AHLFLF5ECU0U8HQxznScdEpDFiSBCQirURy15fMtvCDapZIjSypcl5AqWtGQGhAqQ_lwSpbqpzkwALO4EXLQGC-hl3RB9fdQwU5QEoFmmVYPvNlv8oJT_zACiFvij_N0FpftZCkh3e5YZx8D-DRuF5B1KYwIQ"
            }

            actor = {
                'name' : 'Leon Messi',
            } 
            
            tester = self.client(self)
            res =  tester.patch('/actors/34341', json = actor, headers = executive_producer)
            data = json.loads(res.data)
            if res.status_code == 404:
                self.assertEqual(res.status_code, 404)
                self.assertFalse(data['success'])
                self.assertEqual(data['message'], 'Actor with id 34341 not found in database.')    
           
            elif res.status_code == 401:
                self.assertFalse(data['success'])
            else:
                self.assertFalse(data['success'])
    
    def test_delete_actor(self):  
            executive_producer = {
                'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFCWnZGSzAzdDVWcXBPWEtmSmJwUCJ9.eyJpc3MiOiJodHRwczovL2Z1bGxzdGFja25hbm9kZWdyZWVhYW1hZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjQyM2YzZjg5MzZjYzA0MWNmYzM0YjczIiwiYXVkIjoiY2FzdGluZ0FwaSIsImlhdCI6MTY4MDE2ODY3NiwiZXhwIjoxNjgwMTc1ODc2LCJhenAiOiJmaUFHSFdLdEVGOGVJak15c1VxWVFwdlZqclNCME1taCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.PrRffDmv-YsFflULciGxqya2Txdmf8tO5_IZnSjxKhYncgZ7szt-pLJaOoERTafEy6sAzaucwUwvqjuG0hp72hkkACi_hIfTixtcT7heJdjfbSxCpi2cKHH7z1OWCbiR-soiFR-aFCAnCpqpRSD3sIn8NzifoRFyHQ2HOdT1JNN4QOd5K6O2vPL2_AHLFLF5ECU0U8HQxznScdEpDFiSBCQirURy15fMtvCDapZIjSypcl5AqWtGQGhAqQ_lwSpbqpzkwALO4EXLQGC-hl3RB9fdQwU5QEoFmmVYPvNlv8oJT_zACiFvij_N0FpftZCkh3e5YZx8D-DRuF5B1KYwIQ"
            }

            tester = self.client(self)
            res =  tester.delete('/actors/1', headers = executive_producer)
            data = json.loads(res.data)
            if res.status_code == 200:
                self.assertTrue(data['success'])
                self.assertEqual(data['deleted'], 1)
            elif res.status_code == 401:
                self.assertFalse(data['success'])
            else:
                self.assertFalse(data['success'])

    def test_error_401_delete_actor(self): 
        tester = self.client(self)
        res =  tester.delete('/actors/4')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message']['description'], 'Authorization header is expected.')

# ===========================TEST CASES FOR MOVIES=============================

    def test_get_movies(self):
        
        casting_assisitant= {
             'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFCWnZGSzAzdDVWcXBPWEtmSmJwUCJ9.eyJpc3MiOiJodHRwczovL2Z1bGxzdGFja25hbm9kZWdyZWVhYW1hZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjQyM2YzYTNlMTExOGRhODNmZjFhNGZlIiwiYXVkIjoiY2FzdGluZ0FwaSIsImlhdCI6MTY4MDE2OTA4MSwiZXhwIjoxNjgwMTc2MjgxLCJhenAiOiJmaUFHSFdLdEVGOGVJak15c1VxWVFwdlZqclNCME1taCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsInBvc3Q6YWN0b3JzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.DC4GE1mvpmxkVHnM2hog_3AZyrUI7xWTESOF0OPZg7VkXC5YoG9ea6JH2WPuRMn8yJcAFCtB1sWJ56C2NMVJThqN9b1k9yIHV84jARvbgnQ8CYpwcgogmt_PGfhE8N6IoyhR_flw3ZIiXJcnEYhl65OMV4O9kIldJMak1_yl7d5J0IZz3c34zxxKvRXh3g-YA52QTKCiQ-bruMFOwKXzegW8s4-l-QlEQLFt3tgK0g81H36O5fM8l4iVm0cVzrXTmQCLBcqCGccp5k0_XWny5ufWvSqdhZtZ8vih4ASTaXCnqIf9uQxkOy-LM4jeoIyLv5Z-IAcjGmxcke8UeUXj0A"
        }
        
        tester = self.client(self)
        res = tester.get('/movies', headers=casting_assisitant)
        data = json.loads(res.data)

        if res.status_code == 200:
            # movies were found
            self.assertTrue(data['success'])
            self.assertIsInstance(data['movies'], list)
        elif res.status_code==401:
            self.assertFalse(data['success'])
        else:
            # no movies were found
            self.assertFalse(data['success'])
            self.assertEqual(data['message'], 'No movie found in database.')

    def test_401_get_movies(self):
        
        tester = self.client(self)
        res = tester.get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message']['description'], 'Authorization header is expected.') 


    def test_add_movie(self):
        
        executive_producer = {
             'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFCWnZGSzAzdDVWcXBPWEtmSmJwUCJ9.eyJpc3MiOiJodHRwczovL2Z1bGxzdGFja25hbm9kZWdyZWVhYW1hZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjQyM2YzZjg5MzZjYzA0MWNmYzM0YjczIiwiYXVkIjoiY2FzdGluZ0FwaSIsImlhdCI6MTY4MDE2ODY3NiwiZXhwIjoxNjgwMTc1ODc2LCJhenAiOiJmaUFHSFdLdEVGOGVJak15c1VxWVFwdlZqclNCME1taCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.PrRffDmv-YsFflULciGxqya2Txdmf8tO5_IZnSjxKhYncgZ7szt-pLJaOoERTafEy6sAzaucwUwvqjuG0hp72hkkACi_hIfTixtcT7heJdjfbSxCpi2cKHH7z1OWCbiR-soiFR-aFCAnCpqpRSD3sIn8NzifoRFyHQ2HOdT1JNN4QOd5K6O2vPL2_AHLFLF5ECU0U8HQxznScdEpDFiSBCQirURy15fMtvCDapZIjSypcl5AqWtGQGhAqQ_lwSpbqpzkwALO4EXLQGC-hl3RB9fdQwU5QEoFmmVYPvNlv8oJT_zACiFvij_N0FpftZCkh3e5YZx8D-DRuF5B1KYwIQ"
        }

        movie = {
            'title' : 'Test Movie',
            'release_date' : date.today()
        } 
        
        tester = self.client(self)
        res =  tester.post('/movies', json = movie, headers = executive_producer)
        data = json.loads(res.data)
       
        if res.status_code == 200:
           self.assertEqual(res.status_code, 200)
           self.assertTrue(data['success'])
           self.assertEqual(data['created'], 1)
        elif res.status_code == 401:
            self.assertFalse(data['success'])
        else:
            self.assertFalse(data['success'])

    def test_error_401_add_movie(self):
        movie = {
            'title' : 'Test Movie',
            'release_date' : date.today()
        } 
        tester = self.client(self)
        res =  tester.post('/movies', json = movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message']['description'], 'Authorization header is expected.')

    def test_update_movie(self):
            
            executive_producer = {
                'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFCWnZGSzAzdDVWcXBPWEtmSmJwUCJ9.eyJpc3MiOiJodHRwczovL2Z1bGxzdGFja25hbm9kZWdyZWVhYW1hZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjQyM2YzZjg5MzZjYzA0MWNmYzM0YjczIiwiYXVkIjoiY2FzdGluZ0FwaSIsImlhdCI6MTY4MDE2ODY3NiwiZXhwIjoxNjgwMTc1ODc2LCJhenAiOiJmaUFHSFdLdEVGOGVJak15c1VxWVFwdlZqclNCME1taCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.PrRffDmv-YsFflULciGxqya2Txdmf8tO5_IZnSjxKhYncgZ7szt-pLJaOoERTafEy6sAzaucwUwvqjuG0hp72hkkACi_hIfTixtcT7heJdjfbSxCpi2cKHH7z1OWCbiR-soiFR-aFCAnCpqpRSD3sIn8NzifoRFyHQ2HOdT1JNN4QOd5K6O2vPL2_AHLFLF5ECU0U8HQxznScdEpDFiSBCQirURy15fMtvCDapZIjSypcl5AqWtGQGhAqQ_lwSpbqpzkwALO4EXLQGC-hl3RB9fdQwU5QEoFmmVYPvNlv8oJT_zACiFvij_N0FpftZCkh3e5YZx8D-DRuF5B1KYwIQ"
            }

            movie = {
                 'release_date' : date.today(),
            } 
            
            tester = self.client(self)
            res =  tester.patch('/movies/1', json = movie, headers = executive_producer)
            data = json.loads(res.data)
            if res.status_code == 200:
                # movies were found
                self.assertFalse(data['success'])
                self.assertEqual(res.status_code, 200)
                self.assertTrue(data['success'])
                self.assertEqual(data['updated'], 1)
            elif res.status_code==401:
                self.assertFalse(data['success'])    
            else:
            # no movies were found
              self.assertEqual(res.status_code, 404)
              self.assertFalse(data['success'])
                

    def test_error_400_update_movie(self):
            
            executive_producer = {
                'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFCWnZGSzAzdDVWcXBPWEtmSmJwUCJ9.eyJpc3MiOiJodHRwczovL2Z1bGxzdGFja25hbm9kZWdyZWVhYW1hZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjQyM2YzZjg5MzZjYzA0MWNmYzM0YjczIiwiYXVkIjoiY2FzdGluZ0FwaSIsImlhdCI6MTY4MDE2ODY3NiwiZXhwIjoxNjgwMTc1ODc2LCJhenAiOiJmaUFHSFdLdEVGOGVJak15c1VxWVFwdlZqclNCME1taCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.PrRffDmv-YsFflULciGxqya2Txdmf8tO5_IZnSjxKhYncgZ7szt-pLJaOoERTafEy6sAzaucwUwvqjuG0hp72hkkACi_hIfTixtcT7heJdjfbSxCpi2cKHH7z1OWCbiR-soiFR-aFCAnCpqpRSD3sIn8NzifoRFyHQ2HOdT1JNN4QOd5K6O2vPL2_AHLFLF5ECU0U8HQxznScdEpDFiSBCQirURy15fMtvCDapZIjSypcl5AqWtGQGhAqQ_lwSpbqpzkwALO4EXLQGC-hl3RB9fdQwU5QEoFmmVYPvNlv8oJT_zACiFvij_N0FpftZCkh3e5YZx8D-DRuF5B1KYwIQ"
            }

            movie = {
                 'release_date' : date.today(),
            } 
            
            tester = self.client(self)
            res =  tester.patch('/movies/34341', json = movie, headers = executive_producer)
            data = json.loads(res.data)
            if res.status_code==200:
                self.assertEqual(res.status_code, 404)
                self.assertFalse(data['success'])
                self.assertEqual(data['message'], 'movie with id 34341 not found in database.')
            elif res.status_code == 401:
                self.assertFalse(data['success'])
            else:
                self.assertFalse(data['success'])
    
    def test_delete_movie(self):
            
            executive_producer = {
                'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFCWnZGSzAzdDVWcXBPWEtmSmJwUCJ9.eyJpc3MiOiJodHRwczovL2Z1bGxzdGFja25hbm9kZWdyZWVhYW1hZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjQyM2YzZjg5MzZjYzA0MWNmYzM0YjczIiwiYXVkIjoiY2FzdGluZ0FwaSIsImlhdCI6MTY4MDE2ODY3NiwiZXhwIjoxNjgwMTc1ODc2LCJhenAiOiJmaUFHSFdLdEVGOGVJak15c1VxWVFwdlZqclNCME1taCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.PrRffDmv-YsFflULciGxqya2Txdmf8tO5_IZnSjxKhYncgZ7szt-pLJaOoERTafEy6sAzaucwUwvqjuG0hp72hkkACi_hIfTixtcT7heJdjfbSxCpi2cKHH7z1OWCbiR-soiFR-aFCAnCpqpRSD3sIn8NzifoRFyHQ2HOdT1JNN4QOd5K6O2vPL2_AHLFLF5ECU0U8HQxznScdEpDFiSBCQirURy15fMtvCDapZIjSypcl5AqWtGQGhAqQ_lwSpbqpzkwALO4EXLQGC-hl3RB9fdQwU5QEoFmmVYPvNlv8oJT_zACiFvij_N0FpftZCkh3e5YZx8D-DRuF5B1KYwIQ"
            }

            tester = self.client(self)
            res =  tester.delete('/movies/1', headers = executive_producer)
            data = json.loads(res.data)
            if res.status_code==200:
                self.assertTrue(data['success'])
                self.assertEqual(data['deleted'], 1)
            elif res.status_code == 401:
                self.assertFalse(data['success'])
            else:
                self.assertFalse(data['success'])
    
       

    def test_error_401_delete_movie(self): 
        tester = self.client(self)
        res =  tester.delete('/movies/4')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message']['description'], 'Authorization header is expected.')


        

if __name__ == "__main__":
    unittest.main()
