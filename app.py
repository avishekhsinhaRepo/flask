from flask import Flask, render_template,request
from infopkg.info_form import InfoForm
app = Flask(__name__)


app.config['SECRET_KEY'] = 'your-secret-key'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    print("Register")
    breed = False
    form = InfoForm()
    if form.validate_on_submit():
        breed = form.breed.data
        print("breed", breed)
        form.breed.data = ''
    return render_template('register.html', form=form, breed=breed)


@app.route('/thankyou')
def thankyou():
    user_name = request.args.get('user_name')
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    full_name = first_name+ " " + last_name
    return render_template('thankyou.html', full_name=full_name, validation_errors=validate_user(user_name))

def validate_user(user_name):
    validation_errors =[]
    if not user_name[-1].isdigit():
        validation_errors.append("Username should end with number")
    if not any(char.isupper() for char in user_name):
        validation_errors.append("Username should a contain uppercase letters")
    if not any(char.islower() for char in user_name):
        validation_errors.append("Username should a contain lowercase letters")
    return validation_errors


if __name__ == '__main__':
    app.run(debug=True)

