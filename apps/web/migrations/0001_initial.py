# Generated by Django 2.0 on 2017-12-29 08:28

import uuid

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import apps.web.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('device_uid', models.CharField(blank=True, max_length=255, null=True, verbose_name="Telegram user's id")),
                ('is_bot', models.BooleanField(default=False, verbose_name='User is a bot')),
                ('language_code', models.CharField(blank=True, help_text='Language code from user messages got for the first time', max_length=10, null=True, verbose_name='Language code')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Entity created at', null=True, verbose_name='Created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Entity created at', null=True, verbose_name='Updated at')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=1000, unique=True, validators=[apps.web.validators.token_validator], verbose_name='Bot token')),
                ('name', models.CharField(max_length=250, verbose_name='Bot name')),
                ('enabled', models.BooleanField(default=True, help_text='Define if bot is enabled. Active by default', verbose_name='Bot enabled')),
                ('owner', models.ForeignKey(blank=True, help_text='User that owns this bot', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='telegram_bots', to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
                ('user_api', models.OneToOneField(blank=True, help_text='API user. Automatically retrieved from Telegram', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='telegram_bot', to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
            options={
                'verbose_name': 'Bot',
                'verbose_name_plural': 'Bots',
            },
        ),
        migrations.CreateModel(
            name='CallbackQuery',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Entity created at', null=True, verbose_name='Created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Entity created at', null=True, verbose_name='Updated at')),
                ('id', models.BigIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Callback id')),
                ('data', models.TextField(help_text='Data associated with the callback button.', max_length=1000, verbose_name='Callback data')),
                ('from_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='callback_queries', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Callback query',
                'verbose_name_plural': 'Callback queries',
            },
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Entity created at', null=True, verbose_name='Created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Entity created at', null=True, verbose_name='Updated at')),
                ('id', models.BigIntegerField(help_text='Unique identifier for this chat.', primary_key=True, serialize=False, unique=True)),
                ('type', models.CharField(choices=[('private', 'Private'), ('group', 'Group'), ('supergroup', 'Supergroup'), ('channel', 'Channel')], max_length=255, verbose_name='Type')),
                ('title', models.CharField(blank=True, help_text='Title, for supergroups, channels and group chats.', max_length=255, null=True, verbose_name='title')),
                ('username', models.CharField(blank=True, max_length=255, null=True, verbose_name='Unique username')),
                ('first_name', models.CharField(blank=True, help_text='First name of the other party in a private chat', max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, help_text='Last name of the other party in a private chat', max_length=255, null=True)),
                ('default_keyboard', models.TextField(blank=True, help_text='Chat menu, is used to inherit markup keyboard styles', max_length=1000, null=True, verbose_name='Chat menu')),
                ('current_keyboard', models.TextField(blank=True, editable=False, help_text='Is used to define available command from keyboard', max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'Chat',
                'verbose_name_plural': 'Chats',
            },
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Entity created at', null=True, verbose_name='Created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Entity created at', null=True, verbose_name='Updated at')),
                ('value', models.CharField(max_length=1000, verbose_name='Answer or pattern')),
                ('rule', models.CharField(choices=[('full_coincidence', 'Full coincidence'), ('to_be_in', 'To be in'), ('contains', 'Contains'), ('starts_with', 'Starts with'), ('ends_with', 'Ends with'), ('match_regex', 'Match regex'), ('contain_an_image', 'Contain an image'), ('contain_a_file', 'Contain a file'), ('contain_an_audio', 'Contain a audio'), ('contain_a_video', 'Contain a video'), ('received_before', 'Received before'), ('received_after', 'Received after')], default='full_coincidence', max_length=255, verbose_name='Pattern')),
                ('matched_field', models.CharField(choices=[('any_message', 'Any message'), ('message_text', 'Message text'), ('callback_message_text', 'Callback message text'), ('callback data', 'Callback command')], default='any_message', max_length=255, verbose_name='Matched field')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Entity created at', null=True, verbose_name='Created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Entity created at', null=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=255, verbose_name='Event name')),
                ('send_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Time to send on')),
                ('status', models.CharField(choices=[('not_started', 'Not started'), ('pending', 'Pending'), ('succeeded', 'Succeeded'), ('failed', 'Failed')], default='not_started', max_length=20)),
                ('bot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Bot')),
                ('chat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Chat')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Handler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Entity created at', null=True, verbose_name='Created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Entity created at', null=True, verbose_name='Updated at')),
                ('enabled_on', models.CharField(choices=[('reply_button', 'Reply button'), ('message', 'Message'), ('command', 'Command'), ('callback', 'Callback')], default='reply_button', help_text='Enabled only on following requests', max_length=255, verbose_name='Enabled on')),
                ('ids_expression', models.CharField(blank=True, help_text="Allowed / +*()! /. A set of rules by condition's id", max_length=500, null=True, validators=[apps.web.validators.condition_validator], verbose_name='Mathematics expression')),
                ('title', models.CharField(max_length=255, verbose_name='Handler title')),
                ('allowed', models.ManyToManyField(blank=True, related_name='handlers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Handler',
                'verbose_name_plural': 'Handlers',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Entity created at', null=True, verbose_name='Created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Entity created at', null=True, verbose_name='Updated at')),
                ('message_id', models.BigIntegerField(db_index=True, help_text='Telegram message id retrieved from API', verbose_name='Message id')),
                ('date', models.DateTimeField(help_text='Date the message was sent', verbose_name='Date')),
                ('text', models.TextField(blank=True, max_length=2500, null=True, verbose_name='Message text')),
                ('chat', models.ForeignKey(blank=True, help_text='Retrieved from Telegram API chat id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='web.Chat', verbose_name='Chat id')),
                ('forward_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forwarded_messages', to=settings.AUTH_USER_MODEL, verbose_name='Sender of the original message')),
                ('from_user', models.ForeignKey(help_text='Retrieved user from', on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL, verbose_name='From User')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Entity created at', null=True, verbose_name='Created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Entity created at', null=True, verbose_name='Updated at')),
                ('file_id', models.CharField(db_index=True, help_text='Unique identifier for this file.', max_length=1000, verbose_name='File ID')),
                ('width', models.IntegerField(verbose_name='Image width')),
                ('height', models.IntegerField(verbose_name='Image height')),
                ('file_size', models.IntegerField(verbose_name='File size')),
                ('message', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='web.Message', verbose_name='From message')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Entity created at', null=True, verbose_name='Created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Entity created at', null=True, verbose_name='Updated at')),
                ('title', models.CharField(max_length=255, verbose_name='Quest name')),
                ('description', models.TextField(max_length=1000, verbose_name='Quest description')),
                ('bot', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quest', to='web.Bot', verbose_name='Connected bot')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Entity created at', null=True, verbose_name='Created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Entity created at', null=True, verbose_name='Updated at')),
                ('title', models.CharField(max_length=1000, verbose_name='Response title')),
                ('on_true', models.BooleanField(default=True, verbose_name='Triggering on true')),
                ('as_reply', models.BooleanField(default=False, verbose_name='Send as reply')),
                ('inherit_keyboard', models.BooleanField(default=True, verbose_name='Display last used keyboard')),
                ('set_default_keyboard', models.BooleanField(default=False, verbose_name='Save this keyboard as default for chat')),
                ('delete_previous_keyboard', models.BooleanField(default=False, verbose_name='Delete previous keyboard')),
                ('one_time_keyboard', models.BooleanField(default=False, verbose_name='Hide keyboard after click on')),
                ('text', models.TextField(blank=True, max_length=5000, null=True, validators=[apps.web.validators.jinja2_template_validator], verbose_name='Message text')),
                ('keyboard', models.TextField(blank=True, max_length=2000, null=True, validators=[apps.web.validators.jinja2_template_validator], verbose_name='Keyboard layout')),
                ('redirect_to', models.CharField(blank=True, help_text='List of usernames separated by whitespace', max_length=1000, validators=[apps.web.validators.username_list_validator], verbose_name='Redirect to')),
                ('priority', models.SmallIntegerField(default=1, verbose_name='Priority in the queue')),
                ('handler', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='web.Handler', verbose_name='Attached handler to')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Entity created at', null=True, verbose_name='Created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Entity created at', null=True, verbose_name='Updated at')),
                ('is_initial', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255, verbose_name='Step title')),
                ('number', models.SmallIntegerField(verbose_name='Step Number')),
                ('quest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='web.Quest')),
            ],
            options={
                'ordering': ('number', 'title'),
            },
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Entity created at', null=True, verbose_name='Created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Entity created at', null=True, verbose_name='Updated at')),
                ('update_id', models.BigIntegerField(db_index=True, verbose_name='Update Id')),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Bot', verbose_name='Bot from')),
                ('callback_query', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updates', to='web.CallbackQuery', verbose_name='Callback Query')),
                ('handler', models.ForeignKey(blank=True, help_text='Handler contains expression needed to process a message', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updates', to='web.Handler', verbose_name='Handler')),
                ('message', models.ForeignKey(blank=True, help_text='Update action for particular massage', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updates', to='web.Message', verbose_name='Message ID')),
                ('response', models.ForeignKey(blank=True, help_text='Response that contain this message', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updates', to='web.Response', verbose_name='Response')),
            ],
            options={
                'verbose_name': 'Update',
                'verbose_name_plural': 'Updates',
            },
        ),
        migrations.AddField(
            model_name='handler',
            name='step',
            field=models.ForeignKey(help_text='Handle particular actions for this step', on_delete=django.db.models.deletion.CASCADE, related_name='handlers', to='web.Step'),
        ),
        migrations.AddField(
            model_name='handler',
            name='step_on_error',
            field=models.ForeignKey(blank=True, help_text='Move to this step if mathematics expression wrongful', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='false_handlers', to='web.Step', verbose_name='Step on error'),
        ),
        migrations.AddField(
            model_name='handler',
            name='step_on_success',
            field=models.ForeignKey(blank=True, help_text='Move to this step if mathematics expression truthful', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='true_handlers', to='web.Step', verbose_name='Step on success'),
        ),
        migrations.AddField(
            model_name='event',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Message', verbose_name='Reply to message'),
        ),
        migrations.AddField(
            model_name='event',
            name='move_user_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.Step', verbose_name='Mover user to step'),
        ),
        migrations.AddField(
            model_name='event',
            name='response',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Response', verbose_name='Responses with data'),
        ),
        migrations.AddField(
            model_name='condition',
            name='handler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conditions', to='web.Handler', verbose_name='Attached to handler'),
        ),
        migrations.AddField(
            model_name='callbackquery',
            name='message',
            field=models.ForeignKey(help_text='Message with the callback button that originated the query.', on_delete=django.db.models.deletion.CASCADE, related_name='callback_queries', to='web.Message', verbose_name='Message ID'),
        ),
        migrations.AddField(
            model_name='appuser',
            name='step',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='web.Step', verbose_name="User's level"),
        ),
        migrations.AddField(
            model_name='appuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
