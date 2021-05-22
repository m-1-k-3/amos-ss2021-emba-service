# Generated by Django 3.2.2 on 2021-05-19 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Firmware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True)),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('url', models.TextField(blank=True)),
                ('version', models.TextField(help_text='Firmware version (double quote your input)')),
                ('vendor', models.TextField(help_text='Firmware vendor (double quote your input)')),
                ('device', models.TextField(help_text='Device (double quote your input)')),
                ('notes', models.TextField(help_text='Testing notes (double quote your input)')),
                ('firmware_Architecture', models.TextField(help_text='Architecture of the linux firmware [MIPS, ARM, x86, x64, PPC], -a will be added')),
                ('cwe_checker', models.BooleanField(default=False, help_text='Enables cwe-checker,-c will be added')),
                ('docker_container', models.BooleanField(default=False, help_text='Run emba in docker container, -D will be added')),
                ('deep_extraction', models.BooleanField(default=False, help_text='Enable deep extraction, -x will be added')),
                ('log_path', models.BooleanField(default=False, help_text='Ignores log path check, -i will be added')),
                ('grep_able_log', models.BooleanField(default=False, help_text='Create grep-able log file in [log_path]/fw_grep.log, -g will be added')),
                ('relative_paths', models.BooleanField(default=False, help_text='Prints only relative paths, -s will be added')),
                ('ANSI_color', models.BooleanField(default=False, help_text='Adds ANSI color codes to log, -z will be added')),
                ('web_reporter', models.BooleanField(default=False, help_text='Activates web report creation in log path, -W will be added')),
                ('emulation_test', models.BooleanField(default=False, help_text='Enables automated qemu emulation tests, -E will be added')),
            ],
        ),
    ]
