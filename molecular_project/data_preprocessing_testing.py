import networkx as nx
import helper


def extract_clean_data(graphs_dict):
    """
    Extract cleaned molecular graph data.

    Parameters:
    - graphs_dict: dict of NetworkX graphs loaded from the original JSON file.

    Returns:
    - cleaned_dict: dict with SMILES strings as keys and specific node/edge data as values.
    """
    cleaned_dict = {}

    for smiles, graph in graphs_dict.items():
        # Extract node features
        node_id_features = {}
        for node_id, node_data in graph.nodes(data=True):
            node_features = {
                "atomic": node_data["atomic"],
                "valence": node_data["valence"],
                "formal_charge": node_data["formal_charge"],
                "aromatic": node_data["aromatic"],
                "hybridization": node_data["hybridization"],
                "radical_electrons": node_data["radical_electrons"]
            }
            node_id_features[node_id] = node_features

        # Extract edge features
        edges = []
        for source, target, edge_data in graph.edges(data=True):
            edge_features = {
                "type": edge_data["type"],
                "stereo": edge_data["stereo"],
                "aromatic": edge_data["aromatic"],
                "conjugated": edge_data["conjugated"]
            }
            edges.append({"source": source, "target": target, **edge_features})


        cleaned_dict[smiles] = {
            "node_id_feature": node_id_features,
            "edge_features": edges
        }

    return cleaned_dict


train_data = helper.load_data_from_file("data.json")
cleaned_data = extract_clean_data(train_data)
print(cleaned_data)













