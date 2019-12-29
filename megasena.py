import csv
from raffle_cage import Cage


def load_games(file_name):
     with open(file_name) as csv_file:
          results = []
          csv_reader = csv.reader(csv_file, delimiter=",")
          for row in csv_reader:
               try:
                    results.append([int(n) for n in row])
               except ValueError:
                    pass
     return results


def get_history():
     return load_games("resultados.csv")


def save_games(games, file_name):
     with open(file_name, mode="w") as games_file:
          games_writer = csv.writer(games_file, delimiter=",", quoting=csv.QUOTE_NONE)
          games_writer.writerows(games)


def play_one(cage, dezenas):
     try:
          return sorted([cage.alt_roll() for i in range(dezenas)])
     except TypeError:
          return None


def play(dezenas, history, local_history):
     games = []
     found = []
     local_found = []
     cage = Cage(60)
     while True:
          game = play_one(cage, dezenas)
          if game is None:
               return (sorted(games), found, local_found)
          if game in history:
               found.append(game)
          elif game in local_history or game in games:
               local_found.append(game)
          else:
               games.append(game)


def group(l):
     grouped = {}
     for e in l:
          idx = str(e)
          grouped[idx] = grouped.get(idx, {})
          grouped[idx]["count"] = grouped[idx].get("count", 0) + 1
          grouped[idx]["value"] = e
     return grouped


def play_cages(cages_count, dezenas):
     history = get_history()
     found_log = []
     local_found_log = []
     all_games = []
     for i in range(cages_count):
          games, found, local_found = play(dezenas, history, all_games)
          found_log += found
          local_found_log += local_found
          all_games += games
     return all_games, found_log, sorted(local_found_log)


def play_and_save(cages_count, instance_number):
     games, found, local_found = play_cages(cages_count, 6)
     save_games(games, "games_{}.csv".format(instance_number))


def consolidate(instances_count, path="."):
     all_games = []
     for n in range(instances_count):
          all_games += load_games("{}/games_{}.csv".format(path, n))
     return sorted(all_games)


def consolidate_and_group(instances_count):
     return group(consolidate(instances_count))


def filter_dict(d, filter_fn):
     result = []
     for (k, v) in d.items():
          if filter_fn(v):
               result.append(v)
     return result


def play_and_save_many(cages_count, how_many_times):
     for n in range(how_many_times):
          print("times: ", n)
          play_and_save(cages_count, n)


def count_frequency(games, dezena):
     results = {}
     for game in games:
          d = game[dezena]
          results[d] = results.get(d, 0) + 1
     return results
