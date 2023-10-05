from flask import Flask, abort, flash, render_template, request, jsonify


app = Flask(__name__)
app.config['SECRET_KEY'] = 'os.urandom(32)'  # Replace with your secret key



@app.route('/', strict_slashes=False)
@app.route('/login', strict_slashes=False)
def index():
    """The homepage of the application."""

    return render_template('login.html')

@app.route('/register', strict_slashes=False)
def register():
    """Render the Register page."""
    return render_template('login.html')

@app.route('/add_user', methods=['POST', 'GET'], strict_slashes=False)
def add_user():
    """Create a new instance of user."""
    

@app.route('/tasks', strict_slashes=False)
def tasks():
    """Render the Task page."""
    return render_template('tasks.html')


@app.route('/add_tasks', strict_slashes=False)
def add_task():
  """ Render the task page for Adding a new obj insance"""
  return render_template('tasks.html')


# @app.route('/create_task', methods=['POST'], strict_slashes=False)
# def create_task():
#   """Get the properties of this new obj instance of task create this obj via API"""



@app.route('/edit_task/<task_id>', strict_slashes=False)
def edit_task(task_id):
  """Render the edit page with necessary information to Edit a task."""
  return render_template('edit_task.html')



@app.route('/update_task/<task_id>', methods=['POST'], strict_slashes=False)
def update_task(task_id):
  """Edit a task and send this update to the database using API."""
  return render_template('tasks.html')
 

  
@app.route('/delete_task/<task_id>', methods=['GET'], strict_slashes=False)
def delete_task(task_id):
  """Delete a task."""
  return render_template('tasks.html')



if __name__ == '__main__':
    app.run(debug=True)