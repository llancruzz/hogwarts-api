from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to my Hogwarts AP Project!",
        "documentation": "https://github.com/llancruzz/hogwarts-api"
    })
