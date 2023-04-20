import re
import pandas as pd
import matplotlib.pyplot as plt

class EnumerationPlotter:

    def plot(self):    
        # Read the output file content
        with open("enum.pil", "r") as file:
            content = file.read()
            if content.strip() == "":
                print("No content to display.")
                return

        # Extract initial concentrations
        initial_concentrations = re.findall(r"(\w+) = .*? @initial (\d+(?:\.\d+)?) nM", content)

        # Extract macrostate concentrations
        macrostate_concentrations = re.findall(r"macrostate (\w+) = \[(\w+)\]", content)

        # Extract resting complexes
        resting_complexes = re.findall(r"(\w+) = .*? @initial (\d+(?:\.\d+)?) nM", content)

        # Convert the extracted information into dataframes
        initial_concentrations_df = pd.DataFrame(initial_concentrations, columns=["Species", "Initial Concentration"])
        initial_concentrations_df["Initial Concentration"] = pd.to_numeric(initial_concentrations_df["Initial Concentration"])

        macrostate_concentrations_df = pd.DataFrame(macrostate_concentrations, columns=["Macrostate", "Species"])

        resting_complexes_df = pd.DataFrame(resting_complexes, columns=["Complex", "Initial Concentration"])
        resting_complexes_df["Initial Concentration"] = pd.to_numeric(resting_complexes_df["Initial Concentration"])


      
        # Plot the resting complexes
        plt.figure(figsize=(12, 6))
        plt.bar(resting_complexes_df["Complex"], resting_complexes_df["Initial Concentration"])
        plt.xlabel("Resting Complex")
        plt.ylabel("Initial Concentration (nM)")
        plt.title("Resting Complexes Concentrations")
        plt.xticks(rotation=90)
        plt.show()


        # Filter macrostates that don't start with 'e'
        filtered_macrostate_concentrations_df = macrostate_concentrations_df[~macrostate_concentrations_df["Macrostate"].str.startswith("e")]


        # Plot the filtered macrostate concentrations
        filtered_macrostate_counts = filtered_macrostate_concentrations_df["Macrostate"].value_counts()

        plt.figure(figsize=(12, 6))
        plt.bar(filtered_macrostate_counts.index, filtered_macrostate_counts.values)
        plt.xlabel("Macrostate")
        plt.ylabel("Number of Species")
        plt.title("Filtered Macrostate Concentrations (Excluding 'e' Prefix)")
        plt.xticks(rotation=90)
        plt.show()

       