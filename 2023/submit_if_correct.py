import requests
from urllib import request, parse

def submit_if_correct(solve, answer, true_answer, day, part, year):
    if answer == true_answer:
        session_cookie = "Insert Cookie Here"

        headers = {'cookie': f'session={session_cookie}'}
        response = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", headers=headers)
        input = response.content.decode("ISO-8859-1").strip()
        puzzle_answer = solve(input, False)

        req = request.Request(f"https://adventofcode.com/{year}/day/{day}/answer", headers=headers)
        post_data_raw = parse.urlencode({"answer": puzzle_answer, "level": part}).encode()
        res = request.urlopen(req, data = post_data_raw)
        print(f"Day {day} ({part}/2) submitted: {puzzle_answer}")