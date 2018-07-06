# DRF Add Ons

**Feedbank APP for Django REST Framework with API Views.**<br>

`DRF Feedback` is a Django App that can for collecting feedback from end user. It's view are based upon
`Django REST Framework's GenericAPIView` and hence it contains a RESTful API views also.


I'll like to mention following names for certain contributions:

- **[Civil Machines Technologies Private Limited](https://github.com/civilmahines)**: For providing me platform and
funds for research work. This project is hosted currently with `CMT` only.
- [Himanshu Shankar](https://github.com/iamhssingh): For guiding me and providing me mentorship while doing this
project.

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
