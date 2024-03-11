from wtforms import Form, StringField, validators, IntegerField

class Create_task(Form):
    task_name = StringField('Name', [validators.Length(min=4, max=120)])
    task_priority = StringField('Priority', [validators.Length(min=0, max=25)])
    task_description = StringField('Description', [validators.Length(min=0, max=255)])

class Delete_task(Form):
    task_name = StringField('Name', [validators.Length(min=4, max=120)])
    confirm_task_name = StringField('Confirm Name', [validators.Length(min=4, max=120)])

    def validate_confirm_task_name(form, field):
        if form.task_name.data != field.data:
            raise validators.ValidationError('Task names do not match.')

class Edit_task(Form):
    current_name = StringField('Current Name', [validators.Length(min=4, max=120)])
    new_name = StringField('New Name', [validators.Length(min=4, max=120)])
    task_priority = StringField('Priority', [validators.Length(min=0, max=25)])
    task_description = StringField('Description', [validators.Length(min=0, max=255)])
