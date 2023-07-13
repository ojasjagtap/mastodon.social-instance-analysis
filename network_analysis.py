import config
from mastodon import Mastodon
import networkx as nx
import matplotlib.pyplot as plt
import pause


def authenticate_mastodon():
    client_key = config.CLIENT_KEY
    client_secret = config.CLIENT_SECRET
    access_token = config.ACCESS_TOKEN
    api_base_url = "mastodon.social"

    m = Mastodon(
        client_id=client_key,
        client_secret=client_secret,
        access_token=access_token,
        api_base_url=api_base_url
    )
    return m


def load_users_from_file(filename):
    users = []
    with open(filename, "r") as file:
        for line in file:
            users.append(line.strip())
    return users


def create_follower_graph(users, mastodon):
    graph = nx.DiGraph()
    for user in users:
        if mastodon.ratelimit_remaining > 1:
            username = mastodon.account(user)['username']
            graph.add_node(username)
            followers = mastodon.account_followers(user)
            for follower_info in followers:
                follower_username = follower_info['username']
                graph.add_edge(follower_username, username)
        else:
            pause.until(mastodon.ratelimit_reset)
    return graph


def calculate_eigenvector_centrality(graph):
    return nx.eigenvector_centrality(graph, max_iter=1000)


def visualize_network(graph, centrality):
    node_sizes = [centrality[node] * 10000 for node in graph.nodes()]
    plt.figure(figsize=(12, 10))
    nx.draw_networkx(
        graph,
        alpha=0.7,
        with_labels=True,
        font_size=8,
        node_color=node_sizes,
        cmap='Blues',
        edge_color='gray'
    )
    plt.title(f"mastodon.social User Network")
    plt.axis('off')
    plt.show()


users = load_users_from_file("users.txt")
mastodon = authenticate_mastodon()
graph = create_follower_graph(users, mastodon)
centrality = calculate_eigenvector_centrality(graph)
visualize_network(graph, centrality)
