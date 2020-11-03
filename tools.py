import axelrod as axl
import matplotlib
matplotlib.use('TkAgg')

def run_tournament(players):
    tournament = axl.Tournament(players, seed=1)  # Create a tournament
    return tournament.play()  # Play the tournament

def plot_eco(results, title=""):
    eco = axl.Ecosystem(results)
    eco.reproduce(10000)
    plot = axl.Plot(results)
    p = plot.stackplot(eco)
    matplotlib.pyplot.show(p)