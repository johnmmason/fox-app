from flask import Flask, render_template, request, url_for, flash, redirect
from sqlalchemy import Column, Integer, String, create_engine, desc
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.types import DateTime
from datetime import datetime
import os, hamdb

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24).hex()
Base = declarative_base()

engine = create_engine('sqlite:///foxhunt.db')
Session = sessionmaker(bind = engine)
session = Session()

class HamOperator(Base):
    __tablename__ = 'operators'

    id = Column(Integer, primary_key=True, index=True)
    callsign = Column(String)
    name = Column(String)
    date = Column(DateTime)

Base.metadata.create_all(engine)

def check_log(callsign):
    query = session.query(HamOperator.callsign).all()

    for row in query:
        if row[0] == callsign:
            return True
        else:
            return False
    
@app.route('/')
def index():
    operators = session.query(HamOperator).order_by(desc(HamOperator.date)).all()
    return render_template('table.html', title='N5XU Fox', operators=operators)

@app.route('/log', methods=('GET', 'POST'))
def log():
    if request.method == 'POST':

        callsign = request.form['callsign'].upper()
        
        if not callsign:
            flash('Callsign is required!')
        else:
            operator = hamdb.get(callsign)

            if not operator:
                flash('A valid amateur radio callsign is required.')
            else:
                name = operator['hamdb']['callsign']['fname']

                if check_log(callsign):
                    flash('You have already checked in!')
                else:
                
                    checkin = HamOperator(callsign=callsign, name=name, date=datetime.now())

                    session.add(checkin)
                    session.commit()

                    return redirect(url_for('index'))
        
    return render_template('form.html', title='N5XU Fox')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
