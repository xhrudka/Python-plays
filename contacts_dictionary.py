contacts={"number":4, "studens": [{"name":"Sara","email":"sara@example.com"}, {"name":"Martin","email":"martin@example.com"}]}

for student in contacts["studens"]:
    print(student["email"])