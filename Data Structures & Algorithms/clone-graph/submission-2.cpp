/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (node == nullptr) return nullptr;
        std::unordered_map<Node*, Node*> seen;
        std::queue<Node*> q;
        Node* head = new Node{node->val};
        seen[node] = head;
        q.push(node);

        while (!q.empty()) {
            Node* curr = q.front();
            q.pop();

            Node* curr_clone = seen[curr];
            for (const auto& n : curr->neighbors) {
                if (!seen.contains(n)) {
                    seen[n] = new Node{n->val};
                    q.push(n);
                }
                curr_clone->neighbors.push_back(seen[n]);
            }
        }
/*
inside queue: in the map but neighbors not processed. fully through queue = neighbors fully processed.
*/
        return head;
    }
};
