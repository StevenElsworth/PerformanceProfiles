# PerformanceProfiles
Plotting performance profiles in python


Python implementation of Massimiliano Fasi's Performance profiler, soon to
  appear at:
  https://github.com/mfasi

  Similar to Sam Relton's perfprof but requires less memory:
  https://github.com/sdrelton/perfprof

  Makes a performance profile [1] of the M-by-N array A, where A(i,j) > 0 measures
  the performance of the j-th algorithm on the i-th problem. Smaller values of
  A(i,j) denoting a "better" result. For each algorithm theta is plotted against the
  probability that the algorithm is within a factor theta of the best algorithm over
  all problems, for theta on the interval [1, th_max].
  Set A(i,j) = NaN if algorithm j failed to solve problem i.

  Performance profiles easily allow us to compare relative errors of multiple
  algrithms over a large set of test problems. The x-axis represents a tolerance
  and the y-axis represents a percentage of test problems. If the line representing
  algorithm A passes through the point (2, 0.5) then Algorithm A peformed within a
  factor of 2 of the smallest observed value on 50% of the test problems.

  Parameters
  ----------
  A - numpy array
      Array of timings/errors to construct performance profile. The rows
      correspond to different test cases whereas the columns correspond to
      different algorithms.

  th_max - float
      Maximum value of theta shown on x-axis. Defaults to the smallest
      value of theta for which all probabilities are 1 (modulo any NaN
      entries of A).

  file_name - string
      Name of the perfomance plot. By default, file_name=perfprof.pdf'.
      Ensure you specify file extension. Can include relative path if necessary.

  alg_legend - list(string)
      List of strings. One for each algorithm name for legend.

  n_intervals - int
      Number of theta values.

  linewidth - float
      Thickness of lines in plot.

  markersize - float
      Size of markers in plot.

  markevery - int
      How often marker appears on plot. Useful when n_intervals is large to prevent
      plot looking crowded.


  Returns
  -------
  Function saves figure to filename.

  References
  ----------
  [1] E.D. Dolan, and J. J. More,
      Benchmarking Optimization Software with Performance Profiles.
      Math. Programming, 91:201-213, 2002.
