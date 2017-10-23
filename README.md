# Book-Keeping-API - Django

Django A Book-Keeping API that allows users to keep track of their
bets. Includes a profile page that displays a graph representing profit/loss
of selected sports categories. Allows users to add sports categories, report bets, and personalize their profile page.
Third party account verification leveraging Django-Allauth. 

## Getting Started
Clone or download the repository
Install Django version 1.11

### Installing

Open the folder in a terminal window

```
cd backend
cd src 
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser (provide user information)
python manage.py runserver
```


## Built With

* [Django](https://www.djangoproject.com/) - The back-end web framework used
* [Chart.js](http://www.chartjs.org/docs/latest/) - Library used to generate charts 
* [Bootstrap](http://getbootstrap.com/docs/4.0/getting-started/introduction/) - Framework for creating responsive layouts


## Authors

* **Sam Lee** - *Personal project* - [Sammyuel](https://github.com/Sammyuel)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
