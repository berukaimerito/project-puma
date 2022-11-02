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



        print(self.name)
        print(self.password)


        user = User.objects(name=self.name)
        print(user)



        # if self.user.na:
        #     return True

        return True
