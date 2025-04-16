from rest_framework.response import Response
import rest_framework

# Create your views here.
def incoming_messages(request):
    if request.method == 'POST':
        data = request.get_json(force=True)
        print(f"Incoming message....\n${data}")
        return Response(data=data, status=200)