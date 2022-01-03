# Copyright Florentin Schleuß 2020-2022. Licensed under 
# the EUPL-1.2 or later

# The MIT License (MIT)
# 
# Copyright (c) 2015 The Axelrod-Python project team members listed at
# https://github.com/Axelrod-Python/Axelrod/graphs/contributors
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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