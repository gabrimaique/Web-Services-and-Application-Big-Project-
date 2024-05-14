from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:gabriel%40123@localhost/pubs_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Pub(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(300), nullable=True)
    year_opened = db.Column(db.Integer, nullable=True)
    budget = db.Column(db.Float, nullable=True)
    serve_food = db.Column(db.Boolean, default=False)
    google_review = db.Column(db.Float, nullable=True)
    live_music = db.Column(db.Boolean, default=False)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/pubs', methods=['GET', 'POST'])
def handle_pubs():
    if request.method == 'POST':
        data = request.get_json()
        new_pub = Pub(
            name=data['name'],
            address=data['address'],
            year_opened=data.get('year_opened'),
            budget=data.get('budget'),
            serve_food=data.get('serve_food', False),
            google_review=data.get('google_review'),
            live_music=data.get('live_music', False)
        )
        db.session.add(new_pub)
        db.session.commit()
        return jsonify({'message': 'Pub added!', 'pub': {
            'id': new_pub.id, 'name': new_pub.name, 'address': new_pub.address,
            'year_opened': new_pub.year_opened, 'budget': new_pub.budget,
            'serve_food': new_pub.serve_food, 'google_review': new_pub.google_review,
            'live_music': new_pub.live_music
        }}), 201
    elif request.method == 'GET':
        pubs = Pub.query.all()
        return jsonify([{
            'id': pub.id,
            'name': pub.name,
            'address': pub.address,
            'year_opened': pub.year_opened,
            'budget': pub.budget,
            'serve_food': pub.serve_food,
            'google_review': pub.google_review,
            'live_music': pub.live_music
        } for pub in pubs])

@app.route('/api/pubs/<int:pub_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_pub(pub_id):
    pub = Pub.query.get_or_404(pub_id)
    if request.method == 'GET':
        return jsonify({
            'id': pub.id,
            'name': pub.name,
            'address': pub.address,
            'year_opened': pub.year_opened,
            'budget': pub.budget,
            'serve_food': pub.serve_food,
            'google_review': pub.google_review,
            'live_music': pub.live_music
        })
    elif request.method == 'PUT':
        data = request.get_json()
        pub.name = data.get('name', pub.name)
        pub.address = data.get('address', pub.address)
        pub.year_opened = data.get('year_opened', pub.year_opened)
        pub.budget = data.get('budget', pub.budget)
        pub.serve_food = data.get('serve_food', pub.serve_food)
        pub.google_review = data.get('google_review', pub.google_review)
        pub.live_music = data.get('live_music', pub.live_music)
        db.session.commit()
        return jsonify({'message': 'Pub updated!'})
    elif request.method == 'DELETE':
        db.session.delete(pub)
        db.session.commit()
        return jsonify({'message': 'Pub deleted!'})

if __name__ == '__main__':
    app.run(debug=True)
