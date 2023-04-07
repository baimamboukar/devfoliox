from flask import Flask, render_template
import json
import requests
import feedparser
from datetime import datetime
from bs4 import BeautifulSoup


def get_github_activies():
    # Set the GitHub username for which you want to fetch activities
    username = "baimamboukar"
    # Make GET request to fetch recent activities
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response to JSON
        activities = json.loads(response.text)
        # Print the recent activities in JSON format
        return activities
    else:
        return {

        }


def find_cover_image(html_string):
    soup = BeautifulSoup(html_string, 'html.parser')
    img_tag = soup.find('img')
    if img_tag:
        src = img_tag.get('src')
        return src


def parse_date(date_string):
    # Convert the date string to datetime object
    date_object = datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S %Z')

    # Extract day and month from the datetime object
    day = date_object.day
    month = date_object.strftime('%b')

    # Create a JSON object with day and month
    result = {'day': day, 'month': month}
    return result


def get_abstract(html_string):
    soup = BeautifulSoup(html_string, 'html.parser')
    p_tag = soup.find('p')
    if p_tag:
        return p_tag.text


def get_medium_feeds():
    # URL of the Medium feed
    url = "https://medium.com/feed/@baimamboukar"

    # Parse the feed
    feed = feedparser.parse(url)

    # Convert the feed to JSON
    json_feed = json.dumps(feed, indent=4)

    filtered_feeds = []
    for entry in feed["entries"][:3]:
        filtered_feeds.append(
            {
                "title": entry["title"],
                "cover_image": find_cover_image(entry["content"][0]["value"]) or "https://miro.medium.com/max/1200/1*mk1-6aYaf_Bes1E3Imhc0A.jpeg",
                "id": entry["id"],
                "tags": [tag["term"] for tag in entry["tags"]][:3],
                "link": entry["link"],
                "date": parse_date(entry["published"]),
                "abstract": get_abstract(entry["content"][0]["value"]) or "",
                "summary": entry["summary"],
            }
        )
    # Print the JSON feed
    return filtered_feeds


def get_recommendations():
    return [
        {
            "author": "Diffouo Fopa Esdras",
            "title": "Data Engineer",
            "content": "My personal flutter evangelist, Out of the box thinker, team builder and project management expert. Digital marketer with accomplished teaching and explanation skills",
            "star": 4,
            "link": "https://www.linkedin.com/in/baimamboukar/details/recommendations/",
        },
        {
            "author": "Myra Sika",
            "title": "Fronted Web Developer",
            "content": "Great leader and awesome person to work with.",
            "star": 5,
            "link": "https://www.linkedin.com/in/baimamboukar/details/recommendations/",
        },
        {
            "author": "Assa Jean Ulrich",
            "title": "Technical Product Manager @SahelFund",
            "content": "I know Mr. Baimam Boukar Jean Jacques since 03 year now, grow up with his brothers to, he's self disciplined and like challenges. Trust me he's the best on his domain",
            "star": 5,
            "link": "https://www.linkedin.com/in/baimamboukar/details/recommendations/",
        },
        {
            "author": "Mboh Bless Pearl",
            "title": "Mobile Dev | Beta MLSA | AWS CCP",
            "content": "he is a very great and commited individual. when it comes to his work responds on time to team mate requests and also. also he's a problem solver bringing forth the best solutions to hard problems",
            "star": 5,
            "link": "https://www.linkedin.com/in/baimamboukar/details/recommendations/",
        },
        {
            "author": "Abdoul Azis",
            "title": "GDSC ICT University Lead",
            "content": "He's a tech passionate and a professional, very meticulous in every project he gets involved. He's a team player and a great leader. He's a great mentor and a great friend.",
            "star": 5,
            "link": "https://www.linkedin.com/in/baimamboukar/details/recommendations/",
        },

    ]


def technologies():
    return [
        {
            "name": "Flutter",
            "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flutter/flutter-original.svg"
        },
        {
            "name": "Dart",
            "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/dart/dart-original.svg"
        },
        {
            "name": "Google Cloud",
            "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg"
        },
        {
            "name": "Flask",
            "logo": "https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg"
        },
        {
            "name": "Python",
            "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"
        },
        {
            "name": "Node.js",
            "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg"
        },
        {
            "name": "Firebase",
            "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/firebase/firebase-plain.svg"
        },
        {
            "name": "GitHub",
            "logo": "https://www.vectorlogo.zone/logos/github/github-icon.svg"
        },
        {
            "name": "Postman",
            "logo": "https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg"
        },
        {
            "name": "VsCode",
            "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg"
        }
    ]


def services():
    return [
        {
            "name": "Mobile Development",
            "desc": "High-quality mobile app development for Android and iOS platforms using Flutter."
        },
        {
            "name": "Google Cloud Development",
            "desc": "Creating scalable backend solutions using Google Cloud Platform (GCP) services like Firebase, Cloud Functions, Firestore, and more."
        },
        {
            "name": "Backend Development",
            "desc": "Building robust RESTful APIs and scalable database architectures using Node.js, Express, and MongoDB."
        },
        {
            "name": "Data Engineering",
            "desc": "Designing, developing, and optimizing data pipelines and ETL processes using Google Cloud Data technologies."
        }

    ]


def get_projects():
    return [
        {
            "name": "Eureka Learn",
            "desc": "Eureka Learn is a learning platform that provides a wide range of courses and tutorials for students and professionals. It is built using Flutter and Firebase.",
            "link": "https://play.google.com/store/apps/details?id=com.eurekalearn.app",
            "cover": "img/project/eureka.png",
            "class": "cat-one cat-four"
        },
        {
            "name": "Intellibra",
            "desc": "Breast cancer app that uses machine learning to detect breast cancer. It is built using Flutter and Firebase.",
            "link": "https://play.google.com/store/apps/details?id=com.eurekalearn.app",
            "cover": "img/project/intellibra.png",
            "class": "cat-one cat-two"
        },
        {
            "name": "Alora",
            "desc": "Crop disease detection app that uses machine learning to detect crop diseases. It is built using Flutter and Firebase.",
            "link": "https://play.google.com/store/apps/details?id=com.eurekalearn.app",
            "cover": "img/project/alora-min.png",
            "class": "cat-one cat-two"
        },
        {
            "name": "Electchain",
            "desc": "Voting system that uses blockchain technology to ensure the security of the voting process. It is built using Flutter and Firebase.",
            "link": "https://play.google.com/store/apps/details?id=com.eurekalearn.app",
            "cover": "img/project/electchain.png",
            "class": "cat-one cat-two"
        },
        {
            "name": "Cosmosense",
            "desc": "Space app that provides information about the solar system. It is built using Flutter and Firebase. Nasa and SapceX APIs are used to fetch data.",
            "link": "https://play.google.com/store/apps/details?id=com.eurekalearn.app",
            "cover": "img/project/cosmo.png",
            "class": "cat-one cat-two"
        },
        {
            "name": "Akila",
            "desc": "Cameroon payment app that allows users to send and receive money. It is built using Flutter and Firebase.",
            "link": "https://play.google.com/store/apps/details?id=com.eurekalearn.app",
            "cover": "img/project/cosmo.png",
            "class": "cat-one cat-two",

        },
        {
            "name": "Hymnes Adventistes",
            "desc": "Muti-language Adventist hymn app that allows users to listen to hymns in different languages. It is built using Flutter and Firebase.",
            "link": "https://play.google.com/store/apps/details?id=com.eurekalearn.app",
            "cover": "img/project/cosmo.png",
            "class": "cat-one cat-four cat-two"
        },
        {
            "name": "Omnisense AI",
            "desc": "AI powered chatbot that can be used for various use cases including pararaph generation, text summarization, and more. It is built using Flutter and Google Cloud Platform and OpenAI APIs.",
            "link": "https://play.google.com/store/apps/details?id=com.eurekalearn.app",
            "cover": "img/project/cosmo.png",
            "class": "cat-one cat-two cat-five"
        },
    ]


app = Flask(__name__)

app.debug = True


@app.route("/")
def index():
    feeds = get_medium_feeds()
    stack = technologies()
    skills = services()
    projects = get_projects()
    reco = get_recommendations()
    return render_template("index.html", feeds=feeds, services=skills, technologies=stack, projects=projects, recommendations=reco)


if __name__ == "__main__":
    app.run()
