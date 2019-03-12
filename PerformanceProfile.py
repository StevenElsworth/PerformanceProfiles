import numpy as np
import matplotlib.pyplot as plt

def PerformanceProfile(A, th_max, file_name='plot.pdf', alg_legend=None, n_intervals=100,
            linewidth=2, markersize=12, markevery=1):
    """
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
        File path to perfomance plot. By default, file_name=plot.pdf'.
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
    """
    m, n = A.shape
    minA = np.min(A, 1)

    plt.figure(figsize=(10,7), dpi=80, facecolor='w', edgecolor='k')
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')

    # Use definition at some points theta
    n_intervals = 100;
    p_step = 1; # increase to make plot look smoother.
    theta = np.linspace(1, th_max, num = n_intervals);
    T = np.zeros([n_intervals,1]);

    linestyle = ['-', '--', '-.', ':']
    marker = ['o', '^', '*', 'x', 'v', '<', 'h', 'p']
    for j in np.arange(0,n):
        for k in np.arange(0,n_intervals):
            T[k] = np.sum(A[:,j] <= theta[k]*minA)/m;

        plt.plot(theta, T, linestyle=linestyle[j%4], linewidth=linewidth,
                marker=marker[j%8], markersize=markersize, markevery=markevery)

    plt.xlim([1, th_max])
    plt.ylim([0, 1.01])
    plt.xlabel(r'$\theta$', fontsize=24)
    plt.ylabel(r'$p$', fontsize=24)
    plt.tick_params(labelsize=20)
    if not alg_legend == None:
        plt.legend(alg_legend, fontsize=24)
    plt.savefig(file_name, facecolor='w', edgecolor='w')
