from wtforms import StringField, SubmitField,BooleanField,Form,PasswordField, validators
from wtforms.validators import DataRequired , Length,EqualTo,Email
from flask_wtf import FlaskForm


from puma_db.models import User

class LoginForm(FlaskForm):


    name = StringField("Name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        # print(User.objects.filter(name=self.name.data).first())
        user= User.objects.filter(name=self.name.data).first()
        if user and user.password == self.password.data:
            return True
        return False
