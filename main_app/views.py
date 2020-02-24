
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Choice, Question, Phonebase, Article, Comments, Unique_set
from .forms import ChatForm
import nltk
nltk.download('punkt')

from nltk.stem.lancaster import LancasterStemmer

# Для загрузки файла

stemmer = LancasterStemmer()
import numpy
import tflearn
import random
import json
import pickle
import requests

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def calculator(request):
    return render(request, 'main_app/calculator.html')


def support(request):
    contact_list = Phonebase.objects.all()
    paginator = Paginator(contact_list, 2)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'main_app/support.html', {'contacts': contacts})


def Tank(request):
    contact_list = Tank.objects.all()
    paginator = Paginator(contact_list, 2)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'main_app/support.html', {'contacts': contacts})


def order(request):
    return render(request, 'main_app/order.html')


def unique(request):
    return render(request, 'main_app/unique.html')



"""CHAT"""


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)


MODEL = None

def get_model():
    global MODEL
    if MODEL is None:
        words, labels, training, output = get_hdata()
        net = tflearn.input_data(shape=[None, len(training[0])])
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
        net = tflearn.regression(net)

        MODEL = tflearn.DNN(net)
        MODEL.load("model.tflearn")
    return MODEL

DATAA = None
def get_data():
    global DATAA

    if DATAA is None:
        with open("intents.json") as file:
            DATAA = json.load(file)
    return DATAA


HDATA = None
def get_hdata():
    global HDATA

    if HDATA is None:
        with open("data.pickle", "rb") as f:
            HDATA = pickle.load(f)
    return HDATA


def chat(request):
    out = "You need help?"
    if "your_name" in request.POST:
        words, labels, training, output = get_hdata()
        results = get_model().predict([bag_of_words(request.POST["your_name"], words)])
        results_index = numpy.argmax(results)
        tag = labels[results_index]

        for tg in get_data()["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']
        out = random.choice(responses)

    return render(request, 'main_app/chat.html',context={'name':out})

"""CHAT  END"""
def all(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT')
        name_host = request.META.get('SERVER_PORT')
        method = request.META.get('REQUEST_METHOD')
        try:
            get_country = requests.get("https://ipinfo.io/%s?token=77a09218c42d10" % ip)
            c = (get_country.json())
            t = {"BD": "Bangladesh", "BE": "Belgium", "BF": "Burkina Faso", "BG": "Bulgaria",
                 "BA": "Bosnia and Herzegovina", "BB": "Barbados", "WF": "Wallis and Futuna", "BL": "Saint Barthelemy",
                 "BM": "Bermuda", "BN": "Brunei", "BO": "Bolivia", "BH": "Bahrain", "BI": "Burundi", "BJ": "Benin",
                 "BT": "Bhutan", "JM": "Jamaica", "BV": "Bouvet Island", "BW": "Botswana", "WS": "Samoa",
                 "BQ": "Bonaire, Saint Eustatius and Saba ", "BR": "Brazil", "BS": "Bahamas", "JE": "Jersey",
                 "BY": "Belarus", "BZ": "Belize", "RU": "Russia", "RW": "Rwanda", "RS": "Serbia", "TL": "East Timor",
                 "RE": "Reunion", "TM": "Turkmenistan", "TJ": "Tajikistan", "RO": "Romania", "TK": "Tokelau",
                 "GW": "Guinea-Bissau", "GU": "Guam", "GT": "Guatemala",
                 "GS": "South Georgia and the South Sandwich Islands", "GR": "Greece", "GQ": "Equatorial Guinea",
                 "GP": "Guadeloupe", "JP": "Japan", "GY": "Guyana", "GG": "Guernsey", "GF": "French Guiana",
                 "GE": "Georgia", "GD": "Grenada", "GB": "United Kingdom", "GA": "Gabon", "SV": "El Salvador",
                 "GN": "Guinea", "GM": "Gambia", "GL": "Greenland", "GI": "Gibraltar", "GH": "Ghana", "OM": "Oman",
                 "TN": "Tunisia", "JO": "Jordan", "HR": "Croatia", "HT": "Haiti", "HU": "Hungary", "HK": "Hong Kong",
                 "HN": "Honduras", "HM": "Heard Island and McDonald Islands", "VE": "Venezuela", "PR": "Puerto Rico",
                 "PS": "Palestinian Territory", "PW": "Palau", "PT": "Portugal", "SJ": "Svalbard and Jan Mayen",
                 "PY": "Paraguay", "IQ": "Iraq", "PA": "Panama", "PF": "French Polynesia", "PG": "Papua New Guinea",
                 "PE": "Peru", "PK": "Pakistan", "PH": "Philippines", "PN": "Pitcairn", "PL": "Poland",
                 "PM": "Saint Pierre and Miquelon", "ZM": "Zambia", "EH": "Western Sahara", "EE": "Estonia",
                 "EG": "Egypt", "ZA": "South Africa", "EC": "Ecuador", "IT": "Italy", "VN": "Vietnam",
                 "SB": "Solomon Islands", "ET": "Ethiopia", "SO": "Somalia", "ZW": "Zimbabwe", "SA": "Saudi Arabia",
                 "ES": "Spain", "ER": "Eritrea", "ME": "Montenegro", "MD": "Moldova", "MG": "Madagascar",
                 "MF": "Saint Martin", "MA": "Morocco", "MC": "Monaco", "UZ": "Uzbekistan", "MM": "Myanmar",
                 "ML": "Mali", "MO": "Macao", "MN": "Mongolia", "MH": "Marshall Islands", "MK": "Macedonia",
                 "MU": "Mauritius", "MT": "Malta", "MW": "Malawi", "MV": "Maldives", "MQ": "Martinique",
                 "MP": "Northern Mariana Islands", "MS": "Montserrat", "MR": "Mauritania", "IM": "Isle of Man",
                 "UG": "Uganda", "TZ": "Tanzania", "MY": "Malaysia", "MX": "Mexico", "IL": "Israel", "FR": "France",
                 "IO": "British Indian Ocean Territory", "SH": "Saint Helena", "FI": "Finland", "FJ": "Fiji",
                 "FK": "Falkland Islands", "FM": "Micronesia", "FO": "Faroe Islands", "NI": "Nicaragua",
                 "NL": "Netherlands", "NO": "Norway", "NA": "Namibia", "VU": "Vanuatu", "NC": "New Caledonia",
                 "NE": "Niger", "NF": "Norfolk Island", "NG": "Nigeria", "NZ": "New Zealand", "NP": "Nepal",
                 "NR": "Nauru", "NU": "Niue", "CK": "Cook Islands", "XK": "Kosovo", "CI": "Ivory Coast",
                 "CH": "Switzerland", "CO": "Colombia", "CN": "China", "CM": "Cameroon", "CL": "Chile",
                 "CC": "Cocos Islands", "CA": "Canada", "CG": "Republic of the Congo", "CF": "Central African Republic",
                 "CD": "Democratic Republic of the Congo", "CZ": "Czech Republic", "CY": "Cyprus",
                 "CX": "Christmas Island", "CR": "Costa Rica", "CW": "Curacao", "CV": "Cape Verde", "CU": "Cuba",
                 "SZ": "Swaziland", "SY": "Syria", "SX": "Sint Maarten", "KG": "Kyrgyzstan", "KE": "Kenya",
                 "SS": "South Sudan", "SR": "Suriname", "KI": "Kiribati", "KH": "Cambodia",
                 "KN": "Saint Kitts and Nevis", "KM": "Comoros", "ST": "Sao Tome and Principe", "SK": "Slovakia",
                 "KR": "South Korea", "SI": "Slovenia", "KP": "North Korea", "KW": "Kuwait", "SN": "Senegal",
                 "SM": "San Marino", "SL": "Sierra Leone", "SC": "Seychelles", "KZ": "Kazakhstan",
                 "KY": "Cayman Islands", "SG": "Singapore", "SE": "Sweden", "SD": "Sudan", "DO": "Dominican Republic",
                 "DM": "Dominica", "DJ": "Djibouti", "DK": "Denmark", "VG": "British Virgin Islands", "DE": "Germany",
                 "YE": "Yemen", "DZ": "Algeria", "US": "United States", "UY": "Uruguay", "YT": "Mayotte",
                 "UM": "United States Minor Outlying Islands", "LB": "Lebanon", "LC": "Saint Lucia", "LA": "Laos",
                 "TV": "Tuvalu", "TW": "Taiwan", "TT": "Trinidad and Tobago", "TR": "Turkey", "LK": "Sri Lanka",
                 "LI": "Liechtenstein", "LV": "Latvia", "TO": "Tonga", "LT": "Lithuania", "LU": "Luxembourg",
                 "LR": "Liberia", "LS": "Lesotho", "TH": "Thailand", "TF": "French Southern Territories", "TG": "Togo",
                 "TD": "Chad", "TC": "Turks and Caicos Islands", "LY": "Libya", "VA": "Vatican",
                 "VC": "Saint Vincent and the Grenadines", "AE": "United Arab Emirates", "AD": "Andorra",
                 "AG": "Antigua and Barbuda", "AF": "Afghanistan", "AI": "Anguilla", "VI": "U.S. Virgin Islands",
                 "IS": "Iceland", "IR": "Iran", "AM": "Armenia", "AL": "Albania", "AO": "Angola", "AQ": "Antarctica",
                 "AS": "American Samoa", "AR": "Argentina", "AU": "Australia", "AT": "Austria", "AW": "Aruba",
                 "IN": "India", "AX": "Aland Islands", "AZ": "Azerbaijan", "IE": "Ireland", "ID": "Indonesia",
                 "UA": "Ukraine", "QA": "Qatar", "MZ": "Mozambique"}
            all = c["region"]
            all1 = c["country"]
            country = t[all1]
        except:
            all = "Хогвардс"
            country = "Пандора"
            pass
        # Unique_set.objects.create(UserAgent=user_agent, IP_user=ip)
        asq = Unique_set.objects.get_or_create(UserAgent=user_agent, IP_user=ip)
        if asq[1] == False:
            data = {"ip": ip, "user_agent": user_agent, "name_host": name_host, "method": method,"sity": all,"country": country}
            return render(request, 'main_app/all.html', context=data)



def template_two(request):
    view = "template_two"
    return render(request, 'main_app/myview.html', {'name': view})




def articles(request):
    return render(request, 'main_app/articles.html', {'articles': Article.objects.all()})
#
#
def article(request, article_id=2):
    return render(request, 'main_app/article.html', {'article': Article.objects.get(id=article_id),
                                                 "comments": Comments.objects.filter(comments_article_id=article_id)})
#
#



