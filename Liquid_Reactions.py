import plotly as py
import plotly.graph_objs as go
import numpy as np


def liquid_react(stoic, exponents, init_conc, k_vals, t_step=0.001, duration=10):
    """
    stoic = list of tuples of coefficients of reactants and products for each reaction. 
            Reactants should be negative.
    exponents = list of tuples of exponents for eact reactant in the reaction rate 
                equation for each reaction
    init_conc = list of initial concentrations for each reactant and product, mol/m^3
    k_vals = list of floats of k for each reaction, mol/m^3/s
    V = volume of batch reactor, m^3
    t_step = time step for integration, s
    duration = time window of reaction, s
    """
    # Initialize return arrays
    concs = np.array(init_conc).reshape(1, -1)
    times = np.zeros((1, 1))

    # Calculate concentrations for each time_step
    for i in np.arange(t_step, duration, t_step):
        delta_C = np.zeros((1, len(init_conc)))

        for s, e, k in zip(stoic, exponents, k_vals):

            r = k * np.prod(np.power(concs[-1, :], e))

            delta_C += np.multiply(s, r*t_step)

        concs = np.concatenate((concs, concs[-1, :] + delta_C), axis=0)

        times = np.append(times, i)

        # print(i, r, concs[-1,:], delta_C, times[-1])

    return concs, times


def plot_concs(concs, times, filename='Reactions.html'):
    species = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    plots = []
    for i in range(concs.shape[1]):
        trace = go.Scatter(
            x=times,
            y=concs[:, i],
            mode='lines',
            name='Concentration of {}'.format(species[i]),
            line=dict(
                width=2
            )
        )
        plots.append(trace)
    fig = dict(data=plots)
    py.offline.plot(fig, filename=filename)


if __name__ == "__main__":
    concs, times = liquid_react([(-1, -2, 1, 0), (1, 2, -1, 0), (-1, 0, -1, 1)],
                                [(1, 1, 0, 0), (0, 0, 1, 0), (1, 0, 1, 0)],
                                [10, 5, 0, 0],
                                [0.05, 0.02, 0.03],
                                duration=30)

    plot_concs(concs, times)
