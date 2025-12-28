import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import numpy as np
np.set_printoptions(suppress=True)

if __name__ == '__main__':
    df = pd.read_csv('Gen1_data.csv')
    df = df[df['final_evo'] == True]
    stats = df[['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed']]
    scaler = StandardScaler()
    stats = scaler.fit_transform(stats)
    # print(stats)
    kmean = KMeans(n_clusters=5, random_state=42)
    kmean.fit(stats)
    poke_labels = kmean.labels_
    # print(poke_labels)
    df['cluster'] = poke_labels
    cluster_means = df.groupby('cluster')[['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed']].mean(numeric_only=True)
    used_stats = []
    for i, cluster_id in enumerate(cluster_means.index):
        print(f"Cluster {i}")
        row = cluster_means.loc[cluster_id]
        max_stat = row.idxmax()

        if max_stat == 'speed' :
            cluster_name = "Speedster"
        elif max_stat == 'attack':
            cluster_name = "Physical Attacker"
        elif max_stat == 'special-attack':
            cluster_name = "Special Attacker"
        elif max_stat == 'hp':
            cluster_name = "Hp Tank"
        elif max_stat == 'defense':
            cluster_name = "Defensive Wall"
        elif max_stat == 'special-defense':
            cluster_name = "Special Wall"
        else:
            cluster_name = "Balanced"

        used_stats.append(max_stat)

        cluster_pokemon = df[df['cluster'] == i][['name', 'id', 'hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed']]
        print(cluster_name)
        print(f"Num of Pokemon: {len(cluster_pokemon)}")
        print(cluster_pokemon.to_string())

    
    