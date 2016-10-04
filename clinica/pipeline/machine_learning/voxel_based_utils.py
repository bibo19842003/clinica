
import numpy as np
import csv
from ntpath import basename, splitext

def evaluate_prediction(y, y_hat):

    true_positive = 0.0
    true_negative = 0.0
    false_positive = 0.0
    false_negative = 0.0

    tp = []
    tn = []
    fp = []
    fn = []

    for i in range(len(y)):
        if y[i] == 1:
            if y_hat[i] == 1:
                true_positive += 1
                tp.append(i)
            else:
                false_negative += 1
                fn.append(i)
        else:  # -1
            if y_hat[i] == 0:
                true_negative += 1
                tn.append(i)
            else:
                false_positive += 1
                fp.append(i)

    accuracy = (true_positive + true_negative) / (true_positive + true_negative + false_positive + false_negative)
    sensitivity = true_positive / (true_positive + false_negative)
    specificity = true_negative / (false_positive + true_negative)

    if (true_positive + false_positive) !=  0:
        ppv = true_positive / (true_positive + false_positive)
    else:
        ppv = 0

    if (true_negative + false_negative) != 0:
        npv = true_negative / (true_negative + false_negative)
    else:
        npv = 0

    balanced_accuracy = (sensitivity + specificity) / 2

    results = {'accuracy': accuracy,
               'balanced_accuracy': balanced_accuracy,
               'sensitivity': sensitivity,
               'specificity': specificity,
               'ppv': ppv,
               'npv': npv,
               'predictions': (tp, tn, fp, fn)
               }

    return results


def save_subjects(subjects, diagnosis, y, y_hat, output_file):

    with open(output_file, 'w') as csvfile:

        fieldnames = ['Subject', 'Diagnose', 'Class_label', 'Predicted_label', 'Correct']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(len(subjects)):
            s = splitext(basename(subjects[i]))[0]
            dx = diagnosis[i]
            writer.writerow({'NIP': s,
                             'Diagnose': dx,
                             'Class_label': y[i],
                             'Predicted_label': int(y_hat[i]),
                             'Correct': int(y[i] == y_hat[i])
                             })


def gram_matrix_linear(data):
    return np.dot(data, data.transpose())
