from wtforms import StringField, SubmitField,BooleanField,Form,PasswordField, validators
from wtforms.validators import DataRequired , Length,EqualTo,Email
from flask_wtf import FlaskForm


from puma_db.models import User



class RegisterForm(FlaskForm):
    """Register form."""
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=3, max=25)]
    )
    last_name = StringField(
        "Lastname", validators=[DataRequired(), Length(min=3, max=25)]
    )


    email = StringField(
        "Email", validators=[DataRequired(), Email(), Length(min=6, max=40)]
    )

    cell = StringField(
        "Cell", validators=[DataRequired(), Length(min=6, max=40)]
    )


    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6, max=40)]
    )

    confirm = PasswordField(
        "Verify password",
        [DataRequired(), EqualTo('Password', message="Passwords must match")],
    )

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.user = None


    def validate(self):
        """Validate the form."""
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        user = User.objects(username=self.username.data)
        if user:
            self.username.errors.append("Username already registered")
            return False
        user = User.objects(email=self.email.data)
        if user:
            self.email.errors.append("Email already registered")
            return False
        user = User.objects(cell=self.cell.data)
        if user:
            self.email.errors.append("Cell already registered")
            return False


        return True




