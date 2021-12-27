from django.urls import path

from measurement.views import SensorsView, TemperatureView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    # Ссылаемся на функцию класса с помощью as_view()
    path('show_temperature/', TemperatureView.as_view()),
    path('show_sensors/', SensorsView.as_view()),
    path('show_sensors/<pk>/', SensorsView.as_view()),
]
