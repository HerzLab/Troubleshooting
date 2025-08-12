Note that in some instances you want to lower that duration to e.g. 5s instead of 30s.  It was observed in practice that sometimes (at Jeff) the frequency of the electrical supply slips outside of standard US accuracy specification by enough that 5s measures line noise percentage more accurately than 30s (even though 30s would otherwise be more precise).

The algorithm is fairly straightforward as a principle if one takes a moment to understand it.  The 50Hz/60Hz part is to handle Europe/US.
If you need to build up an intuition for it, it helps to break everything out and plot sel_data and binned.
