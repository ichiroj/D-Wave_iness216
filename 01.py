from pyqubo import Binary, solve_qubo
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

import neal

# Define hamiltonian
q0, q1, q2, q3  = Binary("q0"), Binary("q1"), Binary("q2"), Binary("q3")

# Hamiltonian Eq.
#H = 2 * q0*q1 + 2* q0*q2 +  2 * q0*q3 - q0 +  2 * q1*q2 + 2*q1*q3 - q1 + 2*q2*q3 - q2 - q3 + 1
H = (q0 + q1 + q2 + q3 - 2) ** 2

# Create QUBO
model = H.compile()
qubo, offset = model.to_qubo()

#print(qubo)  ## QUBO形式の表示用

# Solve QUBO model by SA
solution = solve_qubo(qubo)
print(solution)
print("------------------------------------------------------------------------------------------")

neal_sampler = neal.SimulatedAnnealingSampler();
neal_response = neal_sampler.sample_qubo(qubo,
                                         num_reads = 10,
                                         label='01.py - neal')
print(neal_response)
print("------------------------------------------------------------------------------------------")

# Solve QUBO model by D-Wave

#endpoint = "https://cloud.dwavesys.com/sapi"
#token = "DEV-xxxxxxxxxxxxxxxxxx"　　##<--　ここは自分のKeyを入れる
#solver_name = "DW_2000Q_2_1"

#sampler = EmbeddingComposite(DWaveSampler(endpoint=endpoint, token=token, solver=solver_name))
sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample_qubo(qubo,
                                num_reads = 10,
                                label='01.py - embedd')
print(response)
