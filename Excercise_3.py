# Task
# Calculated the accuracy using the following formula:
# {accuracy} = {TP+TN}/{TP+TN+FP+FN}

tp = 2
tn = 985
fp = 2
fn = 11

# calulate accuracy in %
accuracy = 100*((tp +tn) / (tp +tn +fp +fn))

print(f"The accuracy of the model is: {accuracy:.1f} %")