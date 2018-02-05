
class Node:
    """
    base class
    items in a base class implements common things among classes
    """
    def __init__(self, name, cost, utility):
        self.name = name
        self.cost = cost
        self.utility = utility

    def get_expected_cost(self):
        # returns expected cost of this node; abstract method to be overridden in derived class
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes")

    def get_expected_utility(self):
        # return expected utility of this node; abstract to be overridden in derived class
        raise NotImplementedError("This is an abstract method and needs to be implemeted in derived class")


class ChanceNode(Node):
    def __init__(self, name, cost, utility, probs, future_nodes):
        """

        :param name: name of this chance node
        :param cost: cost of visiting this node
        :param probs: probabilities of visiting future nodes
        :param future_nodes: a list of future node objects connected to this node
        """
        Node.__init__(self, name, cost, utility)
        self.probs = probs
        self.future_nodes = future_nodes

    def get_expected_cost(self):
        # return expected cost of this chance node

        exp_cost = self.cost  # the expected cost of this node including the cost of visiting this node
        i = 0  # index to iterate over probabilities
        for thisNode in self.future_nodes:
            exp_cost += self.probs[i] * thisNode.get_expected_cost()
            i += 1

        return exp_cost

    def get_expected_utility(self):
        exp_util = self.utility
        i = 0
        for thisNode in self.future_nodes:
            exp_util += self.probs[i] * thisNode.get_expected_utility()
            i += 1
        return exp_util


class TerminalNode(Node):
    def __init__(self, name, cost, utility):
        Node.__init__(self, name, cost, utility)

    def get_expected_cost(self):
        # return the cost of this terminal node
        return self.cost

    def get_expected_utility(self):
        # return the utility of this terminal node
        return self.utility


class DecisionNode(Node):
    def __init__(self, name, cost, utility, future_nodes):
        Node.__init__(self, name, cost, utility)
        self.future_nodes = future_nodes  # list of future node objects

    def get_expected_cost(self):

        """ :return the expected cost of associated future nodes"""
        cost_outcomes = dict()  # dictionary to store expected cost of future nodes
        for thisNode in self.future_nodes:
            cost_outcomes[thisNode.name] = thisNode.get_expected_cost()

        return cost_outcomes

    def get_expected_utility(self):
        util_outcomes = dict()
        for thisNode in self.future_nodes:
            util_outcomes[thisNode.name] = thisNode.get_expected_utility()

        return util_outcomes


# creating terminal node 1
T1 = TerminalNode("T1", cost=10, utility=0.9)
T2 = TerminalNode("T2", cost=20, utility=0.8)
T3 = TerminalNode("T3", cost=30, utility=0.7)
T4 = TerminalNode("T4", cost=40, utility=0.6)
T5 = TerminalNode("T5", cost=50, utility=0.5)


# Creating Chance nodes
C2 = ChanceNode("C2", cost=35, utility=0, probs=[0.7, 0.3], future_nodes=[T1, T2])
C1 = ChanceNode("C1", cost=25, utility=0, probs=[0.2, 0.8], future_nodes=[C2, T3])
C3 = ChanceNode("C3", cost=45, utility=0, probs=[0.1, 0.9], future_nodes=[T4, T5])

# Decision
D1 = DecisionNode("D1", cost=0, utility=0, future_nodes=[C1, C3])

print("Expected costs are", D1.get_expected_cost())
print("Expected utilities are", D1.get_expected_utility())
