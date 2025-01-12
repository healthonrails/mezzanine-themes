# mezzanine-themes

### Free themes for Mezzanine CMS.



This is a mezzanine project which contains free mezzanine themes(flat/nova/solid/moderna).

Download and run the project to try each theme by changing theme name in settings.py

For example:

```
INSTALLED_APPS = (
    # "moderna",
    # "flat",
    # "nova",
    "solid",
    "django.contrib.admin",
    "django.contrib.auth",
    ...
)
```

```sh
python manage.py makemigrations flat

python manage.py migrate
```

Preview:
- Moderna:
![Moderna](https://cloud.githubusercontent.com/assets/1374633/21468864/5d6c20de-ca34-11e6-8eb3-68094c512155.png)

- Flat:
![Flat](./main/flat/static/images/new_flat_screen_shot.PNG)

- Nova:
![Nova](https://cloud.githubusercontent.com/assets/1374633/21468877/f6077eec-ca34-11e6-9f13-10dee46d1618.png)

- Solid:
![Solid](https://cloud.githubusercontent.com/assets/1374633/21468881/1d29edd4-ca35-11e6-9638-25c6b30a61a5.png)
