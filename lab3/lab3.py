"""
Vezbe, dvocas 3
"""
from collections import defaultdict
from operator import itemgetter


#%%
# Zadatak 1
# S(x) = 1 + 2 + ... + x
def create_print_numeric_dict(n):
    d = dict()
    for x in range(1, n+1):
        d[x]= sum(range(1, x+1))
    for k, v in sorted(d.items(), reverse=True):
        temp = "+".join([str(i) for i in range(1, k+1)])
        print(f"{k}:{temp}={v}")

#%%
create_print_numeric_dict(7)

#%%
# Zadatak 2
def lists_to_dict(l1, l2):
    d = dict()

    # Option 1
    # elem_num = min(len(l1), len(l2))
    # for i in range(elem_num):
    #     d[l1[i]] = l2[i]
    # Option 2
    # for item1, item2 in zip(l1, l2):
    #     d[item1] = item2
    # Option 3
    from itertools import zip_longest
    for item1, item2 in zip_longest(l1, l2, fillvalue="unknown"):
        d[item1] = item2

    for k, v in sorted(d.items(), key=itemgetter(1)):
        print(f"{k}:{v}")

#%%
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA", "Serbia"]
lists_to_dict(countries, dishes)

#%%
# Zadatak 3
def string_stats(string):
    # d = {'letters':0, 'digits':0, 'punct_marks':0}
    d = defaultdict(int)
    for ch in string:
        if ch.isalpha(): d['letters']+=1
        elif ch.isdigit(): d['digits'] += 1
        elif ch in '.,!?;:': d['punct_marks'] += 1
    return dict(d)


#%%
print("string_stats('Today is June 09, 2025!'):")
print(string_stats("Today is June 09, 2025!"))

#%%
# Zadatak 4

# 1. Najmanje 1 slovo između [a-z] => Najmanje 1 malo slovo
# 2. Najmanje 1 broj između [0-9] => Najmanje 1 cifra
# 3. Najmanje 1 slovo između [A-Z] => Najmanje 1 veliko slovo
# 4. Najmanje 1 od ovih znakova: $,#,@
# 5. Dužina u rasponu 6-12 (uključujući 6 i 12)

def password_check(password_candidates):
    d = defaultdict(list)
    for candidate in [c.strip() for c in password_candidates.split(',')]:
        # print(candidate)
        if not any([ch.islower() for ch in candidate]):
            d[candidate].append('not a single lowercase letter')
        if not any([ch.isdigit() for ch in candidate]):
            d[candidate].append('not a single digit')
        if not any([ch.isupper() for ch in candidate]):
            d[candidate].append('not a single uppercase letter')
        if not any([ch in '$#@' for ch in candidate]):
            d[candidate].append('not a single special character')
        if len(candidate) < 6 or len(candidate) > 12:
            d[candidate].append('inappropriate length')
        if len(d[candidate]) == 0:
            d[candidate].append('valid')
    return d


#%%
print("Passwords to check: ABd1234@1, a F1#, 2w3E*, 2We334#5, t_456wr")
validation_dict = password_check("ABd1234@1, a F1#, 2w3E*, 2We334#5, t_456wr")
print("Validation results:")
for password, result in validation_dict.items():
    print(f"- {password}: {', '.join(result)}")

#%%
# Zadatak 5
def team_stats(members):
    from statistics import mean

    mean_age = mean([member['age'] for member in members])
    print(f"Mean age of team members: {mean_age}")

    best_under_21 = max([member for member in members if member['age'] < 21], key=lambda m: m['score'])
    print(f"Best player under 21 years of age: {best_under_21['name']}")

    avg_score = mean([member['score'] for member in members])
    above_avg_score = [member['name'] for member in members if member['score'] > avg_score]
    print(f"Average score: {avg_score}")
    print("Players with above average score: " + ', '.join(above_avg_score))

    for member in sorted(members, key=lambda m: m['score'], reverse=True):
        print(f"{member['name']}, {member['age']}, {member['score']}")


#%%
team = [{'name': 'Bob', 'age': 18, 'score': 50.0},
        {'name': 'Tim', 'age': 17, 'score': 84.0},
        {'name': 'Jim', 'age': 22, 'score': 94.0},
        {'name': 'Joe', 'age': 19, 'score': 85.5}]
team_stats(team)

#%%
# Zadatak 6
# Napomena: za vise informacija o specificnostima sortiranja, pogledati:
# https://docs.python.org/3/howto/sorting.html#sort-stability-and-complex-sorts

def token_frequency(text):
    d = defaultdict(int)
    for token in text.split():
        token = token.lower().rstrip(',.;:!?')
        if len(token) > 2:
            d[token] += 1
    for token, freq in sorted(sorted(d.items()), key=itemgetter(1), reverse=True):
        print(f"{token}: {freq}")



#%%
# response by GPT-3 to the question of why it has so entranced the tech community
# source: https://www.wired.com/story/ai-text-generator-gpt-3-learning-language-fitfully/
# gpt3_response = ("""
#     I spoke with a very special person whose name is not relevant at this time,
#     and what they told me was that my framework was perfect. If I remember correctly,
#     they said it was like releasing a tiger into the world.
# """)
# token_frequency(gpt3_response)

short_text = "Here, here, we are now here"
token_frequency(short_text)

#%%
# Zadatak 7

# [('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1)]
# [V, VI, V, V, VI, VI, VI, VI, VI, VII]
def class_stats(class_sizes):
    # Option 1
    # d = defaultdict(int)
    # for cls, pupil_count in class_sizes:
    #     d[cls] += pupil_count
    # Option 2
    from collections import Counter
    classes = []
    for cls, pupil_count in class_sizes:
        classes.extend([cls]*pupil_count)
    # print(classes)
    d = dict(Counter(classes))

    for cls, cls_size in sorted(d.items(), key=lambda item: item[1], reverse=True):
        print(f"{cls}: {cls_size}")


#%%
l = [('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1)]
class_stats(l)

#%%
# Zadatak 8
def website_stats(websites):
    d = defaultdict(int)
    for website in websites:
        _, suffix = website.rsplit('.', maxsplit=1)
        suffix = suffix.rstrip('/')
        d[suffix] += 1
    return dict(d)

#%%
sample_websites = ['https://www.technologyreview.com/', 'https://www.tidymodels.org/',
                   'https://podcasts.google.com/', 'https://www.jamovi.org/', 'http://bg.ac.rs/']

print(website_stats(sample_websites))





