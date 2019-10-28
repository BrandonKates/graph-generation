import networkx as nx
import numpy as np


class Args():
	def __init__(self):
		self.graph_type = 'fast_gnp_random_graph'
		self.num_graphs = 10
		self.num_nodes = 10
		self.prob = 0.5
		self.random_weights = True
		self.weight_fn = np.random.random
		self.get_spanning_trees = True

def create(args):
	graphs = []
	if args.graph_type == 'fast_gnp_random_graph':
		for i in range(args.num_graphs):
			graphs.append(nx.fast_gnp_random_graph(args.num_nodes, args.prob))


	if args.random_weights:
		add_edge_weights(graphs, args.weight_fn)

	spanning_trees = []
	if args.get_spanning_trees:
		for G in graphs:
		    T = nx.minimum_spanning_tree(G)
		    spanning_trees.append(T)
	return graphs, spanning_trees

def plot(graphs, spanning_trees = None):
	if not spanning_trees and len(graphs) != len(spanning_trees):
		# plot graphs
		for G in graphs:
			nx.drawing.nx_pylab.draw_networkx(G)
		    plt.show()
	else:
		# plot graphs and spanning_trees
		for G, T in zip(graphs, spanning_trees):
			nx.drawing.nx_pylab.draw_networkx(G)
		    plt.show()
		    nx.drawing.nx_pylab.draw_networkx(T)
		    plt.show()

def add_edge_weights(graphs, weight_fn = np.random.random):
	for G in graphs:
		for (u,v,weight) in G.edges(data=True):
			G.add_edge(u,v, weight=weight_fn())


if __name__ == "__main__":
	args = Args()
	graphs = create(args)