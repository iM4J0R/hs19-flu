from ete3 import Tree, NodeStyle, TreeStyle
import csv


def visualize_tree(csv_path, newick, threshold):
    """
    Shows the tree in an ETE window
    :param csv_path: Information about nodes/tips that need to be displayed.
    :param newick: Phylo tree in newick format.
    :param threshold: Threshold of when to show as green, otherwise red
    :return: null
    """
    results = list(csv.reader(open(csv_path)))
    # Load tree with ETE
    t = Tree(newick)

    # Stylize the entire tree
    ts = TreeStyle()
    ts.show_leaf_name = True
    ts.branch_vertical_margin = 99
    ts.scale = 9999

    # Define colours
    green = "#00ff00"
    red = "#ff0000"
    grey = "#9c9c9c"

    # i is just a variable used for debugging
    i = 0

    # Traverse through the entire tree, processing all tips
    for n in t.traverse():
        if n.is_leaf():
            tipPredicted = False
            for result in results:
                if result[1] == n.name:
                    tipPredicted = True
                    if float(result[2]) > threshold:
                        color = green
                    else:
                        color = red
                    nstyle = NodeStyle()
                    nstyle["fgcolor"] = color
                    nstyle["size"] = 500
                    n.set_style(nstyle)
                    i += 1
                    break
            if not tipPredicted:
                n.delete()
        else:
            for result in results:
                if result[1] == n.name:
                    if float(result[2]) > threshold:
                        color = green
                    else:
                        color = red
                    nstyle = NodeStyle()
                    nstyle["fgcolor"] = color
                    nstyle["size"] = 99
                    n.set_style(nstyle)
                    i += 1;
                    break

    t.show(tree_style=ts)


visualize_tree("../visualization/result1.csv", "../clade_assignments/trees/flutree2018_5.nwk", 0.8)
