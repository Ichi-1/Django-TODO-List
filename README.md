# Demo: https://fast-ocean-38849.herokuapp.com/


## I used in this project:
- Django Framework
- Class-based-view
- Linter: Flake8


### Class-based-view (CBS)
Its simply Django View written in OOP-style, its take request and return response as usually. 
As example, instead of @login_required CBV using LoginRequiredMixin. 
CRUD requests support by particular class-based-view: CreateView, DeleteView, UpdateView


Example straight from django docs. Code to handle HTTP GET in a view function would look something like:

```
from django.http import HttpResponse

def my_view(request):
    if request.method == 'GET':
        # <view logic>
        return HttpResponse('result')
```

In a class-based view, this would become:

```
from django.http import HttpResponse
from django.views import View

class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')
```
