
## Sample Answer

**Question:** Is the housing lottery random?

**Answer:**
The housing lottery is not entirely random for everyone; rising sophomores
get a number drawn at random, but juniors and seniors are ordered by
accumulated credit hours first, with a random tie-break used only for ties.
(Source: admin_housing_lottery.txt)

**Relevance cutoff:** 0.6

**Two groups of distances:**

| Question | Best Distance |
|---|---|
| Housing lottery | 0.188 |
| Dining wait times | 0.275 |
| Closest dorms | 0.471 |
| Parking permits | 0.474 |
| Miss registration | 0.491 |
| Best restaurant in Paris | 0.630 |
| Federal taxes | 0.859 |
| 2024 World Cup | 0.851 |
| Speed of light | 0.810 |
| Train neural network | 0.795 |

In-scope questions clustered between 0.188 and 0.491. Out-of-scope questions
clustered between 0.630 and 0.859. The gap between 0.491 and 0.630 is where
I placed the cutoff at 0.6.

## How I Used AI

**Moment 1:** I asked Claude to write the sentence-aware chunker. It returned
a version that used a plain list append without tracking the chunk index. I
added the `index` counter myself so each chunk got the right label, and
changed `produced_by` to `"chunker.py::split_documents"` as required.

**Moment 2:** I asked Claude to help set the relevance cutoff by pasting both
groups of distances. It suggested 0.55 based on the gap. I moved it to 0.6
because the Paris question landed at 0.630 — too close to 0.55 for comfort —
and 0.6 left a cleaner margin on both sides.