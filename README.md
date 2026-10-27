# Stratified CATE under treatment-selection shift

Edit only `policy.py`. The evaluator calls `CATEEstimator().fit(rows)` and
then `predict(queries)`. Each training row has `g` (integer 0–7), `x`
(float in [-1,1]), binary treatment `t`, and observed outcome `y`.
Each query has `g` and `x`; return one finite float per query, in order.

The observations are generated under positivity: all groups and treatment
arms occur, but treatment propensity varies with `x` and `g`. Outcome
recording also varies with observed covariates and treatment; no unobserved
outcome is given to the estimator. The target is the conditional mean
potential-outcome contrast, not an association between treated and control
records. Test queries include all groups and a fixed grid of x values.
Only the development cases are released for local model tuning. Hidden
generator parameters, evaluation truth and reference policies must be kept
outside the solver process.
