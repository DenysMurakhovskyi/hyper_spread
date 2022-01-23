from dataclasses import dataclass, asdict
from networkx import Graph
import numpy as np
import pandas as pd
from typing import Union, Literal

from app import Metrics


@dataclass
class GraphData:

    n_of_nodes: int = 70
    graph_type: Union[Literal['ER'], Literal['WS'], Literal['SW']] = 'ER'
    p1: float = 0.3
    p2: float = 0
    k: int = 0

    def __repr__(self):
        return f'Graph type: {self.graph_type}, number of nodes: {self.n_of_nodes}'

    def return_kwargs(self):
        return asdict(self)


@dataclass
class SimulationData:

    p_trans: float = 0.3
    t_rec: int = 14
    t_sus: np.float64 = 180


@dataclass
class SimulationResult:

    n_of_infected: pd.Series  # represents number of infected by each node
    nodes_state: pd.Series  # represents final states of nodes to mark infected nodes on the graph

@dataclass
class MeasuredGraph:

    G: Graph = Graph()
    metrics: Metrics = Metrics(0, 0)


