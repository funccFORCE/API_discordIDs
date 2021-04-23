from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import redirect
import requests

auth_url_discord = "https://discord.com/api/oauth2/authorize?client_id=830151173846990878&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Foauth2%2Flogin%2Fredirect&response_type=code&scope=identify"


def home(request:HttpRequest) ->JsonResponse:
    return JsonResponse({"msg": "hello"})


def discord_login(request: HttpRequest):
    return redirect(auth_url_discord)


def login_redirect(request: HttpRequest):
    code = request.GET.get("code")
    print(code)
    user = exchange_code(code)
    return JsonResponse({"user": user})


def exchange_code(code: str):
    data = {
        "client_id": "830151173846990878",
        "client_secret": "Ta-WvuHzzkXOY_g7L-peIH0X-CmihpC4",
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://localhost:8000/oauth2/login/redirect",
        "scope": "identify"
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post("https://discord.com/api/oauth2/token", data=data, headers=headers)
    print(response)
    credentials = response.json()
    access_token = "******"
    response = requests.get("https://discord.com/api/v6/users/@me", headers={
        'Authorization': 'Bearer %s' % access_token
    })
    print(response)
    user = response.json()
    print(user)
    return user






