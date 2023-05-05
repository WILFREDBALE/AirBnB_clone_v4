@app.route('/0-hbnb/')
def hbnb():
    cache_id = uuid.uuid4()
    return render_template('0-hbnb.html', cache_id=cache_id)
