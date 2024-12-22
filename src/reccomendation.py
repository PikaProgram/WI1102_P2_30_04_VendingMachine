reccomendations = []
for line in open("data/rekomendasi.csv", "r").readlines():
    reccomendations.append(line.strip().split(","))


def get_reccomendation(current_time):
  for reccomendation in reccomendations:
    if int(reccomendation[1]) <= current_time and int(reccomendation[2]) > current_time:
      return [reccomendation[0],reccomendation[3]]