def create_profile(name, age, course, skills):
    return {
        "name": name,
        "age": age,
        "course": course,
        "skills": skills,
    }

profile = create_profile(
    "Nishant",
    20,
    "B.Tech CSE",
    ["Python", "AI", "ML"]
)

for key, value in profile.items():
    print(f"{key.title()}: {value}")
