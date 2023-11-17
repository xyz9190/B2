

# Define the relevant documents (Rq1) and the answer set (Answer Set A)
Rq1 = ["d3", "d5", "d9", "d25", "d39", "d44", "d56", "d71", "d89", "d123"]
Answer_Set_A = ["d123", "d84", "d56", "d6", "d8", "d9", "d511", "d129", "d187", "d25", "d38", "d48", "d250", "d113", "d3"]

# Initialize variables for precision, recall, F-measure, and E-measure
precision_list = []
recall_list = []
f_measure_list = []
e_measure_list = []

# Iterate through the ranked documents
for i in range(1, len(Answer_Set_A) + 1):
    retrieved_docs = Answer_Set_A[:i]  # Get the first i retrieved documents
    intersection = len(set(Rq1).intersection(retrieved_docs))
    
    precision = intersection / len(retrieved_docs) * 100 if len(retrieved_docs) > 0 else 0.0
    recall = intersection / len(Rq1) * 100 if len(Rq1) > 0 else 0.0
    
    # Calculate F-measure (F1 score)
    if precision + recall > 0:
        f_measure = (2 * precision * recall) / (precision + recall)
    else:
        f_measure = 0.0
    
    # Calculate E-measure
    e_measure = 1 - (1 + 1) / ((precision + 1) * (1 / recall + 1))
    
    precision_list.append(precision)
    recall_list.append(recall)
    f_measure_list.append(f_measure)
    e_measure_list.append(e_measure)

# Display the results
print("Documents |Ra| |A| Precision=|Ra|/|A| Recall=|Ra|/|R| F-measure E-measure")
for i in range(len(Answer_Set_A)):
    print(f"{', '.join(Answer_Set_A[:i+1])} {i+1} {i+1} {precision_list[i]:.2f}% {recall_list[i]:.2f}% {f_measure_list[i]:.2f} {e_measure_list[i]:.2f}")
