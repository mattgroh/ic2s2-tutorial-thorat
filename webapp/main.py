import os
from flask import Blueprint, render_template

# from flask import request, flash, redirect, session, g, make_response, Response, jsonify, url_for
# import random
# import hashlib

# from .models_x import Survey
# from . import db

# from .models_x import Guess
# import pandas as pd 

basedir = os.path.abspath(os.path.dirname(__file__))
main = Blueprint('main', __name__)

# # Step 1 – Let's get our server up and running
# @main.route('/')
# def home():
#     return "HELLO WORLD!"


# # Step 2 – Let's see what Flask – a micro web framework – can do!
# @main.route('/informed-consent')
# def consent():
#     return render_template('consent.html',
#     	informed_consent_text="""
#     	"Custom Experiments with Thorat" is the first step in a tutorial for Thorat, 
#     	a starter pack for building custom dynamic websites for high throughput 
#     	virtual experimentation in computational social science. Generally, "Informed Consent" 
#     	should clarify (1) this is a research experiment, (2) hosted by institution X, (3) all 
#     	submissions are collected anonymously (or only used for research purposes or whatever
#     	is approved by your IRB), (4) for questions, please contact email@university.edu, (5)
#     	you may leave this website at anytime.
#     	""")

# # Step 3 – Let's build a route for the about page

# #
# #
# #

# # Step 4 – Let's start collecting data!
# @main.route('/start')
# def start_survey():
#     try:
#         headers_list = request.headers.getlist("X-Forwarded-For")
#         ip = headers_list[0] if headers_list else request.remote_addr
#     except:
#         ip = "error"
#     user_agent = request.user_agent
#     experiment_id = request.args.get('experiment', default = '', type = str)
#     study_id = request.args.get('study_id', default = '', type = str)
#     x = str(random.uniform(0,1)) + str(random.uniform(0,1))
#     user_id = hashlib.md5(x.encode()).hexdigest()
#     sq0 = """Have you tried deepdish pizza in Chicago?"""
#     sa0 = ["----Please select one----", 
#             "Yes, and it's amaazing!",
#             "Yes, but it's too soupy for me.",
#             "No, but I'm super excited to try Lou Malnati's this week",
#             "No, I'm just not a pizza person."
#             ]
#     sq1 = """What country do you currently live in?"""
#     sa1 = ["----Please select one----", 'Afghanistan', 'Åland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua & Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia & Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Caribbean Netherlands', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo - Brazzaville', 'Congo - Kinshasa', 'Cook Islands', 'Costa Rica', 'Côte d’Ivoire', 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czechia', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Falkland Islands', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard & McDonald Islands', 'Honduras', 'Hong Kong SAR China', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao SAR China', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar (Burma)', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'North Korea', 'North Macedonia', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territories', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn Islands', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russia', 'Rwanda', 'Samoa', 'San Marino', 'São Tomé & Príncipe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia & South Sandwich Islands', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'St. Barthélemy', 'St. Helena', 'St. Kitts & Nevis', 'St. Lucia', 'St. Martin', 'St. Pierre & Miquelon', 'St. Vincent & Grenadines', 'Sudan', 'Suriname', 'Svalbard & Jan Mayen', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad & Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks & Caicos Islands', 'Tuvalu', 'U.S. Outlying Islands', 'U.S. Virgin Islands', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', "United States of America",'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Wallis & Futuna', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']
#     sq2 = """How many elevators in the Empire State building?"""
#     sa2 = ["----Please select one----", "0","4","9","13","29", "73", "97","102"]
#     sq3 = """A bat and a ball cost..."""
#     sa3 = ["----Please select one----", "0.10 cents","0.05 cents", "Not enough information", "47 lilypads", "5 minutes"]
#     sq4 = """On average, do you think your friends have more friends than you or you have more friends then them?"""
#     sa4 = ["----Please select one----", "I have more friends than my friends do", "My friends have more friends than I do"]
#     sq5 = """Have you ever built a website before?"""
#     sa5 = ["----Please select one----", "Yes", "No"]
#     sq6 = """How do you feel things are going?"""
#     sa6 = ["----Please select one----", "Excellent",  "Pretty good", "Alright", "Not bad", "Kinda bad", "Terrible"]
#     resp = make_response(
#             render_template('beginning.html', 
#                 sq0=sq0,
#                 sa0=sa0,
#                 sq1=sq1,
#                 sa1=sa1,
#                 sq2=sq2,
#                 sa2=sa2,
#                 sq3=sq3,
#                 sa3=sa3,
#                 sq4=sq4,
#                 sa4=sa4,
#                 sq5=sq5,
#                 sa5=sa5,
#                 sa6=sa6,
#                 sq6=sq6,
#             ))
#     resp.set_cookie('id_save', user_id)
#     resp.set_cookie('referral_source', experiment_id)
#     resp.set_cookie('study_id', study_id)
#     return resp

# @main.route('/go', methods = ['POST'])
# def step1():
#     print("Sometimes it's useful to print things for debugging")
#     print(request.form)
#     a0 = request.form['sa0']
#     a1 = request.form['sa1']
#     a2 = request.form['sa2']
#     a3 = request.form['sa3']
#     a4 = request.form['sa4']
#     a5 = request.form['sa5']
#     a6 = request.form['sa6']
#     a7 = "space_holder"
#     faithful = "faithful" in request.form.keys()
#     user_id = request.cookies.get('id_save')
#     referral_source = request.cookies.get('referral_source')
#     study_id = request.cookies.get('study_id')
#     if not referral_source:
#         referral_source =  "none"
#         study_id = "none"
#     survey_response = Survey(user_id=user_id, referral_source=referral_source, study_id=study_id,
#                                 a0=a0,a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,a7=a7,
#                                 faithful=faithful)
#     db.session.add(survey_response)
#     db.session.commit()
#     print(a0,a1,a2,a3)
#     return redirect('/')

# # Step 5 – Let's run an experiment

# @main.route('/experiment')
# def experiment():
#     user_id = request.cookies.get('id_save')
#     print(user_id)
#     if not user_id:
#         return redirect("/start")
#     res = db.session.query(Survey).filter_by(user_id=user_id).all()
#     seen = [i.__dict__['faithful'] for i in res]
#     if len(seen)==0:
#         return redirect('/start')
#     try:
#         headers_list = request.headers.getlist("X-Forwarded-For")
#         ip = headers_list[0] if headers_list else request.remote_addr
#     except:
#         ip = "error" 

#     # Look at what imgs a user has seen and show the user something new
#     res = db.session.query(Guess).filter_by(user_id=user_id).all()    
#     seen = list(set([i.__dict__['image_id'] for i in res]))
#     print(seen)
#     print("ABC")
#     unseen = False
#     # img_path = "/static/img/giuseppe_arcimboldo/"
#     # img = "librarian.jpg"


    
#     artist = random.choice(["giuseppe_arcimboldo","magritte"])
#     img_path = "/static/img/{}/".format(artist)
#     images = os.listdir("webapp/static/img/{}/".format(artist))
#     for i in seen:
#     	try:
#     		images.remove(i)
#     	except:
#     		pass
#     img = random.choice(images)
#     emotions = skin_conditions = ["Acceptance",'Admiration',
# 		 'Adoration',
# 		 'Affection',
# 		 'Afraid',
# 		 'Agitation',
# 		 'Agony',
# 		 'Aggressive',
# 		 'Alarm',
# 		 'Alarmed',
# 		 'Alienation',
# 		 'Amazement',
# 		 'Ambivalence',
# 		 'Amusement',
# 		 'Anger',
# 		 'Anguish',
# 		 'Annoyed',
# 		 'Anticipating',
# 		 'Anxious',
# 		 'Apathy',
# 		 'Apprehension',
# 		 'Arrogant',
# 		 'Assertive',
# 		 'Astonished',
# 		 'Attentiveness',
# 		 'Attraction',
# 		 'Aversion',
# 		 'Awe',
# 		 'Baffled',
# 		 'Bewildered',
# 		 'Bitter',
# 		 'Bitter sweetness',
# 		 'Bliss',
# 		 'Bored',
# 		 'Brazen',
# 		 'Brooding',
# 		 'Calm',
# 		 'Carefree',
# 		 'Careless',
# 		 'Caring',
# 		 'Charity',
# 		 'Cheeky',
# 		 'Cheerfulness',
# 		 'Claustrophobic',
# 		 'Coercive',
# 		 'Comfortable',
# 		 'Confident',
# 		 'Confusion',
# 		 'Contempt',
# 		 'Content',
# 		 'Courage',
# 		 'Cowardly',
# 		 'Cruelty',
# 		 'Curiosity',
# 		 'Cynicism',
# 		 'Dazed',
# 		 'Dejection',
# 		 'Delighted',
# 		 'Demoralized',
# 		 'Depressed',
# 		 'Desire',
# 		 'Despair',
# 		 'Determined',
# 		 'Disappointment',
# 		 'Disbelief',
# 		 'Discombobulated',
# 		 'Discomfort',
# 		 'Discontentment',
# 		 'Disgruntled',
# 		 'Disgust',
# 		 'Disheartened',
# 		 'Dislike',
# 		 'Dismay',
# 		 'Disoriented',
# 		 'Dispirited',
# 		 'Displeasure',
# 		 'Distraction',
# 		 'Distress',
# 		 'Disturbed',
# 		 'Dominant',
# 		 'Doubt',
# 		 'Dread',
# 		 'Driven',
# 		 'Dumbstruck',
# 		 'Eagerness',
# 		 'Ecstasy',
# 		 'Elation',
# 		 'Embarrassment',
# 		 'Empathy',
# 		 'Enchanted',
# 		 'Enjoyment',
# 		 'Enlightened',
# 		 'Ennui',
# 		 'Enthusiasm',
# 		 'Envy',
# 		 'Epiphany',
# 		 'Euphoria',
# 		 'Exasperated',
# 		 'Excitement',
# 		 'Expectancy',
# 		 'Fascination',
# 		 'Fear',
# 		 'Flakey',
# 		 'Focused',
# 		 'Fondness',
# 		 'Friendliness',
# 		 'Fright',
# 		 'Frustrated',
# 		 'Fury',
# 		 'Glee',
# 		 'Gloomy',
# 		 'Glumness',
# 		 'Gratitude',
# 		 'Greed',
# 		 'Grief',
# 		 'Grouchiness',
# 		 'Grumpiness',
# 		 'Guilt',
# 		 'Happiness',
# 		 'Hate',
# 		 'Hatred',
# 		 'Helpless',
# 		 'Homesickness',
# 		 'Hope',
# 		 'Hopeless',
# 		 'Horrified',
# 		 'Hospitable',
# 		 'Humiliation',
# 		 'Humility',
# 		 'Hurt',
# 		 'Hysteria',
# 		 'Idleness',
# 		 'Impatient',
# 		 'Indifference',
# 		 'Indignant',
# 		 'Infatuation',
# 		 'Infuriated',
# 		 'Insecurity',
# 		 'Insightful',
# 		 'Insulted',
# 		 'Interest',
# 		 'Intrigued',
# 		 'Irritated',
# 		 'Isolated',
# 		 'Jealousy',
# 		 'Joviality',
# 		 'Joy',
# 		 'Jubilation',
# 		 'Kind',
# 		 'Lazy',
# 		 'Liking',
# 		 'Loathing',
# 		 'Lonely',
# 		 'Longing',
# 		 'Loopy',
# 		 'Love',
# 		 'Lust',
# 		 'Mad',
# 		 'Melancholy',
# 		 'Miserable',
# 		 'Miserliness',
# 		 'Mixed up',
# 		 'Modesty',
# 		 'Moody',
# 		 'Mortified',
# 		 'Mystified',
# 		 'Nasty',
# 		 'Nauseated',
# 		 'Negative',
# 		 'Neglect',
# 		 'Nervous',
# 		 'Nostalgic',
# 		 'Numb',
# 		 'Obstinate',
# 		 'Offended',
# 		 'Optimistic',
# 		 'Outrage',
# 		 'Overwhelmed',
# 		 'Panicked',
# 		 'Paranoid',
# 		 'Passion',
# 		 'Patience',
# 		 'Pensiveness',
# 		 'Perplexed',
# 		 'Persevering',
# 		 'Pessimism',
# 		 'Pity',
# 		 'Pleased',
# 		 'Pleasure',
# 		 'Politeness',
# 		 'Positive',
# 		 'Possessive',
# 		 'Powerless',
# 		 'Pride',
# 		 'Puzzled',
# 		 'Rage',
# 		 'Rash',
# 		 'Rattled',
# 		 'Regret',
# 		 'Rejected',
# 		 'Relaxed',
# 		 'Relieved',
# 		 'Reluctant',
# 		 'Remorse',
# 		 'Resentment',
# 		 'Resignation',
# 		 'Restlessness',
# 		 'Revulsion',
# 		 'Ruthless',
# 		 'Sadness',
# 		 'Satisfaction',
# 		 'Scared',
# 		 'Schadenfreude',
# 		 'Scorn',
# 		 'Self-caring',
# 		 'Self-compassionate',
# 		 'Self-confident',
# 		 'Self-conscious',
# 		 'Self-critical',
# 		 'Self-loathing',
# 		 'Self-motivated',
# 		 'Self-pity',
# 		 'Self-respecting',
# 		 'Self-understanding',
# 		 'Sentimentality',
# 		 'Serenity',
# 		 'Shame',
# 		 'Shameless',
# 		 'Shocked',
# 		 'Smug',
# 		 'Sorrow',
# 		 'Spite',
# 		 'Stressed',
# 		 'Strong',
# 		 'Stubborn',
# 		 'Stuck',
# 		 'Submissive',
# 		 'Suffering',
# 		 'Sullenness',
# 		 'Surprise',
# 		 'Suspense',
# 		 'Suspicious',
# 		 'Sympathy',
# 		 'Tenderness',
# 		 'Tension',
# 		 'Terror',
# 		 'Thankfulness',
# 		 'Thrilled',
# 		 'Tired',
# 		 'Tolerance',
# 		 'Torment',
# 		 'Triumphant',
# 		 'Troubled',
# 		 'Trust',
# 		 'Uncertainty',
# 		 'Undermined',
# 		 'Uneasiness',
# 		 'Unhappy',
# 		 'Unnerved',
# 		 'Unsettled',
# 		 'Unsure',
# 		 'Upset',
# 		 'Vengeful',
# 		 'Vicious',
# 		 'Vigilance',
# 		 'Vulnerable',
# 		 'Weak',
# 		 'Woe',
# 		 'Worried',
# 		 'Worthy',
# 		 'Wrath']
#     resp = make_response(
#             render_template('index.html', 
#                             seen=len(seen)+1, 
#                             name="imgs", 
#                             ip=ip, 
#                             image=img,
#                             img_path=img_path,
#                             confetti="confetti",
#                             artist="Most people say {} and {}".format(random.choice(emotions), random.choice(emotions))
#                             ))
#     resp.set_cookie('id_save', user_id)
#     resp.set_cookie('image', img)
#     return resp

# @main.route('/guess', methods=['POST'])
# def guess():
#     user_agent = request.user_agent
#     print(request.json)
#     try:
#         headers_list = request.headers.getlist("X-Forwarded-For")
#         ip = headers_list[0] if headers_list else request.remote_addr
#     except:
#         ip = "error"
#     img = request.json['image']
#     g = request.json['guess']
#     differential2 = request.json['differential2']
#     differential3 = request.json['differential3']
#     correct_guess = request.json['correct']
#     g_round = request.json['round']
#     g_int = request.json['guess_int']
    
#     seen = int(float(request.json['seen']))
#     model_selection = "none"
#     order_decision_support = "none"
#     try:
#         user_id = request.cookies.get('id_save')

#     except:
#         user_id = "error"
    
#     prolific_pid = request.cookies.get('prolific_pid')
#     study_id = request.cookies.get('study_id')
#     session_id = request.cookies.get('session_id')
#     if not prolific_pid:
#         prolific_pid =  "none"
#         study_id = "none"
#         session_id = "none"
#     print(prolific_pid)
#     biopsy = request.json['biopsy']
#     dermatologist = ""
#     blood_work = ""
#     topical_steriods = ""
#     topical_antibiotics = ""
#     oral_antibiotics = ""
#     systemic_therapy = ""
#     new_Guess = Guess(
#             image_id=img, 
#             correct_guess=correct_guess,
#             guess = g, 
#             differential_two=differential2,
#             differential_three=differential3, 
#             seen=seen, 
#             guess_int=g_int,
#             guess_round=g_round, 
#             user_id=user_id, 
#             ip=ip,
#             user_platform=user_agent.platform, 
#             user_browser=user_agent.browser, 
#             biopsy=biopsy, 
#             dermatologist=dermatologist,
#             model_selection="randomizer",
#             changer="support_tool",
#             assignment="random_assignment"
#             # prolific_pid=prolific_pid,
#             # study_id=study_id,
#             # session_id=session_id, 
#                     )
#     db.session.add(new_Guess)
#     db.session.commit()
#     resp = make_response(render_template('consent.html'))
#     resp.set_cookie('id_save', user_id)
#     return resp