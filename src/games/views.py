from django.shortcuts import render

#home view
def home(request):
    context =  {"active" : "home"} #dictionary that contains data you want to pass from your view to your template
    return render(request, "home.html", context)


#about view
def about(request):
    context = {"active" : "about"}
    return render(request, "about.html", context)
