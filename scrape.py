emails = [
"adrian.sardinata@elu.nl",
"alexey.markov@elu.nl",
"alisa.kalnina@elu.nl",
"aya.alabrash@elu.nl",
"chris.dallat@elu.nl",
"christopher.clayton@elu.nl",
"daniel.egbei@elu.nl",
"schmidt.dennis@elu.nl",
"emilia.rodriguez@elu.nl",
"Erika.Parra@elu.nl",
"firat.demir@elu.nl",
"garry.fokke@elu.nl",
"george.vilnoiu@elu.nl",
"giovanni.dipietro@elu.nl",
"hussein.bakir@elu.nl",
"ilias.markelis@elu.nl",
"jean.louis@elu.nl",
"joao.santos@elu.nl",
"johannes.wubs@elu.nl",
"jose.guevara@elu.nl",
"jozsef.dudas@elu.nl",
"juan.garcia@elu.nl",
"juan.perafan@elu.nl",
"khalil.masree@elu.nl",
"laeticia.blanc@elu.nl",
"leon.aziz@elu.nl",
"leticia.mejia@elu.nl",
"lorenzo.cunial@elu.nl",
"malik.petion@elu.nl",
"marcel.ghisi@elu.nl",
"michael.mullins@elu.nl",
"Milana.Logunova@elu.nl",
"moisieiev.mykyta@elu.nl",
"Neline.Theron@elu.nl",
"oben.kingsly@elu.nl",
"Patryk.Sieradzki@elu.nl",
"pedro.botsaris@elu.nl",
"petar.angelov@elu.nl",
"rhys.christopher@elu.nl",
"rufeena.sovis@elu.nl",
"sahan.caliskan@elu.nl",
"sateh.almalazi@elu.nl",
"selcuk.aksoy@elu.nl",
"sergei.serdechny@elu.nl",
"shane.murtagh@elu.nl",
"siham.ahmed@elu.nl",
"sima.milli@elu.nl",
"soraia.lima@elu.nl",
"stanislav.kashchenko@elu.nl",
"stijn.kat@elu.nl",
"viktor.rodau@elu.nl",
"yana.kondratyuk@elu.nl",
"yaroslav.pakhaliuk@elu.nl",
"ivan.yuri@elu.nl"]

import json
import requests
import os
import pandas as pd 
token = 'xoxb-50977910727-4725064420483-q4OoVSJibclKMgBiEpjkkpCJ'

url = "https://slack.com/api/auth.test"

headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json;charset=utf-8"
}


def word_in_string(s, word_list):
    for word in word_list:
        if word in s:
            return True
    return False


def get_members(token):
    response = requests.get("https://slack.com/api/users.list", headers=headers)
    #print(response.json()["members"])
    #print(json.dumps(response.json()["members"], indent=4))
    # for member in response.json()["members"]:
    #         if 'email' in member['profile'] and member['profile']['email'] in emails:
    #             print(member['profile']['real_name'])
    return response.json()["members"]


def get_last_active(member_id, token):
    response = requests.get("https://slack.com/api/users.getPresence", headers=headers)
    last_active = response.json()["presence"]
    return last_active

members = get_members(token)
# res = requests.post("https://slack.com/api/auth.test", json={"token": SLACK_API_TOKEN})
# print(res, res.json())

for member in members:
    if 'email' in member['profile'] and member['profile']['email'] in emails:
        print("User:", member["name"], "Last active:", get_last_active(member["id"], token))