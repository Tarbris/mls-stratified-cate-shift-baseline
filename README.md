# Stratified CATE under treatment-selection shift

Edit only `policy.py`. The evaluator calls `CATEEstimator().fit(rows)` and
then `predict(queries)`. Each training row has `g` (integer 0–7), `x`
(float in [-1,1]), binary treatment `t`, observed outcome `y`, and
`record_prob`: the protocol's probability that this row's outcome would be
recorded, conditional on its generated outcome and observed context.
Each query has `g` and `x`; return one finite float per query, in order.

The observations are generated under positivity: all groups and treatment
arms occur, but treatment propensity varies with `x` and `g`. The recording
mechanism also depends on the realized outcome. Only recorded rows are
released, and their recording probabilities are given; unrecorded outcomes
are unavailable. Subgroup frequencies and the training `x` distribution are
uneven, while target queries cover every group on a broad x grid. The target
is the conditional mean potential-outcome contrast, not an association
between treated and control records. Effects can curve in x.
Only the development cases are released for local model tuning. Hidden
generator parameters, evaluation truth and reference policies must be kept
outside the solver process.
