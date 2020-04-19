def index(request, question_id):
    return HttpResponse("Please go to <a href="/">admin page</a>" % question_id)
