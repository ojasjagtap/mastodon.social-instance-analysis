# mastodon.social-instance-analysis
This project retrieves users from the mastodon.social instance, creates a directed graph representing follower relationships, computes eigenvector centrality, and visualizes the network using Matplotlib and NetworkX.

Prerequisites:

Before running the program, make sure you have the following:
- Python 3.x installed on your machine.
- The required dependencies installed. You can install them by running pip install -r requirements.txt.

Getting Started:

Clone this repository to your local machine.
Populate the config.py file with your Mastodon API information. The file should contain the following variables:
- CLIENT_KEY: Your Mastodon client key.
- CLIENT_SECRET: Your Mastodon client secret.
- ACCESS_TOKEN: Your Mastodon access token.

Run the user_collection.py script to collect users from the Mastodon instance and save them to a file.

Run the network_analysis.py script to compute eigenvector centrality and visualize the network.

Customization:

You can modify the api_base_url variable in user_collection.py to specify a different Mastodon instance.
Adjust the visualization settings in network_analysis.py to customize the appearance of the network plot.
