# Django REST Framework - Feedback

**Feedback App for Django REST Framework with API Views.**<br>

`DRF Feedback` is a Django App that can for collecting feedback from end user. It's view are based upon
`Django REST Framework's GenericAPIView` and hence it contains a RESTful API views also.


#### Contributors: 
- **[Civil Machines Technologies Private Limited](https://github.com/civilmahines)**: For providing platform and funds
for research work. This project is hosted currently with `CMT` only. 
- [Himanshu Shankar](https://github.com/iamhssingh): Ideation, modification & Quality Assurance in the app.
- [Mahen Gandhi](https://github.com/imlegend19): Developed this app from scratch. 
- [Aditya Gupta](https://github.com/ag93999): Testing, Modification suggestions & intial works. This app is inspire 
his work in live project of [Hisab Kitab](https://hisabkitab.in) 

#### Installation

- Download and Install via `pip`
```
pip install drf_feedback
```
or<br>
Download and Install via `easy_install`
```
easy_install drf_feedback
```
- Add `drf_feedback` in `INSTALLED_APPS`<br>
```
INSTALLED_APPS = [
    ...
    'drf_feedback',
    ...
]
```
- Include urls of `drf_feedback` in `urls.py`
```
urlpatterns = [
    ...
    path('feedback/', include('feedback.urls')),
    ...
]

# or

urlpatterns = [
    ...
    url(r'feedback/', include('feedback.urls')),
    ...
]
```

- Finally, run `migrate` command
```
python manage.py migrate drf_feedback
```
