import pandas as pd
import networkx as nx
from pyvis.network import Network

class friendCharacterNetworkGenerator():
    def __init__(self):
        pass


# Function to generate character network
    def generate_character_network(df):
        windows = 10
        entity_relationship = []

        # Iterate over rows in the DataFrame
        for index, row in df.iterrows():
            speaker = row['Speaker']  # Get the speaker's name
            current_entities = row['ners']  # Get NER entities from the dialogue

            previous_entities_in_window = []

            for entity_set in current_entities:
                previous_entities_in_window.append(list(entity_set))
                previous_entities_in_window = previous_entities_in_window[-windows:]

                previous_entities_flattened = sum(previous_entities_in_window, [])

                for entity in entity_set:
                    # Create relationships with previous entities and the speaker
                    for entity_in_window in previous_entities_flattened:
                        if entity != entity_in_window:
                            entity_relationship.append(sorted([speaker, entity_in_window]))

        relationship_df = pd.DataFrame({'value': entity_relationship})
        relationship_df['source'] = relationship_df['value'].apply(lambda x: x[0])
        relationship_df['target'] = relationship_df['value'].apply(lambda x: x[1])
        relationship_df = relationship_df.groupby(['source', 'target']).count().reset_index()
        relationship_df = relationship_df.sort_values('value', ascending=False)

        return relationship_df

    def draw_network_graph(self,relationship_df):
        relationship_df = relationship_df.sort_values('value', ascending=False)
        relationship_df = relationship_df.head(200)


        # Create the network graph
        G = nx.from_pandas_edgelist(
            relationship_df,
            source='source',
            target='target',
            edge_attr='value',
            create_using=nx.Graph()
        )

        # Visualize the network
        net = Network(notebook=True, width="1000px", height="700px", bgcolor="#222222", font_color="white", cdn_resources="remote")

        # Set node size based on their degree
        node_degree = dict(G.degree)
        nx.set_node_attributes(G, node_degree, 'size')

        # Add the networkx graph to pyvis
        net.from_nx(G)

        # Inject custom JavaScript for edge highlighting and displaying relationship info
        highlight_js = """
        <script type="text/javascript">
            var relationLabel = document.createElement('div');
            relationLabel.id = 'relation-info';
            relationLabel.style.position = 'absolute';
            relationLabel.style.top = '10px';
            relationLabel.style.right = '10px';
            relationLabel.style.padding = '12px';
            relationLabel.style.backgroundColor = 'rgba(50, 50, 50, 0.8)';
            relationLabel.style.color = 'white';
            relationLabel.style.fontSize = '16px';
            relationLabel.style.borderRadius = '5px';
            relationLabel.style.zIndex = '999';
            relationLabel.innerHTML = 'Click on a branch to see relation info';
            document.body.appendChild(relationLabel);

            network.on('click', function(properties) {
                network.body.data.edges.update(network.body.data.edges.get().map(edge => ({ id: edge.id, color: '#97C2FC' })));

                var clickedNode = properties.nodes[0];

                if (clickedNode !== undefined) {
                    network.body.data.edges.get().forEach(edge => {
                        if (edge.from === clickedNode || edge.to === clickedNode) {
                            network.body.data.edges.update({ id: edge.id, color: 'yellow' });
                        }
                    });
                }
            });

            network.on('click', function(properties) {
                var clickedEdgeId = properties.edges[0];

                if (clickedEdgeId !== undefined) {
                    var clickedEdge = network.body.data.edges.get(clickedEdgeId);
                    var source = network.body.data.nodes.get(clickedEdge.from).label;
                    var target = network.body.data.nodes.get(clickedEdge.to).label;
                    var value = clickedEdge.value;

                    relationLabel.innerHTML =
                        '<strong>Relationship Info:</strong><br>' +
                        'Person1 : ' + source + '<br>' +
                        'Person2 : ' + target + '<br>' +
                        'Strength : ' + value;
                }
            });
        </script>
        """

        # Save the network to an HTML file in the current directory
        file_name = "friends_character_network.html"  # Save in current directory
        net.show(file_name)

        # Append the custom JavaScript to the HTML file
        with open(file_name, "a") as f:
            f.write(highlight_js)

        # Return the file name
        return file_name