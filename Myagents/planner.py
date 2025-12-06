class PlannerAgent:
    def __init__(self, topics, difficulty):
        self.topics = topics
        self.difficulty = difficulty

    def plan_topics(self):
        # Basic prioritization logic
        topic_weights = {
            t: 1 + (self.difficulty[t] - 1) * 0.4  # harder topics → higher weight
            for t in self.topics
        }

        # Sorted by difficulty
        sorted_topics = sorted(topic_weights.keys(), key=lambda x: topic_weights[x], reverse=True)

        return {
            "topic_order": sorted_topics,
            "weights": topic_weights
        }
