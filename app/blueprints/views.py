from flask import (Blueprint,
                   current_app,
                   request,
                   redirect,
                   flash,
                   url_for,
                   render_template)

# from flask_login import login_required, login_user, logout_user

blueprint = Blueprint('app_home_blueprint', __name__, template_folder='templates')



@blueprint.route('/')
# @login_required
def home():
    return current_app.send_static_file('dist/index.html')

#
# @blueprint.route('/login', methods=['GET', 'POST'])
# def login():
#     # Here we use a class of some kind to represent and validate our
#     # client-side form data. For example, WTForms is a library that will
#     # handle this for us, and we use a custom LoginForm to validate.
#     from app.blueprints.forms import LoginForm
#     from app.blueprints.user.models import UserModel
#     from app.lib.safe_next_url import safe_next_url
#     form = LoginForm(next=request.args.get('next'))
#
#
#     if form.validate_on_submit():
#         u = UserModel.find_by_username(request.form.get('identity'))
#
#         if u and u.authenticated(password=request.form.get('password')):
#             login_user(u)
#             # Handle optionally redirecting to the next URL safely.
#             next_url = request.form.get('next')
#             if next_url:
#                 return redirect(safe_next_url(next_url))
#
#             return redirect('/')
#         else:
#             flash('Username or Password is incorrect.', 'error')
#     return render_template('login_contextia.html', form=form)
#
#
# @blueprint.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash('You have been logged out.', 'success')
#     return redirect(url_for('app_home_blueprint.login'))