from django.shortcuts import render, redirect
from wall_app.models import *
# Create your views here.
def home(request): 
#user's wall homepage with their messages and comments
    logged_user= User.objects.get(id=request.session['user'])
    context = {
        "users_info": User.objects.get(id=request.session['user']),
        "all_messages": Message.objects.all(),
        "all_comments": logged_user.user_comment.all(),
        "users_messages": logged_user.user_message.all(),
    }
    return render(request,'wall/index.html', context)

def flush(request):
#logs the user off from their wall page
    request.session.flush()
    return redirect('/')

def message(request):
#user writes a message to post to the wall
    if request.method == "POST":
        logged_user = User.objects.get(id=request.session['user'])
        written_message = Message.objects.create(
            message = request.POST['message'],
            poster = logged_user
        )
        print(written_message)
    return redirect('/wall/home')

def comment(request, message_id): 
#user writes a comment to post to a message on the wall
    if request.method == "POST":
        logged_user = User.objects.get(id=request.session['user'])
        Comment.objects.create(
            comment = request.POST['comment'],
            commentor = logged_user,
            message = Message.objects.get(id=message_id),
        )
    return redirect('/wall/home')

def delete(request, message_id): 
#user deletes a message that they wrote
    if request.method == "POST":
        message_to_delete = Message.objects.get(id=message_id)
        logged_user = User.objects.get(id=request.session['user'])
        if message_to_delete.poster.id == request.session['user']:
        #if message_to_delete.poster == logged_user: 
            message_to_delete.delete()
    return redirect('/wall/home')
