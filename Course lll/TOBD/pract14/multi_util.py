from bs4 import BeautifulSoup


def get_reviewers_dict(filename):
    with open(filename, "r") as fp:
        data = BeautifulSoup(fp, 'lxml')
        reviewers = []

        for el in data.find_all("user"):
            id = int(exists(el.find("id")))
            username = exists(el.find("username"))
            name = exists(el.find("name"))
            sex = exists(el.find("sex"))
            country = exists(el.find("country"))
            mail = exists(el.find("mail"))
            registered = exists(el.find("registered"))
            birthdate = exists(el.find("birthdate"))
            name_prefix = el.get("prefix")

            if el.find("country") is None:
                country_code = None
            else:
                country_code = el.find("country").get("code")

            user = {"id": id, "username": username, "name": name, "sex": sex,
                    "country": country, "mail": mail, "registered": registered,
                    "birthdate": birthdate, "name_prefix": name_prefix,
                    "country_code": country_code}

            reviewers.append(user)
        return reviewers


def exists(value):
    return value if value is None else value.text
