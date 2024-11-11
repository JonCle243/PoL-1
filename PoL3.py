# Exercise 1.3.1

# Given values
translation_rate = 12  # amino acids per second per ribosome
division_time_minutes = 30  # division time in minutes
total_protein_amino_acids = 1e9  # total amino acids in cell proteins
ribosome_size_amino_acids = 8000  # amino acids per ribosome

# Convert division time to seconds
division_time_seconds = division_time_minutes * 60

# Calculate amino acids produced by one ribosome per cycle
amino_acids_per_ribosome = translation_rate * division_time_seconds

# Calculate the total number of ribosomes needed
num_ribosomes = total_protein_amino_acids / amino_acids_per_ribosome

# Calculate the fraction of ribosomal protein in the total protein pool
ribosomal_protein_amino_acids = num_ribosomes * ribosome_size_amino_acids
ribosomal_fraction = ribosomal_protein_amino_acids / total_protein_amino_acids

# Display results
print(f"Number of ribosomes needed: {num_ribosomes:.0f}")
print(f"Fraction of ribosomal protein in total protein pool: {ribosomal_fraction:.2f}")

# Exercise 1.3.2

# Given values
translation_rate = 20  # amino acids per second per ribosome
division_time_minutes = 30  # division time in minutes
total_protein_amino_acids = 1e9  # total amino acids in cell proteins
ribosome_size_amino_acids = 8000  # amino acids per ribosome

# Convert division time to seconds
division_time_seconds = division_time_minutes * 60

# Calculate amino acids produced by one ribosome per cycle
amino_acids_per_ribosome = translation_rate * division_time_seconds

# Calculate the total number of ribosomes needed
num_ribosomes = total_protein_amino_acids / amino_acids_per_ribosome

# Calculate the fraction of ribosomal protein in the total protein pool
ribosomal_protein_amino_acids = num_ribosomes * ribosome_size_amino_acids
ribosomal_fraction = ribosomal_protein_amino_acids / total_protein_amino_acids

# Display results
print(f"Number of ribosomes needed: {num_ribosomes:.0f}")
print(f"Fraction of ribosomal protein in total protein pool: {ribosomal_fraction:.2f}")