import networkx as nx

def build_graph():
    G = nx.Graph()
    G.add_edge("Febracis", "empresa de cursos de inteligência emocional")
    G.add_edge("Método CIS", "coaching e inteligência emocional")
    G.add_edge("Facilitadores", "coaching e PNL")
    G.add_edge("Benefícios", "aumento de performance")
    return G

def export_graph_as_text(G):
    lines = []
    for source, target in G.edges():
        lines.append(f"{source} está relacionado a {target}.")
    return "\n".join(lines)
