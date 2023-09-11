# blog_posts/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField,FileAllowed


class BlogPostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    text = TextAreaField('Text',validators=[DataRequired()])
    blog_image = FileField('Select featured image',validators=[FileAllowed(['jpg','png'])])

    submit = SubmitField("Post")
