#!/usr/local/bin/python

import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("eukaryotes.txt", sep="\t", na_values=["-"])
    print("How many fungal species have genomes bigger than 100Mb? What are their names?")
    q1 = df[(df["Group"] == "Fungi") & (df["Size (Mb)"] > 100)]["#Organism/Name"]
    print(q1)
    print()
    print("How many of each Kingdom/group (plants, animals, fungi and protists) have been sequenced?")
    q2 = df["Group"].value_counts()
    print(q2)
    print()
    print("Which Heliconius species genomes have been sequenced?")
    heliconius = df.apply(lambda x: "Heliconius" in x["#Organism/Name"], axis=1)
    q3 = set(df[heliconius]["#Organism/Name"])
    print(q3)
    print()
    print("Which sequencing centre has sequenced the most plant genomes? the most insect genomes?")
    print("Plants")
    df_plant = df[df["Group"] == "Plants"]
    q4_1 = df_plant["Center"].value_counts()
    print(q4_1)
    print("Insects")
    df_insect = df[df["SubGroup"] == "Insects"]
    q4_2 = df_insect["Center"].value_counts()
    print(q4_2)
    print()
    print("Add a column giving the number of proteins per gene. "
          "Which genomes have at least 10% more proteins than genes?")
    df["pro_p_gene"] = df["Proteins"] / df["Genes"]
    q5 = df[df["pro_p_gene"] >= 1.1][["#Organism/Name", "pro_p_gene"]]
    print(q5)
