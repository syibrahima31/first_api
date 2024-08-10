from flask import Blueprint, jsonify, request, render_template
from .models import User 
from extensions import db 

end_bp = Blueprint("end", __name__)

@end_bp.route("/")
def index(): 
    return "<h1> Bienvenue dans API </h1>"

@end_bp.route("/api/v1/ressources/users")
def all_users(): 
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])