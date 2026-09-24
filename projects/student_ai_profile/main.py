def get_profile():
    name = input("Name: ").strip()
    age = int(input("Age: "))
    college = input("College: ").strip()
    course = input("Course: ").strip()

    skills = []
    for i in range(3):
        skill = input(f"AI/ML Skill {i + 1}: ").strip()
        skills.append(skill)

    return {
        "name": name,
        "age": age,
        "college": college,
        "course": course,
        "skills": skills,
    }


def display_profile(profile):
    print("\n" + "=" * 35)
    print("       STUDENT AI PROFILE")
    print("=" * 35)
    print("Name   :", profile["name"])
    print("Age    :", profile["age"])
    print("College:", profile["college"])
    print("Course :", profile["course"])
    print("Skills :", ", ".join(profile["skills"]))
    print("=" * 35)


if __name__ == "__main__":
    student_profile = get_profile()
    display_profile(student_profile)
