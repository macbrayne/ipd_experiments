import axelrod as axl
from tools import *
import io
from datetime import datetime

def pretty_print(no, tournament):
    # Pretty print
    pretty = "Playing Tournament No. " + str(no) + "\n"
    pretty += "Players: "
    pretty += str(tournament.players) + "\n\n"
    pretty += "Player Data:\n"
    for player in (tournament.summarise()):
        pretty += str(player) + "\n"
    pretty += "\n\n"
    with io.open("classical_results.txt", "a") as file:
        file.write(pretty)

"""
Reset output file
"""
with io.open("classical_results.txt", "w") as file:
    file.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n\n")

"""
Tournament One
""" 
players = [axl.Cooperator(), axl.Defector(), \
    axl.Grudger(), axl.CyclerCCD(), \
    axl.TitForTat()]
tournament = run_tournament(players)
pretty_print(1, tournament)
plot_eco(results=tournament, reproduce=20, title="Tournament One", logscale=False)


"""
Tournament Two
"""
players = [axl.Cooperator(), axl.Defector(), \
    axl.Grudger(), axl.CyclerCCD(), \
    axl.TitForTat(), axl.GoByMajority()]
tournament = run_tournament(players)
pretty_print(2, tournament)
plot_eco(results=tournament, reproduce=20, title="Tournament Two", logscale=False)

#players = [axl.Calculator(), axl.Prober(), \
#    axl.Punisher(), axl.Defector(), \
#    axl.TitForTat(), axl.GoByMajority(), \
#    axl.OriginalGradual(), axl.Random()]
# plot_eco(run_tournament(players))