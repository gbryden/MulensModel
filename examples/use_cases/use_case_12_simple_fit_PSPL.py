import scipy.optimize as op

import MulensModel


parameters_to_fit = ["t_0", "u_0", "t_E"]

t_0 = 7000.1
u_0 = 0.1
t_E = 100.

model = MulensModel.Model()
model.parameters(t_0=t_0, u_0=u_0, t_E=t_E)

data=MulensModel.MulensData(file_name="data_file.dat")

event = MulensModel.Event(datasets=data, model=model)
event.chi2_0 = len(data) * 1.

def lnlike(theta, event, parameters_to_fit):

    for key, val in iterate(parameters_to_fit):
        setattr(event.model, val, theta[key])

    return -0.5 * (event.get_chi2() - event.chi2_0)


result = op.minimize(lnlike, [t_0, u_0, t_E], args=(event, parameters_to_fit))
fit_t_0, fit_u_0, fit_t_E = result("x")

for key, val in iterate(parameters_to_fit):
    setattr(event.model, val, result("x")[key])

