library(ape)
library(ggplot2)  # Add this!
library(ggtree)
# iqtree -s all.core2.aln -m "GTR+FO*H4" -bb 1000 -nt 55
region1="iqtree_core"
tree_all <- read.tree("all.core2.aln.treefile")

# Extract first tree if multiPhylo
if (class(tree_all) == "multiPhylo") {
  tree_all <- tree_all[[1]]
}

chordopox_tips <- c(
  "NC_006966.1", "NC_002642.1", "NC_005179.1",
  "NC_016924.1", "NC_032111.1", "NC_001266.1",
  "NC_001132.2", "NC_003389.1", "NC_035460.1")

## Find and root on outgroup
og <- intersect(chordopox_tips, tree_all$tip.label)

if (length(og) >= 2) {
  tree_all <- root(phy = tree_all, outgroup = og, resolve.root = TRUE)
}

# Ladderize
tree_all <- ladderize(tree_all)

# Color tips
tip_colours <- ifelse(
  grepl("LSDV", tree_all$tip.label), "darkgreen",
  ifelse(grepl("GTPV", tree_all$tip.label), "blue",
    ifelse(grepl("SPPV", tree_all$tip.label), "red", "black")))

p_tree_all <- ggtree(tree_all) +
  geom_tiplab(color = tip_colours, size = 2) +
  theme_tree2() +
  coord_cartesian(clip = 'off') +
  theme(plot.margin = margin(0, 30, 0, 0, "mm"))

ggsave(paste0("GENOME/",region1,".tree.pdf"),
 p_tree_all, width =7, height =7)

