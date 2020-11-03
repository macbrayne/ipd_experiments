import axelrod as axl
from tools import plot_eco, run_tournament
#players = [s() for s in axl.short_run_time_strategies]  # Create players
#players = [s() for s in axl.demo_strategies]  # Create players
players = [s() for s in axl.axelrod_first_strategies]  # Create players
#players = [axl.Calculator(), axl.Prober(), axl.Punisher(), axl.Defector(), axl.TitForTat(), axl.GoByMajority(), axl.OriginalGradual(), axl.Random()]
plot_eco(results=run_tournament(players), title="First Strategies")