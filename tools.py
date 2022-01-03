# Copyright Florentin Schleuß 2020-2022. Licensed under 
# the EUPL-1.2 or later

import axelrod as axl
import matplotlib
matplotlib.use('TkAgg')

def run_tournament(players):
    tournament = axl.Tournament(players, seed=1)  # Create a tournament
    return tournament.play()  # Play the tournament

def plot_eco(results, title="Tournament", reproduce=10000, logscale=True):
    eco = axl.Ecosystem(results)
    eco.reproduce(reproduce)
    plot = axl.Plot(results)
    p = plot.stackplot(eco, title, logscale)
    matplotlib.pyplot.show(p)