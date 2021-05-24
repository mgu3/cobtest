# Generated by Django 2.2.13 on 2020-06-09 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rbac", "0016_rbacadmingroup_rbacadmingrouprole_rbacadminusergroup"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rbacadmingrouprole",
            name="group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="rbac.RBACAdminGroup"
            ),
        ),
        migrations.AlterField(
            model_name="rbacadminusergroup",
            name="group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="rbac.RBACAdminGroup"
            ),
        ),
    ]