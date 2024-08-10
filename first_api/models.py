from extensions import db 

class User(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    email = db.Column(db.String(100))

    def to_dict(self): 
        return {"name":self.name, "email":self.email}
