from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from django.shortcuts import redirect

auth_url_discord="https://discord.com/api/oauth2/authorize?client_id=830151173846990878&permissions=0&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Foauth2%2Flogin&response_type=code&scope=identify%20connections%20email%20guilds.join%20guilds%20gdm.join%20rpc%20rpc.notifications.read%20rpc.voice.read%20rpc.voice.write%20rpc.activities.write%20bot%20webhook.incoming%20messages.read%20applications.builds.upload%20applications.builds.read%20applications.commands%20applications.store.update%20applications.entitlements%20activities.read%20activities.write%20relationships.read"
def home(request):
    return HttpResponse("Hello")
def login(request):
    return redirect(auth_url_discord)
