import networkx as nx
import numpy as np
from scipy.spatial.distance import cdist
from matplotlib import pyplot as plt

class Args():
	def __init__(self):
		self.graph_type = 'random_geometric_graph'
		self.num_graphs = 10
		self.num_nodes = 10
		self.prob = 0.5
		self.random_weights = False
		self.weight_fn = np.random.random
		self.get_spanning_trees = True

def create(args):
	graphs = []
	poses = []
	if args.graph_type == 'fast_gnp_random_graph':
		for i in range(args.num_graphs):
			graphs.append(nx.fast_gnp_random_graph(args.num_nodes, args.prob))

	elif args.graph_type == 'random_geometric_graph':
		for i in range(args.num_graphs):
			G = nx.generators.geometric.random_geometric_graph(args.num_nodes, 2, 2)
			pos = nx.random_layout(G)
			positions = np.array([pos[n] for n in pos])
			G.add_weighted_edges_from(get_distances(positions, args.num_nodes))
			graphs.append(G)
			poses.append(pos)

	if args.random_weights:
		add_edge_weights(graphs, args.weight_fn)

	spanning_trees = []
	if args.get_spanning_trees:
		for G in graphs:
			T = nx.minimum_spanning_tree(G)
			spanning_trees.append(T)
	return graphs, spanning_trees, poses

def plot(graphs, spanning_trees = None, poses = None):
	if not poses:
		poses = [None]*len(graphs)

	if not spanning_trees:
		spanning_trees = [None]*len(graphs)
	
	assert len(spanning_trees) == len(graphs) == len(poses)
	for (G,T,pos) in zip(graphs, spanning_trees, poses):
		plot_single(G,T,pos)

	#plt.savefig('./graphs-spanning_tree.png')

def plot_single(G,T=None,pos=None):
	if not pos:
		pos = nx.spring_layout(G)
	nx.drawing.nx_pylab.draw_networkx(G, pos=pos)
	plt.show()
	if T:
		nx.drawing.nx_pylab.draw_networkx(T, pos=pos)
		plt.show()


def add_edge_weights(graphs, weight_fn = np.random.random):
	for G in graphs:
		for (u,v,weight) in G.edges(data=True):
			G.add_edge(u,v, weight=weight_fn())

def get_distances(x, num_nodes):
	dist = cdist(x,x, metric='euclidean')
	return [(i,j,dist[i,j]) for i in range(num_nodes) for j in range(i)] # ebunch

if __name__ == "__main__":
	args = Args()
	graphs, msts = create(args)
	print(graphs[0].adjacency)
	#plot(graphs, msts)
