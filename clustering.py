import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import MeanShift
import numpy as np


# slecting representative samples
def generate_logs(df, tfidf_matrix, mean_shift, labels, num_representative=3):
    representative_logs = []
    for cluster in np.unique(labels):
        cluster_points = df[df['cluster'] == cluster]
        cluster_center = mean_shift.cluster_centers_[cluster]
        # distance of log to its cluster center
        distances = np.linalg.norm(tfidf_matrix[cluster_points.index].toarray() - cluster_center, axis=1)
        # indicies of closest logs (most representative of cluster)
        closest_indices = np.argsort(distances)
        step = max(1, len(closest_indices) // num_representative)
        selected_indices = closest_indices[::step][:num_representative]
        # append most representative logs for each cluster
        for idx in selected_indices:
            representative_logs.append(cluster_points.iloc[idx]['Log'])

        logs_separated = '\n'.join(representative_logs)
    return logs_separated


def get_representative_logs(input_path, num_representative=3):
    # TF-IDF
    df = pd.read_csv(input_path)
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df['Log'])

    # mean shift
    mean_shift = MeanShift()
    mean_shift.fit(tfidf_matrix.toarray())
    labels = mean_shift.labels_

    # adding cluster labels
    df['cluster'] = labels

    logs = generate_logs(df, tfidf_matrix, mean_shift, labels, num_representative)
    return logs