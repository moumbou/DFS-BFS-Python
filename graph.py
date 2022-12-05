from dataclasses import dataclass
import networkx as nx
import matplotlib.pyplot as plt

# ICI ON VA UTILISEZ LA METHODE DATACLASS QUI EST BCP PLUS 
# SIMPLE A UTILISER POUR CREER UNE CLASS
@dataclass
class Graph:
    # LES ENTRES GRAPH ET INDEX SONT DES LISTES VIDE POUR LES UTILISER TEMPORAIREMENT
    graph: list
    index: list
    # NEWLIST EST UN DICTIONNAIRE AVEC LE QUEL ON VA STOCKER LE RESULTAT FINAL
    newList: dict

    # ON DEFINI UNE FONCTION CONVERTTOGRAPH QUI VA PRENDRE COMME PARAMETRE SELF
    # AFIN DACCEDER LES VARIABLE GRAPH,INDEX,NEWLIST ET MEME LA FONCTION EN ELLE MEME
    def convertToGraph(self) -> dict:
        # VERIFIER SI LE LA LISTE DONNE EST UNE LISTE DE TUPLE
        # OU DE DISCTIONNAIRE
        tempListConvert = []
        if self.graph[0] and type(self.graph[0]) is tuple or list:
            for t in self.graph:
                a, b = t
                tempListConvert.append({a: b})
            self.graph = tempListConvert

        # DANS CETTE LOOP ON VA RETIRER TOUT LES INDEX DE LA LISTE
        # DU DICTIONNAIRE DONNE SANS REPITION
        # EN DAUTRE TERME ON AURA PAS DEUX INDEX OU CLE DU MEME TYPE
        # EXP : [0,0,1,2,2] MAIS PLUS TOT [0,1,2] SEULEMENT
        for n in self.graph:
            for i in n:
                a = i
                b = n[i]
                if a not in self.index:
                    self.index.append(a)
                if b not in self.index:
                    self.index.append(b)

        # APRES AVOIR OBTENU TOUT LES INDEX QUI EXISTE DANS LA LISTE
        # ON VA POUVOIR TRIER LES NOEUDS
        for i in self.index:
            # CECI EST UNE LISTE TEMPORAIRE QUI SE REINITIALISE A 
            # CHAQUE DEBUT DE LA LOOP
            tempList=[]
            for node in self.graph:
                # LE IF ICI EST TRES IMPORTANT POUR EVITER 
                # QUE NOTRE LOOP NE CASSE
                if i in node:
                    tempList.append(node[i])
            # APRES AVOIR TRIER LES NOEUDS DE LA MEME CLE 
            # OU INDEX ON VA POUVOIR INSERER LE TOUT DANS NOTRE DICTIONNAIRE
            self.newList[i]=tempList
        
        # ON RETOURNE LE RESULTAT SOUS FORME DE DICTIONNAIRE ET VOILA !
        return self.newList

    def draw(newGraph):
        G = nx.DiGraph()
        G.add_edges_from(newGraph)
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, node_size=500)
        nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
        nx.draw_networkx_labels(G, pos)
        plt.show()
    
    def convertToTuple(result):
        newGraph = []
        for i, x in enumerate(result):
            if i != 0:
                newGraph.append((result[i - 1], x))
        return newGraph