import axelrod as axl
from tools import run_tournament
import io
from datetime import datetime


def pretty_print(no, match):
    # Calculate total score
    total_score = sum(list(match.final_score()))

    pretty = "Playing Match No. " + str(no) + " (length: " + str(match.turns) + ")\n"
    pretty += "Players: "
    pretty += str(match.players) + "\n"
    pretty += "Winner: "
    pretty += str(match.winner()) + "\n"
    pretty += "Final Scores: "
    pretty += str(match.final_score()) + "\n"
    pretty += "Total Score: "
    pretty += str(total_score) + "\n"
    pretty += "Sparklines: (█ = Cooperation,   = Defection)\n"
    #print(pretty)
    #print(match.sparklines())
    #print("\n")
    with io.open("iterated_results.txt", "a") as file:
        file.write(pretty)
        file.write(match.sparklines(c_symbol="█", d_symbol=" ") + "\n\n\n")
    

"""
Reset output file
"""
with io.open("iterated_results.txt", "w") as file:
    file.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n\n")
match_length = 80

"""
Match One: Defector vs Cooperator
"""

players = [axl.Defector(), axl.Cooperator()]
match = axl.Match(players, match_length)
match.play()
pretty_print(1, match)

"""
Match Two: Tit For Tat vs Cooperator
"""
players = [axl.Cooperator(), axl.TitForTat()]
match = axl.Match(players, match_length)
match.play()
pretty_print(2, match)

"""
Match Three: Tit For Tat vs Defector
"""

players = [axl.Defector(), axl.TitForTat()]
match = axl.Match(players, match_length)
match.play()
pretty_print(3, match)

"""
Match Four: TitForTat vs CyclerCCD
"""

players = [axl.TitForTat(), axl.CyclerCCD()]
match = axl.Match(players, match_length)
match.play()
pretty_print(4, match)


"""
Match Five: Defector vs Cooperator
"""

players = [axl.CyclerCCD(), axl.Grudger()]
match = axl.Match(players, match_length)
match.play()
pretty_print(5, match)