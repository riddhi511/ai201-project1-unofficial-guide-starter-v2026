# Acceptance Criteria

1. For at least 4 of my 5 test questions, the retrieved chunks include one
   that contains the answer.

   Reason: I picked 4 of 5 because one question about dorms may only appear
   in one or two documents, making a perfect score unrealistic.

2. Every answer the system produces names at least one source document.

   Reason: Grounding requires a source — if no source is named, the answer
   could be made up. This is observable on every single run.

3. When I ask a question my documents clearly don't cover, the relevance gate
   stops it and the system returns "I don't have enough information about
   that" — in at least 4 of 5 tries.

   Reason: 4 of 5 because one out-of-scope question might accidentally share
   words with a campus document and slip through.

4. At least 4 of my 5 chunks read as complete thoughts — a person could
   answer a question using only that chunk, without reading what came before
   or after.

   Reason: Chunks that are fragments hurt retrieval quality. I picked 4 of 5
   to allow for one edge case where a sentence naturally runs across a boundary.

5. For at least 3 of my 5 test questions, the best retrieved chunk has a
   distance below 0.4, indicating a strong semantic match.

   Reason: A distance below 0.4 means the system found something genuinely
   relevant, not just a keyword overlap. I picked 3 of 5 because some
   questions are phrased differently from how the documents phrase answers.