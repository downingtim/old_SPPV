# 2026-01-30

Code to make a  maximum likelihood phylogeny of the SPPV samples with GTPV, LSDV, and the nine most closely related chordopox species based on the KX894508.1 core genome coordinates corresponding to CDSs LSDV027-LSDV123.

Data:
SPPV samples, GTPV samples, two LSDV samples, and 9 chordopox ones. The data for the nine chordopox species came from: deerpox virus NC_006966.1, Yaba-like disease virus NC_002642.1, Yaba monkeypox tumour virus NC_005179.1, Cotia virus NC_016924.1, BeAn virus NC_032111.1, Rabbit fibroma virus NC_001266.1, Myxoma virus NC_001132.2, Swinepox virus NC_003389.1, and Eptesipox virus NC_035460.1.

Adding in more published LSDV WT core genomes had no effect on the topology, and so two are shown here for visual clarity.

[1] Align the genomes with Mafft v7.453 (Katoh and Standley, 2013) using automatic optimisation and default parameters.

[2] Split the genomes with split_aln.py

[3] The evolutionary relationships of this core genome dataset were reconstructed using RAxML-NG v1.2.0 (Kozlov et al., 2019) with 1,000 bootstraps and with a GTR model and gamma substitution rate heterogeneity, selected by modeltest-ng (Darriba et al., 2020). The phylogeny was rooted using the nine non-capripoxvirus chordopox samples, and was visualised using ape v5.7-1 (Paradis and Schliep, 2019), ggtree v3.8.2 (Yu et al., 2017), phangorn v2.11.1 (Schliep, 2011) and phytools v2.0-3 (Revell, 2024).
