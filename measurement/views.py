# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from pickle import GET

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Temp_sensor, Temp_measure
from measurement.serializer import Temp_sensorSerializer, Temp_measureSerializer


class TemperatureView(APIView):
    """
    http://127.0.0.1:8000/api/show_temperature/
    Чтобы избежать ветвления с использованием if используем класс APIView
    """
    def get(self, request):
        print('id:', request.get(id))
        temperatures = Temp_measure.objects.all()
        temper = Temp_measureSerializer(temperatures, many=True)
        return Response(temper.data)

    def post(self, request):
        temp = Temp_measureSerializer(data=request.data)
        print(temp.is_valid())
        if temp.is_valid():  # если запрос действительный
            if request.data.get('id'):  # если id присутсвует в запросе от пользователя, значит это редактирование
                ids = request.data.get(id)
                print('ids', ids)
                temp.save(id=ids)
            else:  # если id нет, значит завписываем новый датчик.
                temp.save()
                print('записываю ', temp)
        print('temp:', temp)
        return Response({'status': 'OK'})


class SensorsView(APIView):
    """
    http://127.0.0.1:8000/api/show_sensors/
    get - получение из БД через сериалайзер данных и вывод в браузер пользователю
    post - отправка пользователем данных о новых датчиках и редактирование существующих
    """
    def get(self, request):
        temp_sensors = Temp_sensor.objects.all()
        sens = Temp_sensorSerializer(temp_sensors, many=True)
        print('sens: ', sens)
        return Response(sens.data)

    def post(self, request):
        sens = Temp_sensorSerializer(data=request.data)
        if sens.is_valid():  # если запрос действительный
            if request.data.get('id'):  # если id присутсвует в запросе от пользователя, значит это редактирование
                ids = request.data.get(id)
                print('ids', ids)
                sens.save(id=ids)
            else:  # если id нет, значит записываем новый датчик.
                sens.save()
        print('sens:', sens)

        return Response({'status': 'OK'})
